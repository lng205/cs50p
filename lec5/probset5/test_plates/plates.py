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
    for i in range(len(s)):
        if s[i].isdigit():
            if s[i] == '0' or not s[i:].isdigit():
                return False
            else:
                break
    for c in s:
        if not (c.isalpha() or c.isdigit()):
            return False
    return True

if __name__ == "__main__":
    main()
