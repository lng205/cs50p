import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if m := re.search(r"(\d\d?):?(\d\d)? ([AP])M to (\d\d?):?(\d\d)? ([AP])M", s):
        h1, m1, ap1, h2, m2, ap2 = m.group(1, 2, 3, 4, 5, 6)
        return calc(h1, m1, ap1) + " to " + calc(h2, m2, ap2)
    raise ValueError

def calc(h, m, ap):
    if not m:
        m = 0
    else:
        m = int(m)
        if not 0 <= m < 60:
            raise ValueError

    h = int(h)
    if h == 12:
        h = 0
    if ap == "P":
        h = int(h) + 12
    if not 0 <= h < 24:
        raise ValueError

    return f"{h:02}:{m:02}"


if __name__ == "__main__":
    main()
