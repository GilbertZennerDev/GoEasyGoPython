import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 200)
y = np.sin(3*x)

fig, ax = plt.subplots()
ax.plot(x, y)

# Save the figure to a file
plt.savefig('./plot.png')