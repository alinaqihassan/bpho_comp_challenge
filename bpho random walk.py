import numpy as np
import matplotlib.pyplot as plt

N = 50 # no of steps
s = 1  # step size

x = [0]
y = [0]

for i in range(N):
    theta = np.random.uniform(0, 2*np.pi)
    delta_x = s*np.cos(theta)
    delta_y = s*np.sin(theta)
    x.append(x[-1]+delta_x)
    y.append(y[-1]+delta_y)

plt.plot(x, y)