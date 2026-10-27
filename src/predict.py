import json, sys, math
from pathlib import Path

def estimated_price(mileage, theta0, theta1):
    return theta0 + theta1 * mileage
try:
    here = Path(__file__).resolve().parent
    pathfile = here.parent / "model.json"
    with open(pathfile) as file:
        config = json.load(file)
        loaded = True
except FileNotFoundError:
    config = {"theta0": 0, "theta1": 0, "km_min": 0, "km_max": 1}
    loaded = False
try:
    ask = input("How much kilometers ? > ")
    km = float(ask)
except ValueError:
    print("Kilometers can't be letters. It must be a number.\n", file=sys.stderr)
    sys.exit(1)
if km < 0 or not math.isfinite(km):
    print("Kilometers can't be negative, 'nan' or 'inf'.\n", file=sys.stderr)
    sys.exit(1)
km_min = config.get("km_min")
km_max = config.get("km_max")
if km > km_max and loaded == True:
    print("Value out of range of data.\n", file=sys.stderr)
    sys.exit(1)
theta0 = config.get("theta0")
theta1 = config.get("theta1")
km_norm = (km - km_min) / (km_max - km_min)

print(estimated_price(km_norm, theta0, theta1))