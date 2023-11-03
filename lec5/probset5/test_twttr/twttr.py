def main():
    # print(remove_vowel(input("Input: ")))
    print(f"Output: {remove_vowel(input("Input: "))}")

def shorten(word):
    wrd = ""
    for c in word:
        if c.lower() not in ['a', 'e', 'i', 'o', 'u']:
            wrd += c
    return wrd

if __name__ == "__main__":
    main()
