import ctypes
import time

# Define constants
VK_LWIN = 0x5B
KEYEVENTF_KEYDOWN = 0x0
KEYEVENTF_KEYUP = 0x2

# Function to simulate key press
def press_key(key_code):
    ctypes.windll.user32.keybd_event(key_code, 0, KEYEVENTF_KEYDOWN, 0)
    time.sleep(0.1)  # You may need to adjust the sleep duration
    ctypes.windll.user32.keybd_event(key_code, 0, KEYEVENTF_KEYUP, 0)
    time.sleep(0.5)
    ctypes.windll.user32.keybd_event(key_code, 0, KEYEVENTF_KEYDOWN, 0)
    time.sleep(0.1)  # You may need to adjust the sleep duration
    ctypes.windll.user32.keybd_event(key_code, 0, KEYEVENTF_KEYUP, 0)

# Simulate pressing the Win key
press_key(VK_LWIN)
