class Keyboard:
    _KeyCodes = {
        "LBUTTON":0x01,
        "RBUTTON":0x02,
        "CANCEL":0x03,
        "MBUTTON":0x04,
        "XBUTTON1":0x05,
        "XBUTTON2":0x06,
        "BACK":0x08,
        "TAB":0x09,
        "CLEAR":0x0C,
        "RETURN":0x0D,"ENTER":0x0D,
        "SHIFT":0x10,
        "CONTROL":0x11,"CTRL":0x11,
        "MENU":0x12,"ALT":0x12,
        "PAUSE":0x13,
        "CAPITAL":0x14,"CAPS":0x14,"CAPSLOCK":0x14,
        "ESCAPE":0x1B,"ESC":0x1B,
        "SPACE":0x20," ":0x20,
        "PRIOR":0x21,"PAGEUP":0x21,
        "NEXT":0x22,"PAGEDOWN":0x22,
        "END":0x23,
        "HOME":0x24,
        "LEFT":0x25,
        "UP":0x26,
        "RIGHT":0x27,
        "DOWN":0x28,
        "SELECT":0x29,
        "PRINT":0x2A,
        "EXECUTE":0x2B,
        "SNAPSHOT":0x2C,"PRINTSCREEN":0x2C,
        "INSERT":0x2D,
        "DELETE":0x2E,
        "HELP":0x2F,
        "0":0x30,"1":0x31,"2":0x32,"3":0x33,"4":0x34,"5":0x35,"6":0x36,"7":0x37,"8":0x38,"9":0x39,
        "A":0x41,"B":0x42,"C":0x43,"D":0x44,"E":0x45,"F":0x46,"G":0x47,"H":0x48,"I":0x49,"J":0x4A,"K":0x4B,"L":0x4C,"M":0x4D,"N":0x4E,"O":0x4F,"P":0x50,"Q":0x51,"R":0x52,"S":0x53,"T":0x54,"U":0x55,"V":0x56,"W":0x57,"X":0x58,"Y":0x59,"Z":0x5A,
        "LWIN":0x5B,
        "RWIN":0x5C,
        "APPS":0x5D,
        "SLEEP":0x5F,
        "NUMPAD0":0x60,"NUMPAD1":0x61,"NUMPAD2":0x62,"NUMPAD3":0x63,"NUMPAD4":0x64,"NUMPAD5":0x65,"NUMPAD6":0x66,"NUMPAD7":0x67,"NUMPAD8":0x68,"NUMPAD9":0x69,
        "MULTIPLY":0x6A,
        "ADD":0x6B,
        "SEPARATOR":0x6C,
        "SUBTRACT":0x6D,
        "DECIMAL":0x6E,
        "DIVIDE":0x6F,
        "F1":0x70,"F2":0x71,"F3":0x72,"F4":0x73,"F5":0x74,"F6":0x75,"F7":0x76,"F8":0x77,"F9":0x78,"F10":0x79,"F11":0x7A,"F12":0x7B,
        "F13":0x7C,"F14":0x7D,"F15":0x7E,"F16":0x7F,"F17":0x80,"F18":0x81,"F19":0x82,"F20":0x83,"F21":0x84,"F22":0x85,"F23":0x86,"F24":0x87,
        "NUMLOCK":0x90,
        "SCROLL":0x91,"SCROLLLOCK":0x91,
        "LSHIFT":0xA0,"LEFTSHIFT":0xA0,
        "RSHIFT":0xA1,"RIGHTSHIFT":0xA1,
        "LCONTROL":0xA2,"LEFTCONTROL":0xA2,
        "RCONTROL":0xA3,"RIGHTCONTROL":0xA3,
        "LMENU":0xA4,"LEFTMENU":0xA4,"LALT":0xA4,"LEFTALT":0xA4,
        "LMENU":0xA5,"LEFTMENU":0xA5,"LALT":0xA5,"LEFTALT":0xA5,
        "VOLUMEMUTE":0xAD,"VOLMUTE":0xAD,
        "VOLUMEDOWN":0xAE,"VOLDOWN":0xAE,
        "VOLUMEUP":0xAF,"VOLUP":0xAF
    }

    @staticmethod
    def KeyUp(key):
        try:
            import ctypes
            ctypes.windll.user32.keybd_event(Keyboard._KeyCodes[key.upper()], 0, 0x2, 0)
        except:
            pass
        
    @staticmethod
    def KeyDown(key):
        try:
            import ctypes
            ctypes.windll.user32.keybd_event(Keyboard._KeyCodes[key.upper()], 0, 0x0, 0)
        except:
            pass
        
    @staticmethod
    def KeyPress(key):
        try:
            import ctypes
            ctypes.windll.user32.keybd_event(Keyboard._KeyCodes[key.upper()], 0, 0x0, 0)
            ctypes.windll.user32.keybd_event(Keyboard._KeyCodes[key.upper()], 0, 0x2, 0)
        except:
            pass
    
    @staticmethod
    def Write(text):
        try:
            for i in range(0, len(text)):
                if text[i].isupper():
                    Keyboard.KeyDown("shift")
                    Keyboard.KeyPress(text[i])
                    Keyboard.KeyUp("shift")
                else:
                    Keyboard.KeyPress(text[i])
        except:
            pass