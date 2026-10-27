
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 100, 200)

def tri(x, a, b, c):
    return np.maximum(0, np.minimum((x-a)/(b-a), (c-x)/(c-b)))

def trap(x, a, b, c, d):
    return np.maximum(0, np.minimum(np.minimum((x-a)/(b-a), 1), (d-x)/(d-c)))

def gauss(x, m, s):
    return np.exp(-((x-m)**2)/(2*s**2))

for name, p in [("Low", (0, 20, 50)), ("Medium", (25, 50, 75)), ("High", (50, 80, 100))]:
    plt.plot(x, tri(x, *p), label=name + " Tri")

for name, p in [("Low", (0, 0, 20, 45)), ("Medium", (25, 40, 60, 75)), ("High", (55, 80, 100, 100))]:
    plt.plot(x, trap(x, *p), label=name + " Trap")

for name, m in [("Low", 20), ("Medium", 50), ("High", 80)]:
    plt.plot(x, gauss(x, m, 15), label=name + " Gaussian")

plt.xlabel("Traffic Density")
plt.ylabel("Membership")
plt.title("Traffic Signal Control")
plt.legend()
plt.show()
