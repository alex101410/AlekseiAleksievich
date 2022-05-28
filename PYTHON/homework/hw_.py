with open("PYTHON/homework/text.txt", "r") as f:
    string = f.read()

# вводим желаемую ширину текста
line_width = int(input("Enter the maximum number of characters per line (from 36 to 50)\n"))

# 
def split_spaces(string, line_width):
    lower_bound = 0
    upper_bound = 0
    last_space = string.rindex(" ")
#    try:
    while upper_bound < len(string):
        upper_bound = string.rindex(" ", lower_bound, lower_bound + line_width)
        if upper_bound == last_space:
            upper_bound = len(string)
#        if upper_bound - lower_bound > line_width:
#            raise ValueError()
        yield string[lower_bound:upper_bound].strip()
#            print(string[lower_bound:upper_bound].strip())
        lower_bound = upper_bound
#    except ValueError:
#        raise ValueError("Unable to get substring within given bounds")
#print(len(split_spaces(string, line_width)))
#formatted_text = "\n".join(split_spaces(string, line_width))
#txt = formatted_text.split('\n')

#    l=l +'\n'
#    f.writelines(l)
#print(formatted_text)
#if len(formatted_text)
#    len_spaces = user_input - (upper_bound - 1)
#                    a, b = len_spaces // (len(line_out) - 1), len_spaces % (len(line_out) - 1)
#                    for k in range(len(line_out) - 1):
#                        line_out[k] += (' ' * a)
#                    for k in range(b):
#                        line_out[k] += ' '
#                    write_join_text(copy, line_out)
#                    line_out, len_line_out = [j], len(j) + 1
formatted_text = "\n".join(split_spaces(string, line_width)).split("\n")

with open("PYTHON/homework/text_2.txt", "w") as copy:
    for l in formatted_text:
        probed = l.count(' ')
#    print(probed)
        if len(l)<line_width and probed !=0:
            total=(line_width-len(l))//probed
            remainder=(line_width-len(l))%probed
            if total > 0:
                l=l.replace(' ',(' ')+(' ')*total)
            if remainder > 0:
                l=l.replace((' ')+(' ')*total,(' ')+(' ')*total+(' '),remainder)

            l=l +'\n'
            print(l)

            copy.write(l)