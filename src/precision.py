import csv, json
from pathlib import Path

kms = []
prices = []

here = Path(__file__).resolve().parent
data_path = here.parent / "data/data.csv"
with open(data_path) as file:
    reader = csv.DictReader(file)
    for line in reader:
        kms.append(float(line["km"]))
        prices.append(float(line["price"]))

try:
    herejson = Path(__file__).resolve().parent
    json_path = herejson.parent / "model.json"
    with open(json_path) as file:
        config = json.load(file)
except FileNotFoundError:
    config = {"theta0": 0, "theta1": 0, "km_min": 0, "km_max": 1}
    print("Model is not trained. Mean error will be the estimated price.")

theta0 = config.get("theta0")
theta1 = config.get("theta1")
km_min = config.get("km_min")
km_max = config.get("km_max")

kms_norm = [(k - km_min) / (km_max - km_min) for k in kms]

def estimated_price(mileage, theta0, theta1):
    return theta0 + theta1 * mileage

def mean_abs_error(kms, prices, theta0, theta1):
    return sum(abs(estimated_price(km, theta0, theta1) - price) for km, price in zip(kms, prices)) / len(kms)

print("Mean absolute error: ", mean_abs_error(kms_norm, prices, theta0, theta1))