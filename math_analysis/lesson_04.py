import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

print('Задание: Исследование функции f(x)=x^3-x^2.')

x = np.linspace(-1, 2)
y = x**3 - x**2

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.plot([-2, 2], [0, 0], color='red', linewidth=0.75, linestyle="--")
plt.plot([0, 0], [-4, 4], color='red', linewidth=0.75, linestyle="--")
plt.scatter(0, 0, c='red')
plt.scatter(1, 0, c='red')
plt.title('График функции: f(x)=x^3-x^2')
plt.grid(True)
plt.show()

x = np.linspace(-10, 10)
y = x**3 - x**2

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.plot([-10, 10], [0, 0], color='red', linewidth=0.75, linestyle="--")
plt.plot([0, 0], [-1000, 1000], color='red', linewidth=0.75, linestyle="--")
plt.scatter(0, 0, c='red')
plt.scatter(1, 0, c='red')
plt.title('График функции: f(x)=x^3-x^2')
plt.grid(True)
plt.show()
