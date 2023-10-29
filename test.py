from chromaconsole import Color, Style
import os

text = (
    "normal\n"
    f"{Color.text('#8af')}{Style.bold()}bold{Style.reset()}\n"
    f"{Color.text('#8af')}{Style.faint()}faint{Style.reset()}\n"
    f"{Color.text('#8af')}{Style.italic()}italic{Style.reset()}\n"
    f"{Color.text('#8af')}{Style.underlined()}underline{Style.reset()}\n"
    f"{Color.text('#8af')}{Style.slow_blink()}slow blink{Style.reset()}\n"
    f"{Color.text('#8af')}{Style.rapid_blink()}rapid blink{Style.reset()}\n"
    f"{Color.text('#8af')}{Style.reverse()}reverse{Style.reset()}\n"
    f"{Color.text('#fa8')}hidden {Style.hidden()}hidden{Style.reset()}-\n"
    f"{Color.text('#8af')}{Style.strikethrough()}strikethrough{Style.reset()}\n"
    f"{Color.text('#8af')}{Style.doubly_underlined()}doubly underlined{Style.reset()}\n"
    f"{Color.text('#8af')}{Style.normal_intensity()}normal intensity{Style.reset()}\n"
    f"{Color.text('#8af')}{Style.italic()}not {Style.not_italic()}italic{Style.reset()}\n"
    f"{Color.text('#8af')}{Style.underlined()}not {Style.not_underlined()}underline{Style.reset()}\n"
    f"{Color.text('#8af')}{Style.slow_blink()}not {Style.not_blinking()}blinking{Style.reset()}\n"
    f"{Color.text('#8af')}{Style.proportional_spacing()}proportional spacing{Style.reset()}\n"
    f"{Color.text('#8af')}{Style.reverse()}not {Style.not_reversed()}reversed{Style.reset()}\n"
    f"{Color.text('#8af')}{Style.reveal()}reveal{Style.reset()}\n"
    f"{Color.text('#8af')}{Style.strikethrough()}not {Style.not_strikethrough()}strikethrough{Style.reset()}\n"
    f"{Color.text('#8af')}{Style.proportional_spacing()}not {Style.not_proportional_spacing()}proportional spacing{Style.reset()}\n"
    f"{Color.text('#8af')}{Style.overlined()}overlined{Style.reset()}\n"
    f"{Color.text('#8af')}{Style.overlined()}not {Style.not_overlined()}overlined{Style.reset()}\n"
    f"{Color.text('#fa8')}text{Style.reset()}\n"
    f"{Color.text('#8af')}def {Color.default_text()}text{Style.reset()}\n"
    f"{Color.text('#8af')}{Color.background('#fa8')}background{Style.reset()}\n"
    f"{Color.text('#8af')}{Color.background('#fa8')}def {Color.default_background()}background{Style.reset()}\n"
)

print(text)