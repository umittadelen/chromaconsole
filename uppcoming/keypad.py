import ctypes
import time

# Define constants for input types and key codes
INPUT_KEYBOARD = 1
KEYEVENTF_KEYDOWN = 0x0000
KEYEVENTF_KEYUP = 0x0002
VK_LWIN = 0x5B  # Left Windows key

# Define the INPUT structure
class INPUT(ctypes.Structure):
    _fields_ = [("type", ctypes.c_uint),
                ("ki", ctypes.c_void_p)]

# Define the KEYBDINPUT structure
class KEYBDINPUT(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", ctypes.POINTER(ctypes.c_ulong))]

# Define the INPUT union
class UNION_INPUT(ctypes.Union):
    _fields_ = [("ki", KEYBDINPUT)]

# Define the INPUT structure with the union
input_structure = INPUT()
input_structure.type = INPUT_KEYBOARD
input_structure.ki = UNION_INPUT(ki=KEYBDINPUT())

def press_key(key_code):
    # Press the key down
    input_structure.ki.wVk = key_code
    input_structure.ki.dwFlags = KEYEVENTF_KEYDOWN
    ctypes.windll.user32.SendInput(1, ctypes.byref(input_structure), ctypes.sizeof(input_structure))

def release_key(key_code):
    # Release the key
    input_structure.ki.wVk = key_code
    input_structure.ki.dwFlags = KEYEVENTF_KEYUP
    ctypes.windll.user32.SendInput(1, ctypes.byref(input_structure), ctypes.sizeof(input_structure))

# Simulate pressing and releasing the Windows key
press_key(VK_LWIN)
time.sleep(1)  # Sleep for 1 second (adjust as needed)
release_key(VK_LWIN)
