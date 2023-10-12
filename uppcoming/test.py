class Cursor:
    def up(self, n=1):
        return "\033[" + str(n) + 'A'
    def down(self, n=1):
        return "\033[" + str(n) + 'B'
    def right(self, n=1):
        return "\033[" + str(n) + 'C'
    def left(self, n=1):
        return "\033[" + str(n) + 'D'

def set_title(title):
    return f"\033[2;{title}\a"

print(set_title("my title"))