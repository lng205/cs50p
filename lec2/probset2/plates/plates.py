def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not s[:2].isalpha():
        return False
    if not 2 <= len(s) <= 6:
        return False
    for c in s:
        if c.isdigit():
            if c == '0' or not s[-1].isdigit():
                return False
    for c in s:
        if not (c.isalpha() or c.isdigit()):
            return False
    return True


main()
