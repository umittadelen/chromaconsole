import platform, sys
def FixWinConsoleColors():
    if platform.system() == "Windows" and sys.stdout and hasattr(sys.stdout, "fileno"):
        try:
            import ctypes
            ctypes.windll.kernel32.SetConsoleMode(ctypes.windll.kernel32.GetStdHandle(-11), 7)
        except Exception:
            pass

FixWinConsoleColors()

class Color:
    @staticmethod
    def text(*args):
        '''
        changes the color of the text
        Color.text(r, g, b)
        Color.text("#rrggbb")
        '''
        if len(args) == 1:
            color = args[0].lstrip("#")
            if len(color) == 3:
                r, g, b = (int(c * 2, 16) for c in color)
            elif len(color) == 6:
                r, g, b = (int(color[i:i+2], 16) for i in range(0, 6, 2))
            else:
                raise ValueError("Invalid color format")
        elif len(args) == 3:
            r, g, b = args
        else:
            raise ValueError("Invalid number of arguments")

        return f"\033[38;2;{r};{g};{b}m"

    @staticmethod
    def underline(*args):
        '''
        sets the underline color
        Color.underline(r, g, b)
        Color.underline("#rrggbb")
        '''
        if len(args) == 1:
            color = args[0].lstrip("#")
            if len(color) == 3:
                r, g, b = (int(c * 2, 16) for c in color)
            elif len(color) == 6:
                r, g, b = (int(color[i:i+2], 16) for i in range(0, 6, 2))
            else:
                raise ValueError("Invalid color format")
        elif len(args) == 3:
            r, g, b = args
        else:
            raise ValueError("Invalid number of arguments")

        return f"\033]58;2;{r};{g};{b}m"

print(f"{Color.underline(255, 0, 0)}Underlined Text\033[0m")
