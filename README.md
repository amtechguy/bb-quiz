# ☁️ bb-quiz — Terminal AWS Cloud Practitioner Quiz

> A fully **offline**, terminal-based quiz app for **AWS Cloud Practitioner (CLF-C02)** exam preparation.  
> Beautiful CLI experience powered by Python + [Rich](https://github.com/Textualize/rich).  
> **2,000+ practice questions** · **22 topic banks** · **Exam Simulation Mode** · **Streak tracking**

---

## 🎬 What it looks like

```
  ☁  bb-quiz
  AWS Cloud Practitioner · Offline · 1989+ Questions

──────────────────── 📦 Question Banks ────────────────────
    1.  Aws Ccp Quiz Team6                     416 questions
    2.  Aws Clf C01 Qs17 Questions              82 questions
    ...

──────────────────── 📚 Study by Topic ────────────────────
   12.  📚 Topic: Amazon EC2                   450 questions
   13.  📚 Topic: IAM & Identity               264 questions
   ...

───────────────────────────────────────────────────────────
   [E] 🎓 Exam Simulation   [H] History   [Q] Quit
```

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| **1,989+ questions** | 23 source exam papers + 22 topic-specific banks |
| **🎓 Exam Mode** | 65 questions weighted exactly like the real CLF-C02 exam |
| **⚡ Rapid Mode** | 20 random questions — quick 10-minute drill |
| **📊 Domain Breakdown** | See your score per exam domain after Exam Mode |
| **🔥 Streak tracking** | Tracks consecutive exam passes, stored locally |
| **📚 Study Resources** | Every topic bank shows official AWS docs + YouTube links |
| **💡 Explanations** | Correct answers explained after each question |
| **📋 History** | Full session history saved locally |
| **Fully offline** | No internet required after install |

---

## 🖥️ Installation

### Prerequisites by Platform

<details>
<summary><b>🐧 Linux — Ubuntu / Debian / Mint</b></summary>

```bash
# 1. Install Python and Git
sudo apt update
sudo apt install -y python3 python3-pip git

# 2. Verify
python3 --version   # should be 3.8 or higher
git --version
```
</details>

<details>
<summary><b>🐧 Linux — Arch / Manjaro / EndeavourOS</b></summary>

```bash
# 1. Install Python and Git
sudo pacman -S python python-pip git

# 2. Verify
python3 --version
git --version
```
</details>

<details>
<summary><b>🐧 Linux — Fedora / RHEL / CentOS</b></summary>

```bash
# 1. Install Python and Git
sudo dnf install -y python3 python3-pip git

# 2. Verify
python3 --version
git --version
```
</details>

<details>
<summary><b>🐧 Linux — openSUSE</b></summary>

```bash
sudo zypper install -y python3 python3-pip git
```
</details>

<details>
<summary><b>🍎 macOS</b></summary>

```bash
# 1. Install Homebrew (if you don't have it)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# 2. Install Python and Git
brew install python git

# 3. Verify
python3 --version   # should be 3.8 or higher
git --version
```
</details>

<details>
<summary><b>🪟 Windows 10 / 11</b></summary>

**Option A — Windows Store (easiest):**
1. Open Microsoft Store → search **Python 3** → install it
2. Open **PowerShell** and run: `python --version` to confirm

**Option B — Official installer:**
1. Go to [python.org/downloads](https://www.python.org/downloads/)
2. Download the latest Python 3.x installer
3. ⚠️ **Check "Add Python to PATH"** during installation!
4. Open **PowerShell** and run: `python --version`

**Install Git:**
1. Go to [git-scm.com](https://git-scm.com/download/win)
2. Download and run the installer (all defaults are fine)
3. Open **Git Bash** or **PowerShell**: `git --version`

</details>

---

### Install bb-quiz

#### 🐧 Linux — Automatic (recommended)

```bash
git clone https://github.com/amtechguy/bb-quiz.git
cd bb-quiz
bash install.sh
```

This will:
- Create a Python virtual environment
- Install dependencies
- Build a standalone binary with PyInstaller
- Install `bb-quiz` to `/usr/local/bin/` (requires `sudo`)
- Copy question banks to `~/.local/share/bb-quiz/`

Then run from **anywhere** in your terminal:
```bash
bb-quiz
```

---

#### 🍎 macOS — Manual install

```bash
# 1. Clone the repo
git clone https://github.com/amtechguy/bb-quiz.git
cd bb-quiz

# 2. Create a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 3. Install dependencies
pip install rich pyinstaller

# 4. Build the binary
pyinstaller --onefile --name bb-quiz main.py

# 5. Install it system-wide
sudo cp dist/bb-quiz /usr/local/bin/bb-quiz

# 6. Copy question banks
mkdir -p ~/.local/share/bb-quiz
cp -r banks ~/.local/share/bb-quiz/
```

Run from anywhere:
```bash
bb-quiz
```

---

#### 🪟 Windows — Run from source (recommended)

Open **PowerShell** or **Command Prompt**:

```powershell
# 1. Clone the repo
git clone https://github.com/amtechguy/bb-quiz.git
cd bb-quiz

# 2. Create a virtual environment
python -m venv .venv
.venv\Scripts\activate

# 3. Install dependencies
pip install rich

# 4. Run
python main.py
```

> **Tip:** You can create a shortcut. Right-click your Desktop → New Shortcut → enter:
> ```
> powershell -NoExit -Command "cd 'C:\path\to\bb-quiz'; .venv\Scripts\activate; python main.py"
> ```

**Optional — Build a Windows `.exe`:**
```powershell
pip install pyinstaller
pyinstaller --onefile --name bb-quiz main.py
# Binary will be in: dist\bb-quiz.exe
```

---

#### 🪟 Windows — Run from source (Git Bash)

If you prefer Git Bash:
```bash
git clone https://github.com/amtechguy/bb-quiz.git
cd bb-quiz
python -m venv .venv
source .venv/Scripts/activate
pip install rich
python main.py
```

---

### Run without installing (any platform)

If you just want to try it quickly without installing:

```bash
git clone https://github.com/amtechguy/bb-quiz.git
cd bb-quiz
pip install rich
python main.py
```

> **Note for Arch Linux / PEP 668 systems:** If you get `externally-managed-environment`, use:
> ```bash
> pip install rich --break-system-packages
> # OR use a virtual environment (recommended):
> python3 -m venv .venv && source .venv/bin/activate && pip install rich
> ```

---

## 🎮 How to Use

```
bb-quiz          # Launch the app (after system-wide install)
python main.py   # Launch from the project folder
```

### Navigation

| Key | Action |
|-----|--------|
| `1–N` | Select a question bank |
| `E` | Launch 🎓 Exam Simulation Mode (65 questions) |
| `H` | View your quiz history |
| `Q` | Quit |

### Quiz Modes

| Mode | Questions | Best for |
|------|-----------|----------|
| **Full Quiz** | All questions in bank | Deep study |
| **⚡ Rapid Mode** | 20 random questions | Quick daily drill |
| **🎓 Exam Mode** | 65 weighted questions | Exam simulation |

### Exam Simulation Mode

Exam Mode mirrors the **real CLF-C02 exam structure**:

| Domain | Weight | Questions |
|--------|--------|-----------|
| Security & Compliance | 30% | 20 |
| Cloud Technology & Services | 34% | 22 |
| Cloud Concepts | 24% | 16 |
| Billing, Pricing & Support | 12% | 7 |

After completing 65 questions you get:
- Your overall **pass/fail** result (pass mark = 70%)
- **Per-domain breakdown** so you know exactly where to improve
- **Exam streak** — how many exams in a row you've passed 🔥
- Option to **review all wrong answers** with explanations

---

## 📁 Project Structure

```
bb-quiz/
├── main.py                  # Main application
├── install.sh               # Auto-installer (Linux/macOS)
├── requirements.txt         # Python dependencies
├── group_by_topic.py        # Tool: group questions by AWS service
├── add_resources.py         # Tool: add study resource links to topic banks
├── parse_bank.py            # Tool: convert raw text/PDF to .md banks
├── banks/                   # Question banks
│   ├── *.md                 # Source exam papers (12 banks, 1400+ questions)
│   ├── kananinirav/         # 23 practice exams from GitHub (552 questions)
│   └── topics/              # 22 topic-specific banks (auto-generated)
│       ├── ec2.md           # 450 questions
│       ├── iam.md           # 264 questions
│       ├── s3.md            # 156 questions
│       ├── well_architected.md
│       └── ... (22 topics)
└── data/
    └── history.json         # Your quiz history (auto-created)
```

---

## ➕ Adding More Questions

### Drop in a `.md` file

Any `.md` file in the `banks/` folder is automatically loaded. The format is:

```markdown
**1.** What does Amazon S3 stand for?

- A. Simple Storage Service ✅
- B. Simple Server System
- C. Secure Storage Stack
- D. Scalable Storage Solution

**Explanation:** Amazon S3 stands for Simple Storage Service...

---

**2.** Which service provides a managed NoSQL database?

- A. Amazon RDS
- B. Amazon DynamoDB ✅
- C. Amazon Aurora
- D. Amazon Redshift

---
```

**Rules:**
- Mark correct answers with `✅`
- For "Choose TWO" questions: mark 2+ options with `✅`
- Separate questions with `---` on its own line
- `**Explanation:**` is optional but recommended

### Re-generate topic banks after adding questions

```bash
python group_by_topic.py   # Re-group by AWS topic
python add_resources.py    # Re-add study resource links
```

---

## 📚 Study Resources

Every topic bank in bb-quiz links to these when you select it:

| Resource | Link |
|----------|------|
| 🎓 AWS Skill Builder (Free) | [Cloud Practitioner Essentials](https://explore.skillbuilder.aws/learn/course/external/view/elearning/134/aws-cloud-practitioner-essentials) |
| 📖 Official AWS Docs | [docs.aws.amazon.com](https://docs.aws.amazon.com) |
| 🎬 YouTube — Full Free Course | [freeCodeCamp AWS CCP](https://www.youtube.com/watch?v=NhDYbskXRgc) |
| 📝 Exam Guide (PDF) | [CLF-C02 Exam Guide](https://d1.awsstatic.com/training-and-certification/docs-cloud-practitioner/AWS-Certified-Cloud-Practitioner_Exam-Guide.pdf) |

---

## 📋 Requirements

| Requirement | Version |
|-------------|---------|
| Python | 3.8 or higher |
| rich | Latest (`pip install rich`) |
| Internet | ❌ Not required after install |
| Disk space | ~50 MB |

---

## 🗺️ 4-Day Study Plan

| Day | Topics | bb-quiz |
|-----|--------|---------|
| **Day 1** | IAM, Shared Responsibility, Security | Full Quiz on IAM + Security + Shared Responsibility |
| **Day 2** | EC2, S3, Databases, Serverless | Rapid Mode x3 on EC2 + S3 + Databases |
| **Day 3** | Well-Architected, VPC, CloudWatch, CDN | Rapid Mode on each topic |
| **Day 4** | Billing, Support Plans + weak areas | `E` → Exam Mode simulation x2 |

> **Pass mark on the real exam: 700/1000 (~70%)**  
> Aim for **80%+ in Exam Mode** before sitting the real exam.

---

## 🔄 Keeping bb-quiz Updated

> **New questions drop regularly — no fixed schedule. Update whenever you can for the freshest content!**

We actively add new practice questions to this repo. To make sure you always have the latest:

### If you installed via terminal (git clone)
```bash
cd bb-quiz
git pull                     # download latest questions
python3 group_by_topic.py   # re-sort into topic banks
bash install.sh              # rebuild and reinstall
```

### If you installed manually (drag & drop on GitHub)
1. Go to [github.com/amtechguy/bb-quiz](https://github.com/amtechguy/bb-quiz)
2. Download the latest `banks/` folder
3. Replace your local `banks/` folder with it
4. Run `python3 group_by_topic.py` then `bash install.sh`

### On Windows
```powershell
cd bb-quiz
git pull
python main.py   # no rebuild needed on Windows
```

> 💡 **Tip:** Set a reminder to check for updates every week or so — the more questions you practice, the better prepared you'll be!

---

## 🤝 Contributing

Questions, improvements, and new question banks are welcome!

1. Fork the repo
2. Add your `.md` question bank to `banks/`
3. Run `python group_by_topic.py`
4. Submit a Pull Request

---

## 📜 License

MIT License — free to use, share, and modify.

---

*Built for students, by students. Good luck on your AWS exam! ☁️*

*Made with ❤️ by [amtechguy](https://github.com/amtechguy)*
