def main():
    camel = input("camelCase: ")
    snake = camel2snake(camel)
    print(f"snake_case: {snake}")

def camel2snake(camel):
    snake = ""
    for c in camel:
        if c.isupper():
            snake += '_' + c.lower()
        else:
            snake += c
    return snake

main()
