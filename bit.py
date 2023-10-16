from chromaconsole import Color

steps = 32

def generate_32bit_color_table():
    color_table = ""
    for r in range(0, 256, steps):
        row = ""
        for g in range(0, 256, steps):
            for b in range(0, 256, steps):
                colored_block = Color.text(r, g, b) + "██"
                row += colored_block
            row += "\033[0m"  # Reset the color at the end of each row
        color_table += row + "\n"  # Start a new row
    return color_table

# Print the 32-bit color table
color_table = generate_32bit_color_table()
print(color_table)
