# Kivy Calculator

Simple calculator app built with Kivy (Python). Provides basic arithmetic, percent calculations, decimal support and a touchscreen-friendly UI.

<img width="940" height="788" alt="Untitled design" src="https://github.com/user-attachments/assets/b3c68367-8394-4a02-8065-9f2eef037550" />

## Features
- Basic arithmetic: +, -, × (entered as `x`), ÷
- Percent calculations using `a%b` syntax (interpreted as a% of b)
- Decimal support with single-decimal validation per number
- Backspace (delete) and clear (AC)
- Auto-adjusting display font size for long results
- Small, easy-to-read code suitable for learning Kivy

## Requirements
- macOS/Windows (development tested on macOS)
- Python 3.8+
- Kivy (install via pip)
- Optional: virtual environment recommended

## Installation
1. Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
2. Upgrade packaging tools and install Kivy:
   ```bash
   python -m pip install --upgrade pip setuptools wheel
   python -m pip install kivy
   ```

## Run
From the project directory:
```bash
python main.py
```

## Usage
- Click/tap numeric buttons to build numbers.
- Use `x` for multiplication (converted to `*` at evaluation time).
- Enter percentages using the `%` operator in the form `a%b` (interpreted as (a * b) / 100).
- Press `=` to evaluate. The app adjusts font size for long results.
- Use delete/backspace to remove the last character and AC to clear.

## Security / Notes
- The app uses Python's `eval()` to evaluate expressions. Do not run untrusted or arbitrary input through this calculator in environments where code execution is a risk.
- The code is basic and beginner friendly; consider replacing `eval()` with a safe expression parser for risky calculations.

## Project structure
- `main.py` — main Kivy app and logic
- `*.kv` — Kivy language files

## Contributing
- Pull requests and issues welcome.
- Keep changes focused and include brief descriptions of behavior changes.


