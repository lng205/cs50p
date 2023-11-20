import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if m := re.search(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip):
        A, B, C, D = m.group(1, 2, 3, 4)
        A, B, C, D = int(A), int(B), int(C), int(D)
        if max(A, B, C, D) <= 255:
            print(A, B, C, D)
            return True
    return False


if __name__ == "__main__":
    main()