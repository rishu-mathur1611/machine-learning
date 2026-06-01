x = [10,8,7,4,6]
y = [50,40,42,12,18]

x_mean = sum(x) / len(x)
y_mean = sum(y) / len(y)

num = 0
den = 0

for i in range(len(x)):
    num += (x[i] - x_mean) * (y[i] - y_mean)
    den += (x[i] - x_mean) ** 2

m = num / den
b = y_mean - m * x_mean

print("Slope =", m)
print("Intercept =", b)

# Prediction
x_test = 4
y_pred = m * x_test + b

print("Prediction =", y_pred)