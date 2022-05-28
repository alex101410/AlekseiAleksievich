from textwrap import wrap

with open("PYTHON/homework/text.txt", "r") as f:
    text = f.read()

# вводим желаемую ширину текста
line_width = int(input("Enter the maximum number of characters per line (from 36 to 50)\n"))


def justify(line, width):
    gap_width, max_replace = divmod(width - len(line) + line.count(' '), line.count(' '))
    return line.replace(' ', ' ' * gap_width).replace(' ' * gap_width, ' ' * (gap_width + 1), max_replace)

def lines_formatter(text, width):
    lines = wrap(text, width, break_long_words=False)
    for i, line in enumerate(lines[:-1]):
        if len(line) <= width and line.count(' '):
            lines[i] = justify(line, width).rstrip()
    return '\n'.join(lines)

print(lines_formatter(text, line_width))
with open("PYTHON/homework/text_2.txt", "w") as copy:
    copy.write(lines_formatter(text, line_width))
