while True:
    try:
        x, y = input("Fraction: ").split('/')
        fuel = round((int(x)/int(y))*100)
        if not 0 <= fuel <= 100:
            continue
    except (ValueError, ZeroDivisionError):
        pass
    else:
        if fuel == 99 or fuel == 100:
            print('F')
        elif fuel == 0 or fuel == 1:
            print('E')
        else:
            print(fuel, '%', sep='')
        break
