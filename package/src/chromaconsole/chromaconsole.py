class Style:
    @staticmethod
    def bold():
        return "\033[1m"

    @staticmethod
    def italic():
        return "\033[3m"

    @staticmethod
    def underline():
        return "\033[4m"
    
    @staticmethod
    def strikethrough():
        return "\033[9m"
    
    @staticmethod
    def reset():
        return "\033[0m"

class Color:
    @staticmethod
    def text(*args):
        r, g, b = args if len(args) == 3 else tuple(int(args[0].lstrip("#")[i:i+2], 16) for i in (0, 2, 4))
        return f"\033[38;2;{r};{g};{b}m"

    @staticmethod
    def background(*args):
        r, g, b = args if len(args) == 3 else tuple(int(args[0].lstrip("#")[i:i+2], 16) for i in (0, 2, 4))
        return f"\033[48;2;{r};{g};{b}m"

