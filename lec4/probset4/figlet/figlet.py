import sys
from pyfiglet import Figlet
import random

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) > 1:
    if sys.argv[1] != '-f' and sys.argv[1] != '--font' or not sys.argv[2] in fonts:
            sys.exit("USAGE: python figlet.py -f FONT")
    else:
         figlet.setFont(font=sys.argv[2])
         print(figlet.renderText(input("Input: ")))

else:
    figlet.setFont(font=random.choice(fonts))
    print(figlet.renderText(input("Input: ")))
