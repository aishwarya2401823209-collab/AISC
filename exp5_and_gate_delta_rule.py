x = [(0, 0), (0, 1), (1, 0), (1, 1)]
y = [0, 0, 0, 1]

w1 = 0.1
w2 = 0.1
b = 0.1
lr = 0.1

for epoch in range(1000):
    for i in range(4):
        a, c = x[i]
        target = y[i]
        net = a * w1 + c * w2 + b
        output = 1 if net >= 0.5 else 0
        error = target - output
        w1 += lr * error * a
        w2 += lr * error * c
        b += lr * error

print("Final weights:", w1, w2)
print("Final bias:", b)

for a, c in x:
    net = a * w1 + c * w2 + b
    output = 1 if net >= 0.5 else 0
    print(a, c, "=", output)