import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 121)

plt.plot(x, np.cos(x))
plt.plot(x, np.cos(5 * x))
plt.show()
