x, y, z = input("Expression: ").split(' ')
x, z = float(x), float(z)

match y:
    case '+':
        ans = x + z
    case '-':
        ans = x - z
    case '*':
        ans = x * z
    case '/':
        ans = x / z

print(ans)