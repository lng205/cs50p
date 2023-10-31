def main():
    # print(remove_vowel(input("Input: ")))
    print(f"Output: {remove_vowel(input("Input: "))}")

def remove_vowel(str_in):
    str_out = ""
    for c in str_in:
        if c.lower() not in ['a', 'e', 'i', 'o', 'u']:
            str_out += c
    return str_out

main()
