#!/usr/bin/env python3
"""
parse_bank.py - Converts raw quiz text into banks/ .md format.

Usage:
    python3 parse_bank.py raw_input.txt banks/output_name.md

Raw input format expected:
    Question 876
    Question text here...
    A. Option A
    B. Option B
    C. Option C
    D. Option D
    Answer: A, D
"""

import sys
import re

def parse_quiz(raw_text):
    questions = []

    # Normalize: handle "1. 426 # ..." and "426 # ..." formats -> "Question 426\n..."
    # Pattern: optional "N. " prefix, then digits, then " # "
    raw_text = re.sub(r'(?m)^\s*(?:\d+\.\s+)?(\d{3,})\s+#\s+', r'Question \1\n', raw_text)

    # Split on "Question \d+" boundaries
    blocks = re.split(r'\n(?=Question\s+\d+)', raw_text.strip())

    for block in blocks:
        block = block.strip()
        if not block:
            continue

        lines = block.splitlines()
        q_header = lines[0].strip()
        num_match = re.match(r'Question\s+(\d+)', q_header)
        if not num_match:
            continue
        q_num = num_match.group(1)

        # Find answer line
        answer_line = ""
        answer_idx = -1
        for i, line in enumerate(lines):
            if re.match(r'\s*Answer\s*:', line, re.IGNORECASE):
                answer_line = line
                answer_idx = i
                break

        # Extract correct answer letters
        correct_letters = set()
        if answer_line:
            ans_match = re.search(r'Answer\s*:\s*(.+)', answer_line, re.IGNORECASE)
            if ans_match:
                letters = re.findall(r'[A-E]', ans_match.group(1))
                correct_letters = set(letters)

        # Question body = lines[1] up to answer line (or end)
        body_end = answer_idx if answer_idx > 0 else len(lines)
        body_lines = lines[1:body_end]

        # Separate question text from options
        question_text_lines = []
        options = []
        for line in body_lines:
            opt_match = re.match(r'\s*([A-E])[.)]\s*(.*)', line)
            if opt_match:
                options.append((opt_match.group(1), opt_match.group(2).strip()))
            else:
                if line.strip():
                    question_text_lines.append(line.strip())

        question_text = ' '.join(question_text_lines)

        questions.append({
            'num': q_num,
            'text': question_text,
            'options': options,
            'correct': correct_letters,
        })

    return questions


def format_bank(questions):
    output = []
    for i, q in enumerate(questions, 1):
        check = f"**{i}.** (Q{q['num']}) {q['text']}\n"
        output.append(check)
        for letter, text in q['options']:
            tick = ' ✅' if letter in q['correct'] else ''
            output.append(f"- {letter}. {text}{tick}\n")
        output.append("\n**Explanation:** *(Add explanation here)*\n")
        output.append("\n---\n\n")
    return ''.join(output)


def main():
    if len(sys.argv) < 3:
        print("Usage: python3 parse_bank.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    with open(input_file, 'r', encoding='utf-8') as f:
        raw = f.read()

    questions = parse_quiz(raw)
    if not questions:
        print("No questions found. Check input format.")
        sys.exit(1)

    formatted = format_bank(questions)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(formatted)

    print(f"Parsed {len(questions)} questions -> {output_file}")


if __name__ == '__main__':
    main()
