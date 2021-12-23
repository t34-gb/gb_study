from pylab import *
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

print('Задание № 1. Расчёт длины вектора, заданного его координатами.')
num = input('Введите координаты вектора через пробел (x1, x2, x3): ').split()
num = tuple(map(float, num))
x1, x2, x3 = num
x = np.sqrt(x1 ** 2 + x2 ** 2 + x3 ** 2)
print(f'Длина вектора {x1, x2, x3} равна {x}')
print('*' * 100)
# ==================================================================================

print('Задание № 3.1. Построение графика окружности.')
num = input('Введите радиус (r) и координаты центра (x0, y0) через пробел: ').split()
num = tuple(map(float, num))
r, x0, y0 = num
x = np.linspace(x0 - r, x0 + r, 300)
y1 = np.sqrt(r ** 2 - (x - x0) ** 2) + y0
y2 = -np.sqrt(r ** 2 - (x - x0) ** 2) + y0
plt.plot(x, y1)
plt.plot(x, y2)
plt.plot([-10, 10], [0, 0], color='red', linewidth=0.75, linestyle="--")
plt.plot([0, 0], [-10, 10], color='red', linewidth=0.75, linestyle="--")
plt.xlabel('X')
plt.ylabel('Y')
plt.grid()
plt.scatter(x0, y0, c='red')
plt.show()

print('Задание № 3.2. Построение графика эллипса.')
num = input('Введите оси эллипса через пробел (a b): ').split()
num = tuple(map(float, num))
a, b = num
x = np.linspace(-a, a, 300)
y1 = np.sqrt(1 - (x / a) ** 2) * b
y2 = -np.sqrt(1 - (x / a) ** 2) * b
c = np.sqrt(a ** 2 - b ** 2)
plt.plot(x, y1)
plt.plot(x, y2)
plt.plot([-10, 10], [0, 0], color='red', linewidth=0.75, linestyle="--")
plt.plot([0, 0], [-10, 10], color='red', linewidth=0.75, linestyle="--")
plt.xlabel('X')
plt.ylabel('Y')
plt.grid()
plt.scatter(-c, 0, c='red')
plt.scatter(c, 0, c='red')
plt.show()

print('Задание № 3.3. Построение графика гиперболы.')
x1 = []
x2 = []
y1 = []
y2 = []
# a, b = (4, 2)
for i in range(100):
    x_ = a + i / 20
    x1.append(x_)
    x2.append(-x_)
    y1.append(np.sqrt((x_ / a) ** 2 - 1) * b)
    y2.append(-np.sqrt((x_ / a) ** 2 - 1) * b)
c = np.sqrt(a ** 2 + b ** 2)
plt.plot(x1, y1)
plt.plot(x1, y2)
plt.plot(x2, y1)
plt.plot(x2, y2)
plt.plot([-10, 10], [0, 0], color='red', linewidth=0.75, linestyle="--")
plt.plot([0, 0], [-10, 10], color='red', linewidth=0.75, linestyle="--")
plt.xlabel('X')
plt.ylabel('Y')
plt.grid()
plt.scatter(-c, 0, c='red')
plt.scatter(c, 0, c='red')
plt.show()
print('*' * 100)
# ==================================================================================

print('Задание № 5.1. Построение графика двух параллельных плоскостей.')
fig = figure()
ax = Axes3D(fig)
X = np.arange(-50, 50, 1)
Y = np.arange(-50, 50, 1)
X, Y = np.meshgrid(X, Y)
Z1 = -5 * (X + 50) - (Y + 20) * 4
Z2 = 5 - 5 * X - 4 * Y
ax.plot_surface(X, Y, Z1)
ax.plot_surface(X, Y, Z2)
ax.set_title("Parallel planes ")
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
show()

print('Задание 5.2. Построение графика плоскости 2-го порядка в пространстве. Эллиплический параболоид.')
fig = figure()
ax = Axes3D(fig)
X = np.arange(-50, 50, 1)
Y = np.arange(-50, 50, 1)
X, Y = np.meshgrid(X, Y)
Z = (X / 50) ** 2 + (Y / 50) ** 2
ax.plot_surface(X, Y, Z)
ax.set_title("Эллиплический параболоид ")
show()

print('Задание 5.3. Построение графика плоскости 2-го порядка в пространстве. Конус.')
fig = figure()
ax = Axes3D(fig)
X = np.arange(-50, 50, 1)
Y = np.arange(-50, 50, 1)
X, Y = np.meshgrid(X, Y)
Z1 = np.sqrt(((X / 5) ** 2 + (Y / 5) ** 2) * 8 ** 2)
Z2 = -(np.sqrt(((X / 5) ** 2 + (Y / 5) ** 2) * 8 ** 2))
ax.plot_surface(X, Y, Z1)
ax.plot_surface(X, Y, Z2)
ax.set_title("Конус")
show()
