import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(np.pi * -2, np.pi * 2, num = 125)
y1 = np.sin(x)
y2 = np.cos(x)
plt.plot(x, y1)
plt.plot(x, y2)
plt.xticks(np.linspace(np.pi * -2, np.pi * 2, num = 5))
plt.grid()
plt.show()