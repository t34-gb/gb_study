from pylab import *
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

print('Задание. Исследовать на экстремум функцию.')

fig = figure()
ax = Axes3D(fig)
X = np.arange(-50, 50, 1)
Y = np.arange(-50, 50, 1)
X, Y = np.meshgrid(X, Y)
Z = X**2 + X*Y + Y**2 - 6*X - 9*Y
ax.plot_surface(X, Y, Z)

ax.set_title("График функции: Z = X^2 + XY + Y^2 - 6X - 9Y")
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
show()
