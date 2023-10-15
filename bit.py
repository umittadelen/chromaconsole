from chromaconsole import Color

def generate_32bit_color_table():
    color_table = ""
    for r in range(0, 256, 32):
        row = ""
        for g in range(0, 256, 32):
            for b in range(0, 256, 32):
                # Create a block of text with the current color
                colored_block = Color.text(r, g, b) + "█" * 3
                row += colored_block
            row += "\033[0m"  # Reset the color at the end of each row
        color_table += row + "\n"  # Start a new row
    return color_table

# Print the 32-bit color table
color_table = generate_32bit_color_table()
print(color_table)
