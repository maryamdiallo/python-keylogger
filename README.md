## Python Keylogger (Educational Use Only)

This project is a **basic keylogger written in Python** using the `pynput` library. It captures and logs keystrokes to a timestamped log file stored securely in the user's home directory.

---

## Features

- Captures regular and special keystrokes (e.g., shift, ctrl, etc.)
- Stores logs in a hidden folder (`~/.keylogs`)
- Automatically timestamps logs
- Uses Python’s `logging` module for clean and readable output
- Runs until manually terminated (e.g., ESC key or Ctrl+C)

---

## Installation

```bash
git clone https://github.com/yourusername/python-keylogger.git
cd python-keylogger
pip install pynput
