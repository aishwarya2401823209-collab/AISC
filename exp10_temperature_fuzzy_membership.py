
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 40, 200)

def tri(x, a, b, c):
    return np.maximum(0, np.minimum((x-a)/(b-a), (c-x)/(c-b)))

def trap(x, a, b, c, d):
    return np.maximum(0, np.minimum(np.minimum((x-a)/(b-a), 1), (d-x)/(d-c)))

def gauss(x, m, s):
    return np.exp(-((x-m)**2)/(2*s**2))

for name, p in [("Cold", (0, 10, 20)), ("Comfortable", (10, 22, 32)), ("Hot", (22, 32, 40))]:
    plt.plot(x, tri(x, *p), label=name + " Tri")

for name, p in [("Cold", (0, 0, 8, 18)), ("Comfortable", (12, 18, 25, 30)), ("Hot", (25, 33, 40, 40))]:
    plt.plot(x, trap(x, *p), label=name + " Trap")

for name, m in [("Cold", 8), ("Comfortable", 22), ("Hot", 34)]:
    plt.plot(x, gauss(x, m, 5), label=name + " Gaussian")

plt.xlabel("Temperature (C)")
plt.ylabel("Membership")
plt.title("Room Temperature")
plt.legend()
plt.show()
