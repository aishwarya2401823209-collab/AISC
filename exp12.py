
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 100, 200)

def tri(x, a, b, c):
    return np.maximum(0, np.minimum((x-a)/(b-a), (c-x)/(c-b)))

def trap(x, a, b, c, d):
    return np.maximum(0, np.minimum(np.minimum((x-a)/(b-a), 1), (d-x)/(d-c)))

def gauss(x, m, s):
    return np.exp(-((x-m)**2)/(2*s**2))

plt.plot(x, tri(x, 0, 20, 50), label="Lightly")
plt.plot(x, tri(x, 25, 50, 75), label="Moderately")
plt.plot(x, tri(x, 50, 80, 100), label="Heavily")
plt.plot(x, trap(x, 0, 0, 15, 40), label="Lightly Trap")
plt.plot(x, trap(x, 25, 40, 60, 75), label="Moderately Trap")
plt.plot(x, trap(x, 60, 85, 100, 100), label="Heavily Trap")
plt.plot(x, gauss(x, 20, 12), label="Lightly Gaussian")
plt.plot(x, gauss(x, 50, 12), label="Moderately Gaussian")
plt.plot(x, gauss(x, 80, 12), label="Heavily Gaussian")
plt.xlabel("Soil Level")
plt.ylabel("Membership")
plt.title("Washing Machine")
plt.legend()
plt.show()
