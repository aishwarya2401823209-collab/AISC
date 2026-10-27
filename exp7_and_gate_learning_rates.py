
import numpy as np

x = np.array([[0,0], [0,1], [1,0], [1,1]])
y = np.array([0, 0, 0, 1])

for lr in [0.1, 0.3, 0.5]:
    w = np.array([0.1, 0.1])
    b = 0.1
    epochs = 0

    for epoch in range(1000):
        error_sum = 0

        for i in range(len(x)):
            net = np.dot(x[i], w) + b
            output = 1 / (1 + np.exp(-net))
            error = y[i] - output

            w += lr * error * output * (1 - output) * x[i]
            b += lr * error * output * (1 - output)
            error_sum += error ** 2

        epochs = epoch + 1

        if error_sum < 0.01:
            break

    print("Learning Rate:", lr)
    print("Epochs:", epochs)
    print("Final Weights:", np.round(w, 3))
    print("Final Bias:", round(b, 3))
    print()
