import sys
import inflect
from datetime import date


def main():
    birth = get_birth(input("Date of Birth: "))
    print(birth_to_delta_str(birth))


def get_birth(input_birth):
    try:
        year, month, day = input_birth.split("-")
        return date(int(year), int(month), int(day))
    except ValueError:
        sys.exit("Invalid date")


def birth_to_delta_str(birth):
    timedelta = int((date.today()-birth).days)
    minutes = inflect.engine().number_to_words(int(timedelta)*1440, andword="")
    return minutes.capitalize() + " minutes"


if __name__ == "__main__":
    main()
