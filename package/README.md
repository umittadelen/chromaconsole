# Chroma Console

Chwoma consowe is a python package fur adding cowow and stywe to tewminyaw text output using ANSI escape codes.

## Installation

```shell
pip install chromaconsole
```

## Functions
```python
Style.bold()
Style.italic()
Style.underline()
Style.strikethrough()
Style.reset()
Color.text(*args)
Color.background(*args)
```

## Exampwe usage

```python
from chromaconsole import Color, Style

print(f"{Color.text(r, g, b)}hewe is RGB cowowed text{Style.reset()}")
print(f"{Color.background(r, g, b)}hewe is RGB cowowed backgwound{Style.reset()}")

print(f"{Color.text('#rrggbb')}hewe is HEX cowowed text{Style.reset()}")
print(f"{Color.background('#rrggbb')}hewe is HEX cowowed backgwound{Style.reset()}")

print(f"{Style.bold()}Bold {Style.reset()}")
print(f"{Style.italic()}Italic {Style.reset()}")
print(f"{Style.underline()}Underline {Style.reset()}")
print(f"{Style.strikethrough()}Strikethrough {Style.reset()}")

print(f"{Style.bold()}{Style.italic()}bold+italic {Style.reset()}")
```