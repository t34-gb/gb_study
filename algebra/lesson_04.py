import numpy as np
import matplotlib.pyplot as plt

print('Задание 4. Решить уравнение sin(a*x), где 0,01<a<0,02, 100<x<500')
a = np.linspace(0.01, 0.02, 100)
x = 40000 * a - 300
plt.plot(a, x)
plt.xlabel('a')
plt.ylabel('x')
plt.grid(True)
plt.title('График функции: x=40000*a-300')
plt.show()

a = np.linspace(0.01, 0.02, 100)
x = 40000 * a - 300
y = np.sin(a * x)
plt.plot(a, y)
plt.xlabel('a')
plt.ylabel('y')
plt.plot([0.01, 0.02], [0, 0], color='red', linewidth=0.75, linestyle="--")
plt.scatter(0.013370941, 0, c='r')
plt.scatter(0.016829086, 0, c='r')
plt.scatter(0.019547547, 0, c='r')
plt.grid(True)
plt.title('График функции: y=sin(40000*a^2-300*a)')
plt.show()

print('Задание 17.6.5. График функции: (y-1)^2=2*x+6')
x = np.linspace(-3, 10, 200)
y1 = np.sqrt(2 * x + 6) + 1
y2 = -np.sqrt(2 * x + 6) + 1
plt.ylim(-1, 5, 1, 5)
plt.xlim(-4, 4)
plt.plot(x, y1)
plt.plot(x, y2)
plt.plot([-10, 10], [0, 0], color='red', linewidth=0.75, linestyle="--")
plt.plot([0, 0], [-7, 7], color='red', linewidth=0.75, linestyle="--")
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.title('График функции: (y-1)^2=2*x+6')
plt.show()

print('Задание 17.6.6. График функции эллипса: x^2/a^2 + y^2/b^2=1')
x = np.linspace(-np.sqrt(5) - 2, np.sqrt(5) - 2, 1000)
y1 = np.sqrt((1 - (x + 2) ** 2 / 5) * 3) + 3
y2 = -np.sqrt((1 - (x + 2) ** 2 / 5) * 3) + 3
c1 = -np.sqrt(5 - 3) - 2
c2 = np.sqrt(5 - 3) - 2
plt.ylim(-2, 8)
plt.xlim(-6, 2)
plt.plot(x, y1)
plt.plot(x, y2)
plt.scatter(c1, 3, c='r')
plt.scatter(c2, 3, c='r')
plt.plot([-10, 10], [3, 3], color='blue', linewidth=0.75, linestyle="--")
plt.plot([-10, 10], [0, 0], color='red', linewidth=0.75, linestyle="--")
plt.plot([0, 0], [-10, 10], color='red', linewidth=0.75, linestyle="--")
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.title('График функции эллипса: (x+2)^2/5 + (y-3)^2/3=1')
plt.show()

print('Задание 17.6.7. График функции мнимой гиперболы: x^2/a^2 - y^2/b^2=-1')
x1 = np.linspace(-10, -1, 200)
y1 = np.sqrt((x1 ** 2 - 1) * 2) + 3
y1_ = -np.sqrt((x1 ** 2 - 1) * 2) + 3
x2 = np.linspace(1, 10, 200)
y2 = np.sqrt((x2 ** 2 - 1) * 2) + 3
y2_ = -np.sqrt((x2 ** 2 - 1) * 2) + 3
c1 = -np.sqrt(1 + 2)
c2 = np.sqrt(1 + 2)
plt.ylim(-7, 13)
plt.xlim(-10, 10)
plt.plot(x1, y1, linestyle="--")
plt.plot(x1, y1_, linestyle="--")
plt.plot(x2, y2, linestyle="--")
plt.plot(x2, y2_, linestyle="--")
plt.scatter(c1, 3, c='r')
plt.scatter(c2, 3, c='r')
plt.plot([-10, 10], [3, 3], color='blue', linewidth=0.75, linestyle="--")
plt.plot([-10, 10], [0, 0], color='red', linewidth=0.75, linestyle="--")
plt.plot([0, 0], [-10, 10], color='red', linewidth=0.75, linestyle="--")
plt.xlabel('x')
plt.ylabel('y')
plt.title('График функции мнимой гиперболы: x^2/1 - (y-3)^2/2=-1')
plt.grid(True)
plt.show()

print('Задание 17.6.8. График функции гиперболы: x^2/a^2 - y^2/b^2=1')
x1 = np.linspace(-2, -np.sqrt(3) + 7, 200)
y1 = np.sqrt(((x1 - 7) ** 2 / 3 - 1) * 2) - 7
y1_ = -np.sqrt(((x1 - 7) ** 2 / 3 - 1) * 2) - 7
x2 = np.linspace(np.sqrt(3) + 7, 17, 200)
y2 = np.sqrt(((x2 - 7) ** 2 / 3 - 1) * 2) - 7
y2_ = -np.sqrt(((x2 - 7) ** 2 / 3 - 1) * 2) - 7
c1 = -np.sqrt(3 + 2)
c2 = np.sqrt(3 + 2)
plt.ylim(-16, 5)
plt.xlim(-3, 17)
plt.plot(x1, y1)
plt.plot(x1, y1_)
plt.plot(x2, y2)
plt.plot(x2, y2_)
plt.scatter(c1 + 7, -7, c='r')
plt.scatter(c2 + 7, -7, c='r')
plt.plot([-3, 17], [-7, -7], color='blue', linewidth=0.75, linestyle="--")
plt.plot([-3, 17], [0, 0], color='red', linewidth=0.75, linestyle="--")
plt.plot([0, 0], [-16, 5], color='red', linewidth=0.75, linestyle="--")
plt.xlabel('x')
plt.ylabel('y')
plt.title('График функции гиперболы: (x-7)^2/3 - (y+7)^2/2=1')
plt.grid(True)
plt.show()
