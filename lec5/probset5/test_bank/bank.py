def main():
    greeting = input("Greeting: ").lstrip().lower()
    print(f"${value(greeting)}")


def value(greeting):
    if greeting[0] == "h":
        if greeting[1:5] == "ello":
            return 0
        else:
            return 20
    else:
        return 100


if __name__ == "__main__":
    main()


