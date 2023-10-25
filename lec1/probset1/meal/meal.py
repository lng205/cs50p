def main():
    time = convert(input("What time is it? "))
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")


def convert(time):
    h, m = time.split(':')

    # 12-hour
    if len(m) > 2:
        if m[3] == 'p':
            h = float(h) + 12
        return h + float(m[:2]) / 60

    return float(h) + float(m) / 60


if __name__ == "__main__":
    main()