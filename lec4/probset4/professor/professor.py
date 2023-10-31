import random


def main():
    level = get_level()
    score = 0
    for _ in range(10):
        X, Y = generate_integer(level), generate_integer(level)
        for i in range(3):
            ans = int(input(f"{X} + {Y} = "))
            if ans != X + Y:
                if i < 2:
                    print("EEE")
                else:
                    print(f"{X} + {Y} = {X + Y}")
            else:
                score += 1
                break
    print(score)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass


def generate_integer(level):
    match level:
        case 1:
            return random.randint(0, 9)
        case 2:
            return random.randint(10, 99)
        case 3:
            return random.randint(100, 999)


if __name__ == "__main__":
    main()
