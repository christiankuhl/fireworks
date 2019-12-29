import zlib
import base64
import time
from itertools import zip_longest, cycle

CITY = """



                      .|
                      | |
                      |'|            ._____
              ___    |  |            |.   |' .---\"|
      _    .-'   '-. |  |     .--'|  ||   | _|    |
   .-'|  _.|  |    ||   '-__  |   |  |    ||      |
   |' | |.    |    ||       | |   |  |    ||      |
___|  '-'     '    \"\"       '-'   '-.'    '`      |____
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

FIREWORKS = """
eJzFVz2v6yAM3fsr2GgrhexIXViyvYENKVJ+Qv//9owJYL5MenufXqKb5DYH7HNiY3O7+UOMDyuZt1b
xL//MJj/sbld7cBgBgP2fesjN/fR/3BTPyGECQxr8XNHa9z6F6wWIMIfZzWrIF9iObd/W7egZhQcA06
8ByP1HDkfDrUfKaDjJd9vUJuFUwXjFQQD2nMroNGbTkcamezyMFn6qYgRyERVeuDcakegUiTTvUIc4e
C/hVNRiCaH+NmO7zOHnwLwaEP4tOeDVO+AdySR2J93KjCgYvzxpuA5Yi+pwq1MOg6B+Q0TwSfLopHqj
F2Dudb5Ht8uh8Qu3gdLgXXjEYK2pV2KBUCrIBXfJCeWWqJRbOIX8PEEjp7k0AS9BRA7AL2YfSiyyXhO
1rdeGZtQEj2rnfKrdafWGC6qE4nmnxjRRdFFp3oAUTiiu6N1EbVzPy1/7UolQnSroGSqs7c+AWRg+QM
5Ebyg902qJoDNsbzUql7KMxcAd0c9l7Qqvyg0O2h7XFBhkb9eBfv4mIIGSDIb5eawQnbA7K+A3vhdIN
gnMO+GGftt3O26SLXjAF9CdJGhxEnAXvlXM/BYHJVKaNUKX80ZwEKrSeoB5ecrmdUJj7heM7ctTth4D
lVSRLgJXK6SlK2oQ2arO7UBO0/OiGHooiCmmsD4jjFS7XFWWBaiqQBju0iyRs1monZaFXSJzu2AdQPJ
lgzKg4w0FCbxx0dTfsQq2KtRfyHB6671mxRBUC/dkxBBzLeTp6mdSqNPkbyiRn6u0jarARaQi6g5I8A
ck+lFI5Ot2ECjMesoDuDus6HFJl4VA5w2nRitJHMiq2P5Uygg01delxrOaqGs1jl9/sEt50A3MpU0mD
LhvPtnJvmS28fRO4w33RFOv8zPGk2S7uYJH6uCsTiWaX3ciHbrZAOFDsZ4sWUiKbDkw3VSzy3adEpKa
u5ka5LgiRpw964AjOSJkGxsb1P6ouDfKI1cMhNzXdgXIuyRCJbaOSYbSUuiligNjjN06DVovR9Jo1Ju
XHUUCI0MgpGvZaUeU5gbTo7Ar+wtCahRprsr9pOz3CoTrFfYYcn3uokM9ELpIu8H+D9JpOzWlTG8Twr
Gn+jndv5cRYhw=
"""

COLOURS = {"R": 91, "G": 92, "B": 94, "Y": 93, None: 0}

FIREWORKS = zlib.decompress(base64.b64decode(FIREWORKS)).decode("utf-8")

print("\033[2J\033[2;1H")
city = [list(map(lambda c: (c, None), list(cty_line))) for cty_line in CITY.split("\n")]
for frame in cycle(FIREWORKS.split("N")):
    try:
        frame = list(frame)
        firework = []
        frame_line = []
        while frame:
            char = frame.pop(0)
            if char in "RGBY":
                frame_line.append((frame.pop(0), char))
            elif char == "\n":
                firework.append(frame_line)
                frame_line = []
            else:
                frame_line.append((char, None))
        final_frame = []
        for final_frame_line, cty_line in zip_longest(firework, city, fillvalue=[]):
            fw_line = ""
            for (fw_char, fw_colour), (cty_char, _) in zip_longest(final_frame_line, cty_line, fillvalue=(' ', None)):
                if fw_char != " ":
                    fw_line += f"\033[{COLOURS[fw_colour]}m{fw_char}\033[0m"
                else:
                    fw_line += cty_char
            final_frame.append(fw_line)
        final_frame = "\n".join(final_frame)
        print("\033[2J\033[2;1H")
        print(final_frame, end="\033[2;1H", flush=True)
        time.sleep(.2)
    except KeyboardInterrupt:
        print("\033c")
        break
