def main():
    while True:
        date_in = input("Date: ").strip()
        try:
            if date_in[0].isdigit():
                m, d, y = date_in.split("/")
            else:
                    md, y = date_in.split(", ")
                    m, d = md.split(" ")
                    m = str(mon.index(m) + 1)
        except ValueError:
            pass
        else:
            if 1 <= int(m) <= 12 and 1 <= int(d) <= 31:
                if len(m) < 2:
                    m = "0" + m
                if len(d) < 2:
                    d = "0" + d
                break
    print(y, m, d, sep="-")


mon = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


main()
