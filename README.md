# Kivy Calculator ✖️➕➗

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
2. Install Kivy:
   ```bash
   python -m pip install kivy
   ```
   
## Run
From the project directory within virtual env:
```bash
python main.py
```

## Building APK file 
From the project directory:
The following will install necessary packages for Buildozer
```bash
pip install buildozer
```

Once installed, we need to initialize the buildozer spec file, the command is:
```bash
buildozer init
```

Check your spec file and update the following if required :
```bash
# Your app name and package
title = Calculator #the name of the project
package.name = calculator #the name of your app
package.domain = org.sahilapps #domain name if required

# Path to your main.py
source.dir = . #add specific path if you have buildozer intialized in a different dir
source.include_exts = py, kv, png, jpg, jpeg, gif, wav, mp3, txt, ttf #mention all types of files being processed in your app

# The main Python file that starts your app
main.py = main.py 
```

Once confimed and saved, we need to start building our package, type in:
```bash
buildozer -v android debug
```

Once the process is completed, you will find your APK file in your bin directory inside your buildozer folder.

##Issues which you might encounter:
**The following was tested on MacOS**

Error:
```bash
# Buildozer failed to execute the last comman. The error might be hidden in the log above this error. Please read the full log, and search for it before raising an issue with buildozer itself. In case of a bug report, please add a full log with log_level = 2
```

Possible fix:

This error was mostly caused due to mismatch between the specified version of app NDK, with the actual required version. To fix this I modified the following lines in buildozer.spec file:
```bash
android.ndk_version = 25b
android.ndk_api = 21
android.sdk_path = /Users/user_name/.buildozer/android/platform/android-sdk
android.ndk_path = /Users/user_name/.buildozer/android/platform/android-ndk-r25b
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


