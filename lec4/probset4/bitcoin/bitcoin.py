import sys
import requests

try:
    n = float(sys.argv[1])
except IndexError:
    sys.exit("Missing command-line argument")
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    price = float(r.json()["bpi"]["USD"]["rate_float"])
except requests.RequestException:
    sys.exit("Request error")

amount = float(sys.argv[1]) * price
print(f"${amount:,.4f}")
