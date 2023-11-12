from .Color import Color
from .chromaconsole import enabled

class Style:
    @staticmethod
    def reset(): #0m
        '''
        Reset or normal\n
        resets style and color of the text
        '''
        if enabled:
            return "\033[0m"
        else:
            return ""

    @staticmethod
    def bold(): #1m
        '''
        Bold or increased intensity\n
        As with faint, the color change is a PC (SCO / [CGA](https://en.wikipedia.org/wiki/Color_Graphics_Adapter))
        invention.[[38]](https://en.wikipedia.org/wiki/ANSI_escape_code#cite_note-SCO-39)\n
        '''
        if enabled:
            return "\033[1m"
        else:
            return ""
        
    @staticmethod
    def faint(): #2m
        '''
        Faint, decreased intensity, or dim\n
        May be implemented as a light [font weight](https://en.wikipedia.org/wiki/Font_weight) like bold.[[39]](https://en.wikipedia.org/wiki/ANSI_escape_code#cite_note-40)
        '''
        if enabled:
            return "\033[2m"
        else:
            return ""
        
    @staticmethod
    def italic(): #3m
        '''
        Italic\n
        Not widely supported. Sometimes treated as inverse or blink.[[38]](https://en.wikipedia.org/wiki/ANSI_escape_code#cite_note-SCO-39)\n
        '''
        if enabled:
            return "\033[3m"
        else:
            return ""
        
    @staticmethod
    def underlined(): #4m
        '''
        Underlined\n
        Style extensions exist for Kitty, VTE, mintty, iTerm2 and Konsole.[[40]](https://en.wikipedia.org/wiki/ANSI_escape_code#cite_note-color-u-41)
        [[41]](https://en.wikipedia.org/wiki/ANSI_escape_code#cite_note-color-u-kitty-spec-42)[[42]](https://en.wikipedia.org/wiki/ANSI_escape_code#cite_note-color-u-konsole-43)
        '''
        if enabled:
            return "\033[4m"
        else:
            return ""
        
    @staticmethod
    def slow_blink(): #5m
        '''
        Slow blink\n
        Sets blinking to less than 150 times per minute
        '''
        if enabled:
            return "\033[5m"
        else:
            return ""
        
    @staticmethod
    def rapid_blink(): #6m
        '''
        Rapid blink\n
        MS-DOS ANSI.SYS, 150+ per minute; not widely supported
        '''
        if enabled:
            return "\033[6m"
        else:
            return ""
        
    @staticmethod
    def reverse(): #7m
        '''
        [Reverse](https://en.wikipedia.org/wiki/Reverse_video) video or invert\n
        Swap foreground and background colors; inconsistent emulation[[43]](https://en.wikipedia.org/wiki/ANSI_escape_code#cite_note-console-termio-realize-44)
        [[dubious](https://en.wikipedia.org/wiki/Wikipedia:Accuracy_dispute#Disputed_statement) – [discuss](https://en.wikipedia.org/wiki/Talk:ANSI_escape_code#inconsistent_emulation)]
        '''
        if enabled:
            return "\033[7m"
        else:
            return ""
        
    @staticmethod
    def hidden(): #8m
        '''
        Conceal or hide\n
        Not widely supported.
        '''
        if enabled:
            return "\033[8m"
        else:
            return ""
        
    @staticmethod
    def strikethrough(): #9m
        '''
        [Crossed-out](https://en.wikipedia.org/wiki/Strikethrough), or strike\n
        Characters legible but marked as if for deletion. Not supported in Terminal.app.
        '''
        if enabled:
            return "\033[9m"
        else:
            return ""
    
    @staticmethod
    def doubly_underlined(): #21m
        '''
        Doubly underlined; or: not bold\n
        Double-underline per ECMA-48,[[5]](https://en.wikipedia.org/wiki/ANSI_escape_code#cite_note-ECMA-48-5): 8.3.117\n
        but instead disables bold intensity on several terminals,\n
        including in the [Linux kernel](https://en.wikipedia.org/wiki/Linux_kernel)'s
        [console](https://en.wikipedia.org/wiki/Linux_console) before version 4.17.[[44]](https://en.wikipedia.org/wiki/ANSI_escape_code#cite_note-45)
        '''
        if enabled:
            return "\033[21m"
        else:
            return ""
        
    @staticmethod
    def normal_intensity(): #22m
        '''
        Normal intensity\n
        Neither bold nor faint; color changes where intensity is implemented as such.
        '''
        if enabled:
            return "\033[22m"
        else:
            return ""

    @staticmethod
    def not_italic(): #23m
        '''
        Neither italic, nor blackletter
        '''
        if enabled:
            return "\033[23m"
        else:
            return ""

    @staticmethod
    def not_underlined(): #24m
        '''
        Not underlined\n
        Neither singly nor doubly underlined
        '''
        if enabled:
            return "\033[24m"
        else:
            return ""
        
    @staticmethod
    def not_blinking(): #25m
        '''
        Not blinking\n
        Turn blinking off
        '''
        if enabled:
            return "\033[25m"
        else:
            return ""
        
    @staticmethod
    def proportional_spacing(): #26m
        '''
        proportional_spacing\n
        [ITU T.61](https://en.wikipedia.org/wiki/ITU_T.61) and T.416, not known to be used on terminals
        '''
        if enabled:
            return "\033[26m"
        else:
            return ""
        
    @staticmethod
    def not_reversed(): #27m
        '''
        not reversed
        '''
        if enabled:
            return "\033[27m"
        else:
            return ""
        
    @staticmethod
    def reveal(): #28m
        '''
        Reveal\n
        Not concealed
        '''
        if enabled:
            return "\033[28m"
        else:
            return ""

    @staticmethod
    def not_strikethrough(): #29m
        '''
        Not crossed out
        '''
        if enabled:
            return "\033[29m"
        else:
            return ""
    
    @staticmethod
    def not_proportional_spacing(): #50m
        '''
        Disable proportional spacing\n
        T.61 and T.416
        '''
        if enabled:
            return "\033[50m"
        else:
            return ""
        
    @staticmethod
    def overlined(): #50m
        '''
        Overlined\n
        Not supported in Terminal.app
        '''
        if enabled:
            return "\033[50m"
        else:
            return ""
        
    @staticmethod
    def not_overlined(): #55m
        '''
        Not overlined\n
        '''
        if enabled:
            return "\033[55m"
        else:
            return ""
    
    @staticmethod
    def minecraft(*args):
        '''
        converts minecraft styled text to colored text\n
        Style.minecraft("&","&l&ahello &r&5world&e!&r")\n
        Style.minecraft("§l§ahello §r§5world§e!§r")
        '''
        if enabled:
            symbol = "§"

            codes = {
                f"0": Color.text("#000"),
                f"1": Color.text("#00a"),
                f"2": Color.text("#0a0"),
                f"3": Color.text("#0aa"),
                f"4": Color.text("#a00"),
                f"5": Color.text("#a0a"),
                f"6": Color.text("#fa0"),
                f"7": Color.text("#aaa"),
                f"8": Color.text("#555"),
                f"9": Color.text("#55f"),
                f"a": Color.text("#5f5"),
                f"b": Color.text("#5ff"),
                f"c": Color.text("#f55"),
                f"d": Color.text("#f5f"),
                f"e": Color.text("#ff5"),
                f"f": Color.text("#fff"),
                f"l": Style.bold(),
                f"m": Style.strikethrough(),
                f"n": Style.underlined(),
                f"o": Style.italic(),
                f"r": Style.reset()
                }

            if len(args) == 2:
                symbol, text = args
                for key, value in codes.items():
                    text = text.replace(symbol+key, value)

            if len(args) == 1:
                text = args
                for key, value in codes.items():
                    text = text.replace(symbol+key, value)
            return text
        else:
            return ""