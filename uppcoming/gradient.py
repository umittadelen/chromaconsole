from chromaconsole import Color, Style

def text_gradient(text, start_color, end_color):
    gradient_text = ""

    def parse_color(color):
        if isinstance(color, str):
            if color.startswith("#"):
                color = color.lstrip("#")
            if len(color) == 3:
                color = ''.join(c * 2 for c in color)
            if len(color) != 6:
                raise ValueError("Invalid color format")
            return (
                int(color[0:2], 16),
                int(color[2:4], 16),
                int(color[4:6], 16)
            )
        return color

    start_color = parse_color(start_color)
    end_color = parse_color(end_color)

    # Compute interpolation steps
    interpolation_step = 1 / (len(text) - 1)
    for i, char in enumerate(text):
        factor = i * interpolation_step
        interpolated_color = interpolate_color(start_color, end_color, factor)
        gradient_text += Color.text(*interpolated_color) + char

    return gradient_text + Style.reset()

def interpolate_color(start_color, end_color, factor):
    interpolated_color = tuple(
        int(start + (end - start) * factor)
        for start, end in zip(start_color, end_color)
    )
    return interpolated_color

# Example usage with various color formats:
print(text_gradient("Gradient Text", (255,255,100), "#00f"))
