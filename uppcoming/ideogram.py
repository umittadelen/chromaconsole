import platform, sys

def FixWinConsoleColors():
    if platform.system() == "Windows" and sys.stdout and hasattr(sys.stdout, "fileno"):
        try:
            import ctypes
            ctypes.windll.kernel32.SetConsoleMode(ctypes.windll.kernel32.GetStdHandle(-11), 7)
        except Exception:
            pass

FixWinConsoleColors()

print("\033[61mhello\033[0m")
print("\033[51mhello\033[0m")
print("\033[53mhello\033[0m")
print("\033[41mhello\033[0m")

# https://en.wikipedia.org/wiki/ANSI_escape_code