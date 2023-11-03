def main():
    while True:
        try:
            percentage = convert(input("Fraction: "))
            break
        except (ValueError, ZeroDivisionError):
            pass
    print(gauge(percentage))


def convert(fraction):
    x, y = fraction.split("/")
    percentage = round((int(x) / int(y)) * 100)
    if not 0 <= percentage <= 100:
        raise ValueError
    return percentage


def gauge(percentage):
    if percentage == 99 or percentage == 100:
        return "F"
    elif percentage == 0 or percentage == 1:
        return "E"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
