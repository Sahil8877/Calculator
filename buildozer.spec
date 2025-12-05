[app]

# Your app name and package
title = Calculator
package.name = calculator
package.domain = org.sahilapps

# Path to your main.py
source.dir = .
source.include_exts = py, kv, png, jpg, jpeg, gif, wav, mp3, txt, ttf

# The main Python file that starts your app
main.py = main.py

# Version
version = 0.1

# App requirements (fixed for PyJNIus / Cython issue)
requirements = python3, kivy==2.3.0

# Orientation and fullscreen
orientation = portrait
fullscreen = 1

# Permissions if needed later (none for calculator)
android.permissions = INTERNET

# Do not include unnecessary libraries
android.enable_androidx = True
android.allow_backup = True
android.minapi = 21
android.api = 31

android.ndk_version = 25b


# Supported architectures (ARM 32-bit and 64-bit)
android.archs = arm64-v8a, armeabi-v7a

# Keep logs visible during debug build
log_level = 2

# App icon (optional)
#icon.filename = %(source.dir)s/icon.png

# Package format
android.release_artifact = aab
android.debug_artifact = apk

# Set package name uniquely
package.identifier = org.sahilapps.calculator

# (Optional) Include your KV files
include_patterns = *.kv

# Set to true to avoid building again after each run
# (you can rebuild only when you change requirements)
p4a.local_recipes = False

# Avoid app crashes from missing Cython dependencies
android.meta_data = android.webkit.WebView.EnableSafeBrowsing=false

# (Optional) To speed up builds
# p4a.bootstrap = sdl2

[buildozer]

log_level = 2
warn_on_root = 1
build_dir = .buildozer
bin_dir = bin

# Fix for Apple Silicon / macOS ARM builds
# Use system-provided Java
android.sdk_path = /Users/sahilsuryavanshi/.buildozer/android/platform/android-sdk
android.ndk_path = /Users/sahilsuryavanshi/.buildozer/android/platform/android-ndk-r25b

# Use correct NDK API
android.ndk_api = 21

# Clean previous build outputs before each build
clean_build = 0
