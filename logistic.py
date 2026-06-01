import math

x = [1, 2, 3, 4, 5]
y = [0, 0, 0, 1, 1]

w = 0
b = 0

lr = 0.01
epochs = 1000

for _ in range(epochs):

    dw = 0
    db = 0

    for i in range(len(x)):

        z = w * x[i] + b
        pred = 1 / (1 + math.exp(-z))

        error = pred - y[i]

        dw += error * x[i]
        db += error

    w -= lr * dw
    b -= lr * db

test = 4.3

z = w * test + b
pred = 1 / (1 + math.exp(-z))

print("Probability =", pred)

if pred >= 0.5:
    print("Class = 1")
else:
    print("Class = 0")