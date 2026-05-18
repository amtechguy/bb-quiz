#!/usr/bin/env python3
"""
bb-quiz — Terminal AWS Cloud Practitioner Quiz
Offline terminal quiz app with beautiful Rich UI.
"""

import sys
import os
import json
import random
import re
import time
from datetime import datetime
from pathlib import Path

try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.table import Table
    from rich.text import Text
    from rich.prompt import Prompt, Confirm
    from rich import box
    from rich.align import Align
    from rich.rule import Rule
    from rich.columns import Columns
    from rich.padding import Padding
except ImportError:
    print("Missing dependency: run  pip install rich  then try again.")
    sys.exit(1)

# ── Path resolution (works both as script and PyInstaller binary) ─────────────
if getattr(sys, "frozen", False):
    _APP_HOME = Path.home() / ".local" / "share" / "bb-quiz"
    BANKS_DIR = _APP_HOME / "banks"
    DATA_DIR  = _APP_HOME / "data"
else:
    _APP_HOME = Path(__file__).parent
    BANKS_DIR = _APP_HOME / "banks"
    DATA_DIR  = _APP_HOME / "data"

HISTORY_FILE = DATA_DIR / "history.json"
DATA_DIR.mkdir(parents=True, exist_ok=True)

console = Console()

# ── Colour palette ────────────────────────────────────────────────────────────
PRIMARY   = "bright_cyan"
ORANGE    = "dark_orange"
SUCCESS   = "bright_green"
DANGER    = "bright_red"
WARNING   = "yellow"
MUTED     = "grey70"
DIM       = "grey42"
WHITE     = "bold white"
SUBTLE    = "grey50"

# ══════════════════════════════════════════════════════════════════════════════
# PARSER
# ══════════════════════════════════════════════════════════════════════════════

def parse_bank(path: Path) -> list[dict]:
    text = path.read_text(encoding="utf-8").replace("\r", "")
    blocks = [b.strip() for b in text.split("---") if b.strip()]
    questions = []

    for block in blocks:
        lines = [l.strip() for l in block.splitlines() if l.strip()]

        q_line = next(
            (l for l in lines if re.match(r"^\*\*\d+\.", l) or re.match(r"^\d+\.", l)),
            None,
        )
        if not q_line:
            continue
        question = re.sub(r"^\*\*\d+\.\*\*\s*", "", q_line)
        question = re.sub(r"^\d+\.\s*", "", question)
        question = re.sub(r"\*\*(.*?)\*\*", r"\1", question).strip()

        options, correct = [], []
        for line in lines:
            m = re.match(r"^[-*]\s*([A-E])\.\s*(.+)", line)
            if not m:
                continue
            raw = m.group(2)
            opt_text = re.sub(r"✅\s*$", "", raw).replace("**", "").strip()
            if "✅" in raw:
                correct.append(opt_text)
            options.append(opt_text)

        if len(options) < 2 or not correct:
            continue

        exp_line = next(
            (l for l in lines if re.match(r"^\*\*Explanation:\*\*", l, re.I)
                               or re.match(r"^Explanation:", l, re.I)),
            None,
        )
        explanation = ""
        if exp_line:
            explanation = re.sub(r"^\*\*Explanation:\*\*\s*", "", exp_line, flags=re.I)
            explanation = re.sub(r"^Explanation:\s*", "", explanation, flags=re.I).strip()

        questions.append({
            "question":    question,
            "options":     options,
            "correct":     correct,
            "explanation": explanation,
            "multi":       len(correct) > 1,
        })

    return questions


def load_all_banks() -> dict[str, list[dict]]:
    source_banks = {}
    topic_banks  = {}

    for f in sorted(BANKS_DIR.glob("*.md")):
        qs = parse_bank(f)
        if qs:
            title = f.stem.replace("_", " ").title()
            source_banks[title] = qs

    TOPIC_LABELS = {
        "ai_ml":                  "AI & Machine Learning",
        "analytics":              "Analytics",
        "cdn_global":             "CloudFront & Global Network",
        "cloud_adoption":         "Cloud Adoption Framework (CAF)",
        "cloud_concepts":         "Cloud Computing Concepts",
        "connectivity":           "Hybrid Connectivity (VPN & Direct Connect)",
        "cost_billing":           "Cost Management & Billing",
        "databases":              "Databases (RDS, DynamoDB, Aurora…)",
        "devops_deploy":          "DevOps & Deployment Tools",
        "ec2":                    "Amazon EC2",
        "general":                "General AWS",
        "iam":                    "IAM & Identity",
        "migration":              "Migration Services",
        "monitoring_audit":       "Monitoring & Auditing",
        "s3":                     "Amazon S3",
        "security_compliance":    "Security & Compliance",
        "serverless_containers":  "Serverless & Containers",
        "shared_responsibility":  "Shared Responsibility Model",
        "storage":                "Storage (EBS, EFS, Snowball…)",
        "support_plans":          "AWS Support Plans",
        "vpc_networking":         "VPC & Networking",
        "well_architected":       "Well-Architected Framework",
    }
    topics_dir = BANKS_DIR / "topics"
    if topics_dir.exists():
        for f in sorted(topics_dir.glob("*.md")):
            qs = parse_bank(f)
            if qs:
                label = TOPIC_LABELS.get(f.stem, f.stem.replace("_", " ").title())
                topic_banks[label] = qs

    return source_banks, topic_banks


# ══════════════════════════════════════════════════════════════════════════════
# HISTORY
# ══════════════════════════════════════════════════════════════════════════════

def load_history() -> list[dict]:
    if HISTORY_FILE.exists():
        try:
            return json.loads(HISTORY_FILE.read_text())
        except Exception:
            return []
    return []


def save_history(record: dict):
    history = load_history()
    history.append(record)
    HISTORY_FILE.write_text(json.dumps(history, indent=2))


def get_exam_streak() -> tuple[int, int]:
    """Return (current_pass_streak, best_pass_streak) for exam mode."""
    history = load_history()
    exams = [r for r in history if r.get("mode") == "exam"]
    if not exams:
        return 0, 0
    streak = 0
    best   = 0
    for r in reversed(exams):
        if r.get("passed"):
            streak += 1
            best = max(best, streak)
        else:
            break
    # Also scan full list for all-time best
    cur = 0
    for r in exams:
        if r.get("passed"):
            cur += 1
            best = max(best, cur)
        else:
            cur = 0
    return streak, best


# ══════════════════════════════════════════════════════════════════════════════
# UI HELPERS
# ══════════════════════════════════════════════════════════════════════════════

def clear():
    console.clear()


def banner():
    """Print the app banner."""
    console.print()
    logo = Text()
    logo.append("  ☁  ", style=f"bold {PRIMARY}")
    logo.append("bb", style=f"bold {ORANGE}")
    logo.append("-", style=f"bold {MUTED}")
    logo.append("quiz", style=f"bold {PRIMARY}")
    console.print(Align.center(logo))
    console.print(
        Align.center(
            Text("AWS Cloud Practitioner  ·  Offline  ·  1989+ Questions", style=MUTED)
        )
    )
    console.print()


# ══════════════════════════════════════════════════════════════════════════════
# EXAM MODE
# ══════════════════════════════════════════════════════════════════════════════

# Real CLF-C02 domain weights → mapped to our topic banks
# Security & Compliance  30% = 20 q
# Cloud Tech & Services  34% = 22 q
# Cloud Concepts         24% = 16 q
# Billing & Support      12% =  7 q  → total 65
EXAM_DOMAINS = [
    {
        "name":    "Domain 1 — Security & Compliance",
        "color":   DANGER,
        "weight":  30,
        "count":   20,
        "topics":  [
            ("iam",                8),
            ("security_compliance", 7),
            ("shared_responsibility", 5),
        ],
    },
    {
        "name":    "Domain 2 — Cloud Technology & Services",
        "color":   PRIMARY,
        "weight":  34,
        "count":   22,
        "topics":  [
            ("ec2",                    5),
            ("s3",                     4),
            ("vpc_networking",         3),
            ("databases",              3),
            ("serverless_containers",  2),
            ("storage",               2),
            ("monitoring_audit",      2),
            ("cdn_global",            1),
        ],
    },
    {
        "name":    "Domain 3 — Cloud Concepts",
        "color":   WARNING,
        "weight":  24,
        "count":   16,
        "topics":  [
            ("cloud_concepts",   6),
            ("well_architected", 5),
            ("cloud_adoption",   3),
            ("devops_deploy",    2),
        ],
    },
    {
        "name":    "Domain 4 — Billing, Pricing & Support",
        "color":   ORANGE,
        "weight":  12,
        "count":   7,
        "topics":  [
            ("cost_billing",   4),
            ("support_plans",  3),
        ],
    },
]


def build_exam_pool() -> list[dict] | None:
    """Build a 65-question pool weighted like the real CCP exam."""
    topics_dir = BANKS_DIR / "topics"
    if not topics_dir.exists():
        return None

    # Load all topic banks
    loaded = {}
    for f in topics_dir.glob("*.md"):
        qs = parse_bank(f)
        if qs:
            loaded[f.stem] = qs

    pool = []
    for domain in EXAM_DOMAINS:
        for topic_name, count in domain["topics"]:
            bank = loaded.get(topic_name, [])
            if bank:
                sample = random.sample(bank, min(count, len(bank)))
                for q in sample:
                    q["_domain"] = domain["name"]
                pool.extend(sample)

    random.shuffle(pool)
    for q in pool:
        random.shuffle(q["options"])
    return pool


def show_exam_results(results: list[dict], elapsed: float, streak: int, best: int):
    """Show the full exam results screen with domain breakdown."""
    clear()
    console.print()

    total   = len(results)
    correct = sum(1 for r in results if r["is_correct"])
    pct     = round((correct / total) * 100)
    passed  = pct >= 70
    mins    = int(elapsed // 60)
    secs    = int(elapsed % 60)

    if passed:
        grade, color, emoji = "PASS — Well Done!", SUCCESS, "🏆"
    else:
        grade, color, emoji = "FAIL — Keep Practicing", DANGER, "💪"

    # Big result panel
    console.print(Panel(
        Align.center(
            f"\n[bold {color}]{pct}%[/]   [{MUTED}]({correct}/{total} correct)[/]\n\n"
            f"[bold {color}]{emoji}  {grade}[/]\n\n"
            f"[{MUTED}]Time: {mins}m {secs}s   Pass mark: 70%[/]\n\n"
            f"[{WARNING}]Exam streak: {streak} 🔥   Best: {best}[/]\n"
        ),
        title=f"[bold {PRIMARY}]  ☁  AWS Cloud Practitioner Exam Simulation  [/]",
        border_style=color,
        padding=(1, 6),
        box=box.DOUBLE_EDGE,
    ))
    console.print()

    # Domain breakdown table
    section_rule("📊  Domain Breakdown")
    console.print()
    table = Table(box=box.SIMPLE_HEAD, header_style=f"bold {PRIMARY}", border_style=DIM, padding=(0,1))
    table.add_column("Domain",    style="white",  no_wrap=True)
    table.add_column("Weight",    justify="right", style=MUTED,  width=7)
    table.add_column("Score",     justify="right", width=8)
    table.add_column("Result",    justify="right", width=8)

    for domain in EXAM_DOMAINS:
        domain_results = [r for r in results if r.get("_domain") == domain["name"]]
        if not domain_results:
            continue
        d_correct = sum(1 for r in domain_results if r["is_correct"])
        d_total   = len(domain_results)
        d_pct     = round((d_correct / d_total) * 100)
        d_color   = SUCCESS if d_pct >= 70 else DANGER
        table.add_row(
            domain["name"].split(" — ")[1],
            f"{domain['weight']}%",
            f"{d_correct}/{d_total}",
            f"[bold {d_color}]{d_pct}%[/]",
        )

    console.print(Padding(table, (0, 2)))
    console.print()

    # Save to history
    save_history({
        "bank":    "Exam Simulation",
        "mode":    "exam",
        "score":   correct,
        "total":   total,
        "pct":     pct,
        "passed":  passed,
        "streak":  streak,
        "time":    f"{mins}m {secs}s",
        "date":    datetime.now().strftime("%Y-%m-%d %H:%M"),
    })

    # Review wrong answers
    wrong = [r for r in results if not r["is_correct"]]
    if wrong and Confirm.ask(f"  [{PRIMARY}]Review your {len(wrong)} incorrect answers?[/]", default=True):
        console.print()
        section_rule("❌  Wrong Answers")
        console.print()
        for i, r in enumerate(wrong):
            console.print(f"  [{DANGER}]✗[/]  [{MUTED}]{r['question'][:95]}{'…' if len(r['question'])>95 else ''}[/]")
            console.print(f"       [{MUTED}]You answered:[/]  [{DANGER}]{', '.join(r['chosen']) or 'None'}[/]")
            console.print(f"       [{MUTED}]Correct:      [/]  [{SUCCESS}]{', '.join(r['correct'])}[/]")
            if r.get("explanation"):
                console.print(Panel(
                    f"[italic {MUTED}]{r['explanation']}[/]",
                    title=f"[{WARNING}] 💡 [/]",
                    border_style=DIM,
                    padding=(0, 2),
                    box=box.SIMPLE,
                ))
            console.print()
    Prompt.ask(f"  [{DIM}]↵  Press Enter to return to main menu[/]", default="")


def run_exam():
    """Run a full 65-question exam simulation."""
    pool = build_exam_pool()
    if not pool or len(pool) < 20:
        console.print(f"\n  [{DANGER}]Not enough topic banks installed for Exam Mode.[/]")
        console.print(f"  [{MUTED}]Run the installer to ensure all topic banks are present.[/]\n")
        Prompt.ask(f"  [{DIM}]↵  Press Enter to go back[/]", default="")
        return

    results = []
    start   = time.time()

    for idx, q in enumerate(pool):
        clear()
        elapsed_so_far = time.time() - start
        mins = int(elapsed_so_far // 60)
        secs = int(elapsed_so_far % 60)

        console.print()
        console.print(
            f"  [bold {PRIMARY}]bb-quiz[/]  [dim]›[/]  [bold {ORANGE}]🎓 Exam Simulation[/]"
            f"   [{MUTED}]⏱ {mins:02d}:{secs:02d}[/]"
        )
        console.print()

        # Progress
        bar_len = 38
        filled  = int(bar_len * (idx + 1) / len(pool))
        bar     = f"[{ORANGE}]{'█' * filled}[/][{DIM}]{'░' * (bar_len - filled)}[/]"
        console.print(f"  {bar}  [{MUTED}]{idx+1}/{len(pool)}[/]")
        console.print()

        # Domain tag
        domain_name = q.get("_domain", "").split(" — ")[-1] if q.get("_domain") else ""
        console.print(f"  [{DIM}]Domain: {domain_name}[/]")
        console.print()

        is_multi = q["multi"]
        console.print(Panel(
            f"[bold white]{q['question']}[/]" + (
                f"\n\n[bold {WARNING}]★  Select {len(q['correct'])} answers[/]" if is_multi else ""
            ),
            title=f"[bold {ORANGE}] Question {idx + 1} of {len(pool)} [/]",
            border_style=ORANGE,
            padding=(1, 3),
            box=box.ROUNDED,
        ))
        console.print()

        for i, opt in enumerate(q["options"]):
            console.print(f"   [bold {ORANGE}]{letter(i)}[/][{DIM}].[/]  {opt}")
        console.print()

        if is_multi:
            need = len(q["correct"])
            while True:
                raw = Prompt.ask(
                    f"  [{ORANGE}]Your answers[/] [{MUTED}](choose {need}, e.g. A C)[/]"
                ).upper().split()
                chosen_letters = [c for c in raw if len(c) == 1 and c.isalpha()]
                chosen = [q["options"][ord(c)-65] for c in chosen_letters if 0 <= ord(c)-65 < len(q["options"])]
                if len(chosen) < need:
                    console.print(
                        f"  [{WARNING}]⚠  This question requires {need} answers — "
                        f"you selected {len(chosen)}. Press Enter to proceed anyway.[/]"
                    )
                    confirm = Prompt.ask(
                        f"  [{MUTED}]Continue with {len(chosen)} answer(s)? [y/n][/]",
                        default="y",
                    ).strip().lower()
                    if confirm in ("y", ""):
                        break
                else:
                    break
        else:
            while True:
                raw = Prompt.ask(
                    f"  [{ORANGE}]Your answer[/] [{MUTED}](A–{letter(len(q['options'])-1)})[/]"
                ).upper().strip()
                if len(raw) == 1 and raw.isalpha():
                    i = ord(raw) - 65
                    if 0 <= i < len(q["options"]):
                        chosen = [q["options"][i]]
                        break
                console.print(f"  [{DANGER}]  ✗  Enter a single letter only.[/]")

        is_correct = sorted(chosen) == sorted(q["correct"])

        # Brief feedback (no pause — exam pace)
        if is_correct:
            console.print(f"  [{SUCCESS}]✓  Correct![/]")
        else:
            console.print(f"  [{DANGER}]✗  Incorrect[/]   [{MUTED}]Correct: {', '.join(q['correct'])}[/]")

        results.append({
            "question":    q["question"],
            "chosen":      chosen,
            "correct":     q["correct"],
            "explanation": q.get("explanation", ""),
            "is_correct":  is_correct,
            "_domain":     q.get("_domain", ""),
        })

        console.print()
        if idx < len(pool) - 1:
            Prompt.ask(f"  [{DIM}]↵  Next question[/]", default="")

    elapsed = time.time() - start
    correct = sum(1 for r in results if r["is_correct"])
    pct     = round((correct / len(results)) * 100)
    passed  = pct >= 70

    # Update exam streak
    streak, best = get_exam_streak()
    if passed:
        streak += 1
        best = max(best, streak)
    else:
        streak = 0

    show_exam_results(results, elapsed, streak, best)


def section_rule(title: str, style: str = PRIMARY):
    console.print(Rule(f"[bold {style}]  {title}  [/]", style=DIM))


def letter(i: int) -> str:
    return chr(65 + i)


def progress_bar(current: int, total: int) -> str:
    bar_len = 38
    filled  = int(bar_len * current / total)
    bar     = f"[{PRIMARY}]{'█' * filled}[/][{DIM}]{'░' * (bar_len - filled)}[/]"
    pct     = int(100 * current / total)
    return f"  {bar}  [{MUTED}]{current}/{total}  ({pct}%)[/]"


# ══════════════════════════════════════════════════════════════════════════════
# QUIZ RUNNER
# ══════════════════════════════════════════════════════════════════════════════

def run_quiz(bank_title: str, questions: list[dict], rapid: bool = False):
    pool = random.sample(questions, min(20, len(questions))) if rapid else list(questions)
    random.shuffle(pool)
    for q in pool:
        random.shuffle(q["options"])

    results   = []
    correct_n = 0
    streak    = 0
    best_str  = 0

    for idx, q in enumerate(pool):
        clear()

        # Header strip
        mode_tag = f"  [bold {ORANGE}]⚡ RAPID[/]" if rapid else ""
        console.print()
        console.print(
            f"  [bold {PRIMARY}]bb-quiz[/]  [dim]›[/]  [{MUTED}]{bank_title}[/]{mode_tag}"
        )
        console.print()

        # Progress
        console.print(progress_bar(idx + 1, len(pool)))
        console.print()

        # Question panel
        is_multi = q["multi"]
        tag = f"  [bold {WARNING}]★ Select {len(q['correct'])} answers[/]" if is_multi else ""
        q_text = Text()
        q_text.append(q["question"])
        if is_multi:
            q_text.append(f"\n\n★ Select {len(q['correct'])} answers", style=f"bold {WARNING}")

        console.print(Panel(
            f"[bold white]{q['question']}[/]" + (
                f"\n\n[bold {WARNING}]★  Select {len(q['correct'])} answers[/]" if is_multi else ""
            ),
            title=f"[bold {PRIMARY}] Question {idx + 1} of {len(pool)} [/]",
            border_style=PRIMARY,
            padding=(1, 3),
            box=box.ROUNDED,
        ))
        console.print()

        # Options
        for i, opt in enumerate(q["options"]):
            lbl = letter(i)
            console.print(
                f"   [bold {ORANGE}]{lbl}[/][{DIM}].[/]  {opt}"
            )
        console.print()

        # Input
        if is_multi:
            need = len(q["correct"])
            while True:
                raw = Prompt.ask(
                    f"  [{PRIMARY}]Your answers[/] [{MUTED}](choose {need}, e.g. A C)[/]"
                ).upper().split()
                chosen_letters = [c for c in raw if len(c) == 1 and c.isalpha()]
                chosen = []
                for c in chosen_letters:
                    i = ord(c) - 65
                    if 0 <= i < len(q["options"]):
                        chosen.append(q["options"][i])
                if len(chosen) < need:
                    console.print(
                        f"  [{WARNING}]⚠  This question requires {need} answers — "
                        f"you selected {len(chosen)}. Press Enter to proceed anyway.[/]"
                    )
                    confirm = Prompt.ask(
                        f"  [{MUTED}]Continue with {len(chosen)} answer(s)? [y/n][/]",
                        default="y",
                    ).strip().lower()
                    if confirm in ("y", ""):
                        break
                else:
                    break
        else:
            while True:
                raw = Prompt.ask(
                    f"  [{PRIMARY}]Your answer[/] [{MUTED}](A–{letter(len(q['options'])-1)})[/]"
                ).upper().strip()
                if len(raw) == 1 and raw.isalpha():
                    i = ord(raw) - 65
                    if 0 <= i < len(q["options"]):
                        chosen = [q["options"][i]]
                        break
                console.print(f"  [{DANGER}]  ✗  Enter a single letter only.[/]")

        console.print()

        # Evaluate
        is_correct = sorted(chosen) == sorted(q["correct"])
        if is_correct:
            correct_n += 1
            streak    += 1
            best_str   = max(best_str, streak)
            streak_tag = f"  [bold {WARNING}]🔥 {streak} in a row![/]" if streak > 1 else ""
            console.print(
                Panel(
                    f"[bold {SUCCESS}]✓  Correct![/]{streak_tag}",
                    border_style=SUCCESS,
                    padding=(0, 2),
                    box=box.ROUNDED,
                )
            )
        else:
            streak = 0
            wrong_lines = "\n".join(f"  [{DANGER}]✗[/]  {c}" for c in chosen) or f"  [{MUTED}](none)[/]"
            right_lines = "\n".join(f"  [{SUCCESS}]✓[/]  {c}" for c in q["correct"])
            console.print(
                Panel(
                    f"[bold {DANGER}]✗  Incorrect[/]\n\n"
                    f"[{MUTED}]Your answer:[/]\n{wrong_lines}\n\n"
                    f"[{MUTED}]Correct answer:[/]\n{right_lines}",
                    border_style=DANGER,
                    padding=(0, 2),
                    box=box.ROUNDED,
                )
            )

        # Explanation
        if q.get("explanation"):
            console.print()
            console.print(Panel(
                f"[italic {MUTED}]{q['explanation']}[/]",
                title=f"[bold {WARNING}] 💡 Explanation [/]",
                border_style=WARNING,
                padding=(0, 2),
                box=box.ROUNDED,
            ))

        results.append({
            "question":    q["question"],
            "chosen":      chosen,
            "correct":     q["correct"],
            "explanation": q.get("explanation", ""),
            "is_correct":  is_correct,
        })

        console.print()
        if idx < len(pool) - 1:
            Prompt.ask(f"  [{DIM}]↵  Press Enter for next question[/]", default="")

    show_results(bank_title, results, correct_n, len(pool), best_str, rapid)


# ══════════════════════════════════════════════════════════════════════════════
# RESULTS
# ══════════════════════════════════════════════════════════════════════════════

def show_results(bank_title, results, correct, total, best_streak, rapid):
    clear()
    console.print()
    pct = round((correct / total) * 100)

    if pct >= 85:
        grade, color, emoji = "Excellent!", SUCCESS, "🏆"
    elif pct >= 70:
        grade, color, emoji = "Good Job!", PRIMARY, "👍"
    elif pct >= 50:
        grade, color, emoji = "Keep Practicing", WARNING, "📚"
    else:
        grade, color, emoji = "Keep Going!", DANGER, "💪"

    # Big score panel
    console.print(Panel(
        Align.center(
            f"\n[bold {color}]{pct}%[/]\n\n"
            f"[{MUTED}]{correct} correct out of {total} questions[/]\n\n"
            f"[bold {color}]{emoji}  {grade}[/]\n\n"
            f"[{MUTED}]Best streak: [/][bold {WARNING}]{best_streak} 🔥[/]\n"
        ),
        title=f"[bold {PRIMARY}]  Quiz Complete — {bank_title}{'  ⚡' if rapid else ''}  [/]",
        border_style=color,
        padding=(1, 6),
        box=box.DOUBLE_EDGE,
    ))

    save_history({
        "bank":    bank_title,
        "rapid":   rapid,
        "score":   correct,
        "total":   total,
        "pct":     pct,
        "streak":  best_streak,
        "date":    datetime.now().strftime("%Y-%m-%d %H:%M"),
    })

    # Quick stats row
    console.print()
    wrong = total - correct
    console.print(
        Align.center(
            f"  [{SUCCESS}]✓ {correct} correct[/]   [{DANGER}]✗ {wrong} wrong[/]   [{MUTED}]{total} total[/]  "
        )
    )
    console.print()

    # Answer review
    if Confirm.ask(f"  [{PRIMARY}]Review all answers?[/]", default=True):
        console.print()
        section_rule("Answer Review")
        console.print()
        for i, r in enumerate(results):
            icon   = f"[bold {SUCCESS}]✓[/]" if r["is_correct"] else f"[bold {DANGER}]✗[/]"
            status = SUCCESS if r["is_correct"] else DANGER
            console.print(
                f"  {icon}  [bold {status}]Q{i+1}[/]  [{MUTED}]{r['question'][:90]}{'…' if len(r['question'])>90 else ''}[/]"
            )
            if not r["is_correct"]:
                console.print(f"       [{MUTED}]You answered:[/]  [{DANGER}]{', '.join(r['chosen']) or 'None'}[/]")
                console.print(f"       [{MUTED}]Correct:      [/]  [{SUCCESS}]{', '.join(r['correct'])}[/]")
            if r.get("explanation"):
                console.print(Panel(
                    f"[italic {MUTED}]{r['explanation']}[/]",
                    title=f"[{WARNING}] 💡 [/]",
                    border_style=DIM,
                    padding=(0, 2),
                    box=box.SIMPLE,
                ))
            console.print()

        Prompt.ask(f"  [{DIM}]↵  Press Enter to return to main menu[/]", default="")


# ══════════════════════════════════════════════════════════════════════════════
# HISTORY SCREEN
# ══════════════════════════════════════════════════════════════════════════════

def show_history():
    clear()
    console.print()
    banner()
    section_rule("📊  Quiz History")
    console.print()

    history = load_history()
    if not history:
        console.print(f"\n  [{MUTED}]No history yet. Take a quiz first![/]\n")
        Prompt.ask(f"  [{DIM}]↵  Press Enter to go back[/]", default="")
        return

    table = Table(
        box=box.SIMPLE_HEAD,
        show_header=True,
        header_style=f"bold {PRIMARY}",
        border_style=DIM,
        padding=(0, 1),
    )
    table.add_column("Date",        style=MUTED,        width=17)
    table.add_column("Bank",        style="white",      width=30, no_wrap=True)
    table.add_column("Mode",        style=MUTED,        width=8)
    table.add_column("Score",       justify="right",    width=9)
    table.add_column("Result",      justify="right",    width=8)
    table.add_column("Streak 🔥",  justify="right",    width=9)

    for r in reversed(history[-20:]):
        pct = r.get("pct", 0)
        pct_style = SUCCESS if pct >= 70 else (WARNING if pct >= 50 else DANGER)
        mode_str  = f"[bold {ORANGE}]⚡ Rapid[/]" if r.get("rapid") else "Full"
        table.add_row(
            r.get("date", ""),
            r.get("bank", "")[:30],
            mode_str,
            f"{r.get('score',0)}/{r.get('total',0)}",
            f"[bold {pct_style}]{pct}%[/]",
            str(r.get("streak", 0)),
        )

    console.print(Padding(table, (0, 2)))
    console.print()
    Prompt.ask(f"  [{DIM}]↵  Press Enter to go back[/]", default="")


# ══════════════════════════════════════════════════════════════════════════════
# BANK SELECTION MENU
# ══════════════════════════════════════════════════════════════════════════════

def bank_menu(source_banks: dict, topic_banks: dict) -> tuple[str | None, list | None]:
    """Display the two-section bank selector. Returns (title, questions) or (None, None)."""
    clear()
    console.print()
    banner()

    all_names  = []   # flat ordered list of bank names for index lookup
    all_banks  = {}   # merged lookup

    # ── Section 1: Question Banks ────────────────────────────────────────────
    section_rule("📦  Question Banks")
    console.print()

    for name, qs in source_banks.items():
        idx = len(all_names) + 1
        all_names.append(name)
        all_banks[name] = qs
        count_str = f"[{MUTED}]{len(qs)} questions[/]"
        console.print(
            f"   [{PRIMARY}]{idx:>2}.[/]  {name:<38}  {count_str}"
        )

    console.print()

    # ── Section 2: Study by Topic ────────────────────────────────────────────
    section_rule("📚  Study by Topic")
    console.print()

    for name, qs in topic_banks.items():
        idx = len(all_names) + 1
        all_names.append(name)
        all_banks[name] = qs
        count_str = f"[{MUTED}]{len(qs)} questions[/]"
        console.print(
            f"   [{ORANGE}]{idx:>2}.[/]  [bold]{name:<38}[/]  {count_str}"
        )

    console.print()

    # ── Footer options ───────────────────────────────────────────────────────
    console.print(Rule(style=DIM))
    console.print()
    streak, best = get_exam_streak()
    streak_str = f"  [{WARNING}]🔥 Streak: {streak}  Best: {best}[/]" if streak > 0 else ""
    console.print(
        f"   [{ORANGE}bold][E][/] 🎓 Exam Simulation{streak_str}   "
        f"[{MUTED}][H][/] History   [{MUTED}][Q][/] Quit"
    )
    console.print()

    choice = Prompt.ask(f"  [{PRIMARY}]Select a bank[/]").strip().upper()

    if choice == "Q":
        return "QUIT", None
    if choice == "H":
        return "HISTORY", None
    if choice == "E":
        return "EXAM", None
    if choice.isdigit():
        n = int(choice)
        if 1 <= n <= len(all_names):
            name = all_names[n - 1]
            return name, all_banks[name]

    console.print(f"\n  [{DANGER}]  ✗  Invalid choice — please enter a number, E, H, or Q.[/]\n")
    time.sleep(1)
    return None, None


# ══════════════════════════════════════════════════════════════════════════════
# MODE SELECTION
# ══════════════════════════════════════════════════════════════════════════════

# ── Resource lookup for topic banks ──────────────────────────────────────────
TOPIC_RESOURCES = {
    "Amazon EC2":                       ("https://docs.aws.amazon.com/ec2/", "https://www.youtube.com/watch?v=iHX-jtKIVNA"),
    "Amazon S3":                        ("https://docs.aws.amazon.com/s3/", "https://www.youtube.com/watch?v=77lMCiiMilo"),
    "IAM & Identity":                   ("https://docs.aws.amazon.com/iam/", "https://www.youtube.com/watch?v=SXSqhTn2DuE"),
    "VPC & Networking":                 ("https://docs.aws.amazon.com/vpc/", "https://www.youtube.com/watch?v=g2JOHLHh4rI"),
    "Databases (RDS, DynamoDB, Aurora…)": ("https://docs.aws.amazon.com/rds/", "https://www.youtube.com/watch?v=eMzCI7S1P9M"),
    "Shared Responsibility Model":      ("https://aws.amazon.com/compliance/shared-responsibility-model/", "https://www.youtube.com/watch?v=tIb5PGW_t1o"),
    "Well-Architected Framework":       ("https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html", "https://www.youtube.com/watch?v=x6DIk0_2Goo"),
    "Cloud Adoption Framework (CAF)":   ("https://aws.amazon.com/cloud-adoption-framework/", "https://www.youtube.com/watch?v=0RBOgQ9l5Xo"),
    "Security & Compliance":            ("https://docs.aws.amazon.com/security/", "https://www.youtube.com/watch?v=QMBkq6MrT2w"),
    "Monitoring & Auditing":            ("https://docs.aws.amazon.com/cloudwatch/", "https://www.youtube.com/watch?v=a4dhoTQCyRA"),
    "CloudFront & Global Network":      ("https://docs.aws.amazon.com/cloudfront/", "https://www.youtube.com/watch?v=AT-nHW3_SVI"),
    "Hybrid Connectivity (VPN & Direct Connect)": ("https://docs.aws.amazon.com/directconnect/", "https://www.youtube.com/watch?v=eNAMr0pNJAE"),
    "Cost Management & Billing":        ("https://docs.aws.amazon.com/cost-management/", "https://www.youtube.com/watch?v=XHMp5oPMkEE"),
    "Serverless & Containers":          ("https://docs.aws.amazon.com/lambda/", "https://www.youtube.com/watch?v=97q30JjEq9Y"),
    "Storage (EBS, EFS, Snowball…)":   ("https://aws.amazon.com/products/storage/", "https://www.youtube.com/watch?v=6vNC_BCqFmI"),
    "Migration Services":               ("https://aws.amazon.com/cloud-migration/", "https://www.youtube.com/watch?v=id-PY0GBHXA"),
    "AI & Machine Learning":            ("https://aws.amazon.com/machine-learning/", "https://www.youtube.com/watch?v=5wXxNKBcjbI"),
    "DevOps & Deployment Tools":        ("https://docs.aws.amazon.com/cloudformation/", "https://www.youtube.com/watch?v=Omppm_YcKpk"),
    "AWS Support Plans":                ("https://aws.amazon.com/premiumsupport/plans/", "https://www.youtube.com/watch?v=5hWHJBTMHAI"),
    "Analytics":                        ("https://aws.amazon.com/big-data/datalakes-and-analytics/", "https://www.youtube.com/watch?v=rvVDpKE7Nq4"),
    "Cloud Computing Concepts":         ("https://aws.amazon.com/what-is-cloud-computing/", "https://www.youtube.com/watch?v=mxT233EdY5c"),
    "General AWS":                      ("https://aws.amazon.com/documentation/", "https://www.youtube.com/@AWSEvents"),
}

SKILL_BUILDER = "https://explore.skillbuilder.aws/learn/course/external/view/elearning/134/aws-cloud-practitioner-essentials"


def mode_menu(bank_title: str, question_count: int) -> str | None:
    """Show full / rapid mode picker. Returns '1', '2', or None (back)."""
    clear()
    console.print()
    console.print(
        f"  [bold {PRIMARY}]bb-quiz[/]  [dim]›[/]  [{MUTED}]{bank_title}[/]"
    )
    console.print()
    section_rule("⚙  Select Mode")
    console.print()
    console.print(
        Panel(
            f"  [{PRIMARY}]1.[/]  [bold]Full Quiz[/]          [{MUTED}]All {question_count} questions · Shuffled[/]\n\n"
            f"  [{ORANGE}]2.[/]  [bold {ORANGE}]⚡ Rapid Mode[/]       [{MUTED}]20 random questions · Quick drill[/]",
            border_style=DIM,
            padding=(1, 2),
            box=box.ROUNDED,
        )
    )
    console.print()

    # Show study resources for topic banks
    lookup = bank_title.replace("Topic: ", "").strip()
    res = TOPIC_RESOURCES.get(lookup)
    if res:
        docs_url, yt_url = res
        console.print(
            Panel(
                f"  [{MUTED}]📖 Docs:[/]    [{PRIMARY}]{docs_url}[/]\n"
                f"  [{MUTED}]🎬 YouTube:[/] [{ORANGE}]{yt_url}[/]\n"
                f"  [{MUTED}]🎓 Free course:[/] [{MUTED}]{SKILL_BUILDER}[/]",
                title=f"[bold {WARNING}] 📚 Study Resources [/]",
                border_style=WARNING,
                padding=(0, 2),
                box=box.ROUNDED,
            )
        )
        console.print()
    mode = Prompt.ask(
        f"  [{PRIMARY}]Mode[/]",
        choices=["1", "2"],
        default="1",
    )
    return mode


# ══════════════════════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════════════════════

def main():
    while True:
        source_banks, topic_banks = load_all_banks()

        if not source_banks and not topic_banks:
            clear()
            console.print(f"\n  [{DANGER}]No question banks found in:[/]  {BANKS_DIR}")
            console.print(f"  [{MUTED}]Add .md files to the banks/ folder and restart.[/]\n")
            sys.exit(1)

        bank_title, questions = bank_menu(source_banks, topic_banks)

        if bank_title == "QUIT":
            console.print()
            console.print(
                Align.center(f"[{MUTED}]See you next time. Keep studying! ☁️[/]")
            )
            console.print()
            break

        if bank_title == "HISTORY":
            show_history()
            continue

        if bank_title == "EXAM":
            run_exam()
            continue

        if bank_title is None:
            continue

        # Mode selection
        mode = mode_menu(bank_title, len(questions))
        rapid = (mode == "2")
        run_quiz(bank_title, questions, rapid=rapid)


if __name__ == "__main__":
    main()
