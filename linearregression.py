x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

m = 0
b = 0

lr = 0.01
epochs = 1000
n = len(x)

for _ in range(epochs):

    dm = 0
    db = 0

    for i in range(n):
        pred = m * x[i] + b
        error = y[i] - pred

        dm += (-2 / n) * x[i] * error
        db += (-2 / n) * error

    m = m - lr * dm
    b = b - lr * db

print("Slope =", m)
print("Intercept =", b)

print("Prediction =", m * 6 + b)