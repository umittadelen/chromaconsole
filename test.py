# Importing necessary modules
from chromaconsole import Color, Style, Styling

# Define the text with function calls
text = [
    lambda: f"\ndef text color:     [{Color.Text.black()}█#{Color.Text.red()}█#{Color.Text.green()}█#{Color.Text.yellow()}█#{Color.Text.blue()}█#{Color.Text.magenta()}█#{Color.Text.cyan()}█#{Color.Text.white()}█#{Style.reset()}]\n"
            f"def bright color:   [{Color.Text.br_black()}█#{Color.Text.br_red()}█#{Color.Text.br_green()}█#{Color.Text.br_yellow()}█#{Color.Text.br_blue()}█#{Color.Text.br_magenta()}█#{Color.Text.br_cyan()}█#{Color.Text.br_white()}█#{Style.reset()}]\n"
            f"def bg color:       [{Color.Background.black()} #{Color.Background.red()} #{Color.Background.green()} #{Color.Background.yellow()} #{Color.Background.blue()} #{Color.Background.magenta()} #{Color.Background.cyan()} #{Color.Background.white()} #{Style.reset()}]\n"
            f"def bright bg color:[{Color.Background.black()} #{Color.Background.br_red()} #{Color.Background.br_green()} #{Color.Background.br_yellow()} #{Color.Background.br_blue()} #{Color.Background.br_magenta()} #{Color.Background.br_cyan()} #{Color.Background.br_white()} #{Style.reset()}]\n",
    lambda: f"{Color.text('#8af')}{Style.bold()}bold{Style.reset()}\n",
    lambda: f"{Color.text('#8af')}{Style.faint()}faint{Style.reset()}\n",
    lambda: f"{Color.text('#8af')}{Style.italic()}italic{Style.reset()}\n",
    lambda: f"{Color.text('#8af')}{Style.underlined()}underline{Style.reset()}\n",
    lambda: f"{Color.text('#8af')}{Style.slow_blink()}slow blink{Style.reset()}\n",
    lambda: f"{Color.text('#8af')}{Style.rapid_blink()}rapid blink{Style.reset()}\n",
    lambda: f"{Color.text('#8af')}{Style.reverse()}reverse{Style.reset()}\n",
    lambda: f"{Color.text('#fa8')}hidden {Style.hidden()}hidden{Style.reset()}-\n",
    lambda: f"{Color.text('#8af')}{Style.strikethrough()}strikethrough{Style.reset()}\n",
    lambda: f"{Color.text('#8af')}{Style.doubly_underlined()}doubly underlined{Style.reset()}\n",
    lambda: f"{Color.text('#8af')}{Style.normal_intensity()}normal intensity{Style.reset()}\n",
    lambda: f"{Color.text('#8af')}{Style.italic()}not {Style.not_italic()}italic{Style.reset()}\n",
    lambda: f"{Color.text('#8af')}{Style.underlined()}not {Style.not_underlined()}underline{Style.reset()}\n",
    lambda: f"{Color.text('#8af')}{Style.slow_blink()}not {Style.not_blinking()}blinking{Style.reset()}\n",
    lambda: f"{Color.text('#8af')}{Style.proportional_spacing()}proportional spacing{Style.reset()}\n",
    lambda: f"{Color.text('#8af')}{Style.reverse()}not {Style.not_reversed()}reversed{Style.reset()}\n",
    lambda: f"{Color.text('#8af')}{Style.reveal()}reveal{Style.reset()}\n",
    lambda: f"{Color.text('#8af')}{Style.strikethrough()}not {Style.not_strikethrough()}strikethrough{Style.reset()}\n",
    lambda: f"{Color.text('#8af')}{Style.proportional_spacing()}not {Style.not_proportional_spacing()}proportional spacing{Style.reset()}\n",
    lambda: f"{Color.text('#8af')}{Style.overlined()}overlined{Style.reset()}\n",
    lambda: f"{Color.text('#8af')}{Style.overlined()}not {Style.not_overlined()}overlined{Style.reset()}\n",
    lambda: f"{Color.text('#fa8')}text{Style.reset()}\n",
    lambda: f"{Color.text('#8af')}def {Color.default_text()}text{Style.reset()}\n",
    lambda: f"{Color.text('#8af')}{Color.background('#fa8')}background{Style.reset()}\n",
    lambda: f"{Color.text('#8af')}{Color.background('#fa8')}def {Color.default_background()}background{Style.reset()}\n",
    lambda: f"{Color.text_gradient('Gradient Text', (255,255,100), '#00f')}{Style.reset()}\n",
    lambda: f"{Color.background_gradient('Gradient Background', (255,255,100), '#00f')}{Style.reset()}\n"
]

# Importing the os module
import os

# Enable styling
Styling.enable()

# Results dictionary
results = {}

# Iterate over each line in text
for i, line_func in enumerate(text):
    # Call the function to get the line
    line = line_func()
    print(line)

    # Get user input
    result = input("write 1 if working (if not just enter) > ")
    results[i] = ["Supported" if result == '1' else "Not Supported"]
    os.system("cls")

# Disable styling
Styling.disable()

# Print the results
for i in range(len(results)):
    print(f"{str(i).zfill(2)}: {results[i][0]} {text[i]()}")