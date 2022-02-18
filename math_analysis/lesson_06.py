import numpy as np
import matplotlib.pyplot as plt

print('Задание: Найти угол наклона касательной к графику функции f(x)=(3*x)^(1/3)*ln(x).')

x = np.linspace(0.01, 10)
y = (3*x)**(1/3) * np.log(x)

x1 = np.linspace(0.01, 10)
y1 = 3**(1/3)*(x - 1)

plt.plot(x, y, label='Функция: f(x)=(3*x)^(1/3)*ln(x)')
plt.plot(x1, y1, label='Касательная: f(x)=3^(1/3)*(x-1)')

plt.xlabel('x')
plt.ylabel('f(x)')
plt.plot([-1, 10], [0, 0], color='red', linewidth=0.75, linestyle="--")
plt.plot([0, 0], [-2, 13], color='red', linewidth=0.75, linestyle="--")
plt.scatter(1, 0, c='red')
plt.legend()
plt.title('График функции: f(x)=(3*x)^(1/3)*ln(x)')
plt.grid(True)
plt.show()

alfa = np.arctan(np.sqrt(3))
print('Угол наклона касательной: alfa =', round(alfa*180/np.pi))
