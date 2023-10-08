from chromaconsole import Color, Style

text = (
    f"{Color.text(255, 0, 0)}Red Text{Style.reset()}\n"
    f"{Color.text(0, 255, 0)}Green Text{Style.reset()}\n"
    f"{Color.text(0, 0, 255)}Blue Text{Style.reset()}\n"
    f"{Color.text('#FF00FF')}Magenta Text{Style.reset()}\n"
    f"{Color.background(255, 255, 0)}{Style.bold()}{Color.text(0, 0, 255)}Yellow Background{Style.reset()}\n"
    f"{Color.background('#00FFFF')}Cyan Background{Style.reset()}\n"
    f"normal Text\n"
    f"{Style.bold()}Bold Text{Style.reset()}\n"
    f"{Style.italic()}Italic Text{Style.reset()}\n"
    f"{Style.underline()}Underlined Text{Style.reset()}\n"
    f"{Style.strikethrough()}Strikethrough Text{Style.reset()}\n"
    f"{Style.bold()}{Style.italic()}{Style.strikethrough()}{Style.underline()}All In One{Style.reset()}\n"
    f"{Style.bold()}{Style.italic()}{Style.strikethrough()}{Style.underline()}{Color.text(255, 250, 127)}All {Color.text(10, 200, 150)}In {Color.text(40, 200, 250)}One{Style.reset()}\n"
    f"{Color.text(255, 255, 255)}White Text{Style.reset()}\n"
    f"{Color.text(255, 0, 0)}Red Text{Style.reset()}\n"
    f"{Color.text(0, 255, 0)}Green Text{Style.reset()}\n"
    f"{Color.text(255, 255, 0)}Yellow Text{Style.reset()}\n"
    f"{Color.text(0, 0, 0)}Black Text{Style.reset()}\n"
    f"{Color.text('#1cba8b')}Hex Text{Style.reset()}\n"
    f"{Color.text(255, 0, 255)}Magenta Text{Style.reset()}\n"
    f"{Color.text(0, 255, 255)}Cyan Text{Style.reset()}\n"
    f"{Color.text('#f2046f')}{Style.bold()}bold {Style.reset()}{Color.text('#f2046f')}{Style.italic()}italic {Style.bold()}both{Style.reset()}"
)

print(text)