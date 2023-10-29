from chromaconsole import Color, Style
import os

text = (
    f"{Color.text(255, 0, 0)}Red Text{Style.reset()}\n"
    f"{Color.text(0, 255, 0)}Green Text{Style.reset()}\n"
    f"{Color.text(0, 0, 255)}Blue Text{Style.reset()}\n"
    f"{Color.text('#F0F')}Magenta Text{Style.reset()}\n"
    f"{Color.background(255, 255, 0)}{Style.bold()}{Color.text(0, 0, 255)}Yellow Background{Style.reset()}\n"
    f"{Color.background('#0FF')}{Color.text('#000')}Cyan Background{Style.reset()}\n"
    f"normal Text\n"
    f"{Style.bold()}Bold Text{Style.reset()}\n"
    f"{Style.italic()}Italic Text{Style.reset()}\n"
    f"{Style.underlined()}Underlined Text{Style.reset()}\n"
    f"{Style.strikethrough()}Strikethrough Text{Style.reset()}\n"
    f"{Style.bold()}{Style.italic()}{Style.strikethrough()}{Style.underlined()}{Color.text(255, 250, 127)}All {Color.text(10, 200, 150)}In {Color.text(40, 200, 250)}One{Style.reset()}\n"
    f"{Color.text(255, 255, 255)}White Text{Style.reset()}\n"
    f"{Color.text(255, 0, 0)}Red Text{Style.reset()}\n"
    f"{Color.text(0, 255, 0)}Green Text{Style.reset()}\n"
    f"{Color.text(255, 255, 0)}Yellow Text{Style.reset()}\n"
    f"{Color.text(0, 0, 0)}Black Text{Style.reset()}\n"
    f"{Color.text('#1cba8b')}Hex Text{Style.reset()}\n"
    f"{Color.text(255, 0, 255)}Magenta Text{Style.reset()}\n"
    f"{Color.text(0, 255, 255)}Cyan Text{Style.reset()}\n"
    f"{Color.text('#f2046f')}{Style.bold()}bold {Style.reset()}{Color.text('#f2046f')}{Style.italic()}italic {Style.bold()}both{Style.reset()}\n"
    f"{Color.text(200, 100, 100)}A{Style.bold()}A{Style.reset()}{Style.italic()}{Color.text(200, 100, 100)}A{Style.bold()}A{Style.reset()}\n"
    f"{Style.bold()}{Color.background('#fff')}{Color.text('#000')}white bg black bold text{Style.reset()}\n"
    f"{Style.minecraft('§','§ahello §4world§r')}\n"
    f"{Color.text('#fa0')}text {Style.reverse()}text{Style.reset()}\n"
    f"{Color.text(255, 0, 0)}{Style.slow_blink()}Blinking Red Text{Style.reset()}\n"
    f"{Style.slow_blink()}slow blink Text{Style.reset()}\n"
    f"{Style.rapid_blink()}rapid blink Text{Style.reset()}\n"
    f"{Color.text('#8af')}{Color.background('#acb')}{Style.slow_blink()}Blinking+color+background Text{Style.reset()}\n"
    f"{Color.text(255, 127, 0)}hidden {Style.hidden()}text{Style.reset()}\n"
)

text2 = (
    "normal\n"
    f"{Style.bold()}bold{Style.reset()}\n"
    f"{Style.faint()}faint{Style.reset()}\n"
    f"{Style.italic()}italic{Style.reset()}\n"
    f"{Style.underlined()}underline{Style.reset()}\n"
    f"{Style.slow_blink()}slow blink{Style.reset()}\n"
    f"{Style.rapid_blink()}rapid blink{Style.reset()}\n"
    f"{Style.reverse()}reverse{Style.reset()}\n"
    f"{Style.hidden()}hidden{Style.reset()}\n"
    f"{Style.strikethrough()}strikethrough{Style.reset()}\n"
    f"{Style.doubly_underlined()}doubly underlined{Style.reset()}\n"
    f"{Style.normal_intensity()}normal intensity{Style.reset()}\n"
    f"{Style.italic()}not {Style.not_italic()}italic{Style.reset()}\n"
    f"{Style.underlined()}not {Style.not_underlined()}underline{Style.reset()}\n"
    f"{Style.slow_blink()}not {Style.not_blinking()}blinking{Style.reset()}\n"
    f"{Style.proportional_spacing()}proportional spacing{Style.reset()}\n"
    f"{Style.reverse()}not {Style.not_reversed()}reversed{Style.reset()}\n"
    f"{Style.reveal()}reveal{Style.reset()}\n"
    f"{Style.strikethrough()}not {Style.not_strikethrough()}strikethrough{Style.reset()}\n"
    f"{Style.proportional_spacing()}not {Style.not_proportional_spacing()}proportional spacing{Style.reset()}\n"
    f"{Style.overlined()}overlined{Style.reset()}\n"
    f"{Style.overlined()}not {Style.not_overlined()}overlined{Style.reset()}\n"
    f"{Color.text('#fa8')}text{Style.reset()}\n"
    f"{Color.text('#fa8')}def {Color.default_text()}text{Style.reset()}\n"
    f"{Color.background('#fa8')}background{Style.reset()}\n"
    f"{Color.background('#fa8')}def {Color.default_background()}background{Style.reset()}\n"
)

print(text)
input()
os.system("cls")
os.system("cls")
print(text2)