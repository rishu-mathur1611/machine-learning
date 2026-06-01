import math

# Training data
X = [
    [1, 2],
    [2, 3],
    [3, 3],
    [6, 7],
    [7, 8],
    [8, 8]
]

y = [0, 0, 0, 1, 1, 1]

# Test point
test = [5, 6]

k = 3

distances = []

# Calculate distance from test point to all points
for i in range(len(X)):

    x1 = X[i][0]
    y1 = X[i][1]

    x2 = test[0]
    y2 = test[1]

    d = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

    distances.append([d, y[i]])

# Sort by distance
distances.sort()

# Take k nearest neighbors
neighbors = distances[:k]

# Voting
votes = []

for d, label in neighbors:
    votes.append(label)

prediction = max(set(votes), key=votes.count)

print("Nearest Neighbors:")
print(neighbors)

print("Predicted Class =", prediction)