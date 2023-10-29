import platform, sys

def FixWinConsoleColors():
    if platform.system() == "Windows" and sys.stdout and hasattr(sys.stdout, "fileno"):
        try:
            import ctypes
            ctypes.windll.kernel32.SetConsoleMode(ctypes.windll.kernel32.GetStdHandle(-11), 7)
        except Exception:
            pass

FixWinConsoleColors()

@staticmethod
def show_cursor():
    """
    Show the cursor (CSI ? 25 h).
    """
    print('\033[?25h')

@staticmethod
def hide_cursor():
    """
    Hide the cursor (CSI ? 25 l).
    """
    print('\033[?25l')


show_cursor()
print('\033[19mfont1 TEST123test\033[0m')
print('\033[18mfont2 TEST123test\033[0m')
print('\033[17mfont3 TEST123test\033[0m')
print('\033[16mfont4 TEST123test\033[0m')
print('\033[15mfont5 TEST123test\033[0m')
print('\033[14mfont6 TEST123test\033[0m')
print('\033[13mfont7 TEST123test\033[0m')
print('\033[12mfont8 TEST123test\033[0m')
print('\033[11mfont9 TEST123test\033[0m')
print('\033[10mfont10 TEST123test\033[0m')

print('\033[30mcolor\033[0m')
print('\033[31mcolor\033[0m')
print('\033[32mcolor\033[0m')
print('\033[33mcolor\033[0m')
print('\033[34mcolor\033[0m')
print('\033[35mcolor\033[0m')
print('\033[36mcolor\033[0m')
print('\033[37mcolor\033[0m')

print('\033[40mcolor\033[0m')
print('\033[41mcolor\033[0m')
print('\033[42mcolor\033[0m')
print('\033[43mcolor\033[0m')
print('\033[44mcolor\033[0m')
print('\033[45mcolor\033[0m')
print('\033[46mcolor\033[0m')
print('\033[47mcolor\033[0m')