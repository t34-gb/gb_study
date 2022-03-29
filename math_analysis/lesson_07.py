import numpy as np
import matplotlib.pyplot as plt

print('Задание: Найти экстремумы функций.')

x = np.linspace(-10, 10, 300)
y1 = np.abs(2*x)
y2 = 2*x/np.abs(x)

plt.plot(x, y1, label='y=|2*x|')
plt.plot(x, y2, label='y=2*x/|x|')
plt.xlabel('x')
plt.ylabel('y')
plt.plot([-10, 10], [0, 0], color='red', linewidth=0.75, linestyle="--")
plt.plot([0, 0], [0, 20], color='red', linewidth=0.75, linestyle="--")
plt.scatter(0, 0, c='red')
plt.legend()
plt.title('График функции: y = |2*x|')
plt.grid(True)
plt.show()

x = np.linspace(-5, 5, 300)
y1 = x**3
y2 = 3*x**2

plt.plot(x, y1, label='y=x^3')
plt.plot(x, y2, label='y=3*x^2')
plt.xlabel('x')
plt.ylabel('y')
plt.plot([-5, 5], [0, 0], color='red', linewidth=0.75, linestyle="--")
plt.plot([0, 0], [-150, 150], color='red', linewidth=0.75, linestyle="--")
plt.legend()
plt.title('График функции: y = x^3')
plt.grid(True)
plt.show()

x = np.linspace(-1, 1, 300)
y1 = np.e**(3*x)
y2 = 3*np.e**(3*x)

plt.plot(x, y1, label='y=e^(3x)')
plt.plot(x, y2, label='y=3*e^(3x)')
plt.xlabel('x')
plt.ylabel('y')
plt.plot([-1, 1], [0, 0], color='red', linewidth=0.75, linestyle="--")
plt.plot([0, 0], [-1, 100], color='red', linewidth=0.75, linestyle="--")
plt.legend()
plt.title('График функции: y = e^(3x)')
plt.grid(True)
plt.show()

x = np.linspace(-4, 4, 300)
y1 = x**3-5*x
y2 = 3*x**2-5

plt.plot(x, y1, label='y=x^3-5*x')
plt.plot(x, y2, label='y=3x^2-5')
plt.xlabel('x')
plt.ylabel('y')
plt.plot([-4, 4], [0, 0], color='red', linewidth=0.75, linestyle="--")
plt.plot([0, 0], [-40, 40], color='red', linewidth=0.75, linestyle="--")
m = round(np.sqrt(5/3), 2)
plt.scatter(-m, 0, c='red')
plt.scatter(m, 0, c='red')
plt.scatter(-m, -m**3+5*m, c='blue')
plt.scatter(m, m**3-5*m, c='blue')
plt.legend()
plt.title('График функции: y = x^3-5*x')
plt.grid(True)
plt.show()
