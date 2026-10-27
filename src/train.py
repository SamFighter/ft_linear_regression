import csv, json

kms = []
prices = []
theta0 = 0.0
theta1 = 0.0
learning_rate = 0.1

with open("../data/data.csv") as file:
    reader = csv.DictReader(file)
    for line in reader:
        kms.append(float(line["km"]))
        prices.append(float(line["price"]))

def estimated_price(mileage, theta0, theta1):
    return theta0 + theta1 * mileage

def mean_error(kms, prices, theta0, theta1):
    return sum(estimated_price(km, theta0, theta1) - price for km, price in zip(kms, prices)) / len(kms)

def mean_error_km(kms, prices, theta0, theta1):
    return sum((estimated_price(km, theta0, theta1) - price) * km for km, price in zip(kms, prices)) / len(kms)

km_min = min(kms)
km_max = max(kms)
kms_norm = [(k - km_min) / (km_max - km_min) for k in kms]

for i in range(100000):
    tmp_theta0 = mean_error(kms_norm, prices, theta0, theta1) * learning_rate
    tmp_theta1 = mean_error_km(kms_norm, prices, theta0, theta1) * learning_rate
    if abs(tmp_theta0) < 0.0001 and abs(tmp_theta1) < 0.0001:
        break
    theta0 = theta0 - tmp_theta0
    theta1 = theta1 - tmp_theta1
config = {"theta0": theta0, "theta1": theta1, "km_min": km_min, "km_max": km_max}
with open("../model.json", "w") as f:
    json.dump(config, f)

print(i)
print("theta0 =", theta0)
print("theta1 =", theta1)
print("mean error =", mean_error(kms_norm, prices, theta0, theta1), "\n")