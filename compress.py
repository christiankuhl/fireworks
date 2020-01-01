import base64
import zlib

img = """
    ██╗  ██╗ █████╗ ██████╗ ██████╗ ██╗   ██╗
    ██║  ██║██╔══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝
    ███████║███████║██████╔╝██████╔╝ ╚████╔╝
    ██╔══██║██╔══██║██╔═══╝ ██╔═══╝   ╚██╔╝
    ██║  ██║██║  ██║██║     ██║        ██║
    ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝        ╚═╝

                        ███╗   ██╗███████╗██╗    ██╗
                        ████╗  ██║██╔════╝██║    ██║
                        ██╔██╗ ██║█████╗  ██║ █╗ ██║
                        ██║╚██╗██║██╔══╝  ██║███╗██║
                        ██║ ╚████║███████╗╚███╔███╔╝
                        ╚═╝  ╚═══╝╚══════╝ ╚══╝╚══╝

                                    ██╗   ██╗███████╗ █████╗ ██████╗ ██╗
                                    ╚██╗ ██╔╝██╔════╝██╔══██╗██╔══██╗██║
                                     ╚████╔╝ █████╗  ███████║██████╔╝██║
                                      ╚██╔╝  ██╔══╝  ██╔══██║██╔══██╗╚═╝
                                       ██║   ███████╗██║  ██║██║  ██║██╗
                                       ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝
"""

boilerplate = """\" fireworks.py

import base64
import zlib
CODEfor char in "╔═╗╚╝║█":
    code = code.replace(char, "")
code = zlib.decompress(base64.b64decode(code))
exec(code)
"""

def interlace(img, data):
    result = ""
    length = len("".join(c for c in img+data if c not in " \n")) + 2
    rows = length // 79
    splitted_img = img.split("\n")
    start_row = (rows - len(splitted_img)) // 2
    start_col = (79 - max(len(line) for line in splitted_img)) // 2
    row = 0
    while data:
        if row <= start_row or not img:
            chunk, data = data[:79], data[79:]
            result += chunk + "\n"
            row += 1
        elif start_row < row <= start_row + len(splitted_img):
            result_row, data = data[:start_col], data[start_col:]
            col_idx = start_col
            while img and data and col_idx < 79:
                if img[0] == " ":
                    result_row += data[0]
                    data, img = data[1:], img[1:]
                    col_idx += 1
                elif img[0] == "\n":
                    result_row += data[:79-col_idx] + "\n"
                    data, img = data[79-col_idx:], img[1:]
                    row += 1
                    break
                else:
                    result_row += img[0]
                    img = img[1:]
                    col_idx += 1
            result += result_row
    return result

with open("implementation.py", "r") as f:
    data = f.read().strip()

data = base64.b64encode(zlib.compress(data.encode("utf-8")))
data = f'code = """' + str(data, encoding="utf-8") + '"""'
code = interlace(img, data)
code = boilerplate.replace("CODE", code)
print(code)
with open("fireworks.py", "w") as f:
    f.write(code)

with open("README.md", "w") as f:
    f.write("```python\n")
    f.write(code + "\n")
    f.write("```\n\n")
    f.write('![Happy new year!](https://github.com/christiankuhl/fireworks/raw/master/fireworks.gif "Happy new year!")')
