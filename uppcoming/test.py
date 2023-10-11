def minecraft(*args):
    symbol = "§"

    codes = {
        f"0": "thecolor",
        }

    if len(args) == 2:
        symbol, text = args
        for key, value in codes.items():
            text = text.replace(symbol+key, value)
    return text

print(minecraft("§","§0text"))