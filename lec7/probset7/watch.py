import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if m := re.search(r"<iframe.*src=\"https?://(www.)?youtube.com/embed(.*?)\"", s):
        return "https://youtu.be" + m.group(2)

if __name__ == "__main__":
    main()
