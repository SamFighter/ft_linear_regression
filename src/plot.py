import csv, json
from pathlib import Path
import matplotlib.pyplot as plt

kms = []
prices = []
learning_rate = 0.1

here = Path(__file__).resolve().parent
data_path = here.parent / "data/data.csv"
with open(data_path) as file:
    reader = csv.DictReader(file)
    for line in reader:
        kms.append(float(line["km"]))
        prices.append(float(line["price"]))

def estimated_price(mileage, theta0, theta1):
    return theta0 + theta1 * mileage
try:
    here = Path(__file__).resolve().parent
    json_path = here.parent / "model.json"
    with open(json_path) as file:
        config = json.load(file)
        loaded = True
except FileNotFoundError:
    config = {"theta0": 0, "theta1": 0, "km_min": 0, "km_max": 1}
    loaded = False

theta0 = config.get("theta0")
theta1 = config.get("theta1")
km_min = config.get("km_min")
km_max = config.get("km_max")

km_min_norm = (km_min - km_min) / (km_max - km_min)
km_max_norm = (km_max - km_min) / (km_max - km_min)
price_min = estimated_price(km_min_norm, theta0, theta1)
price_max = estimated_price(km_max_norm, theta0, theta1)

plt.scatter(kms, prices)
plt.xlabel("Kms")
plt.ylabel("Prices")
plt.title("Prices per kms")
plt.plot([km_min, km_max], [price_min, price_max], color="red")
plt.show()