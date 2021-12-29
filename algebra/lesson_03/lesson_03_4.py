from pylab import *
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

print('Задание 7.4.1. Графическое решение системы уравнений:\n'
      'exp(x)+x(1-y)=1 и y=x^2-1')


def equations(p_):
    x_, y_ = p_
    return y_ - x_ ** 2 + 1, np.exp(x_) + x_ * (1 - y_) - 1


x1, y1 = fsolve(equations, (-2, 2))
print('x1, y1: ', x1, y1)
x2, y2 = fsolve(equations, (2, 5))
print('x2, y2: ', x2, y2)
x3, y3 = fsolve(equations, (4, 15))
print('x3, y3: ', x3, y3)

x = np.linspace(-6, 6, 201)
plt.plot(x, 1 + (np.exp(x) - 1) / x, label='exp(x)+x(1-y)=1')
plt.plot(x, x ** 2 - 1, label='y=x^2-1')
plt.xlabel('x')
plt.ylabel('y')
plt.ylim(-2, 30)
plt.plot([-6, 6], [0, 0], color='blue', linewidth=0.75, linestyle="--")
plt.scatter(x1, y1, c='r')
plt.text(x1, y1, f'A({round(x1, 1)}, {round(y1, 1)}) ',
         horizontalalignment='right', verticalalignment='bottom')
plt.scatter(x2, y2, c='r')
plt.text(x2, y2, f'B({round(x2, 1)}, {round(y2, 1)}) ',
         horizontalalignment='right', verticalalignment='bottom')
plt.scatter(x3, y3, c='r')
plt.text(x3, y3, f'C({round(x3, 1)}, {round(y3, 1)}) ',
         horizontalalignment='right', verticalalignment='bottom')
plt.grid(True)
plt.legend()
plt.title('Графическое решение системы уравнений:\nexp(x)+x(1-y)=1 и y=x^2-1')
plt.show()
print(f'Ответ: x1={round(x1, 1)}, x2={round(x2, 1)}, x3={round(x3, 1)}')
print('*' * 100)

print('Задание 7.4.2. Графическое решение системы неравенств:\n'
      'exp(x)+x(1-y)-1>0 и y=x^2-1')


def equation(x_):
    return np.exp(x_) - x_ ** 3 + 2 * x_ - 1


x1 = fsolve(equation, -2)[0]
print(f'x1: {x1}')
x2 = fsolve(equation, 1)[0]
print(f'x2: {x2}')
x3 = fsolve(equation, 2)[0]
print(f'x3: {x3}')
x4 = fsolve(equation, 4)[0]
print(f'x4: {x4}')

x = np.linspace(-6, 6, 201)
plt.plot(x, np.exp(x) - x ** 3 + 2 * x - 1)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.ylim(-5, 25)
plt.plot([-6, 6], [0, 0], color='red', linewidth=0.75, linestyle="--")
plt.scatter(x1, 0, c='r')
plt.text(x1, 0, f'(- ~, {round(x1, 1)})  ',
         horizontalalignment='right', verticalalignment='bottom')
plt.scatter(x2, 0, c='r')
plt.scatter(x3, 0, c='r')
plt.text(x3, 0, f'({round(x2, 1)}, {round(x3, 1)})   ',
         horizontalalignment='right', verticalalignment='bottom')
plt.scatter(x4, 0, c='r')
plt.text(x4, 0, f' ({round(x4, 1)}, + ~)',
         horizontalalignment='left', verticalalignment='bottom')
plt.grid(True)
plt.title('Графическое решение системы неравенств:\nexp(x)+x(1-y)-1>0 и y=x^2-1')
plt.show()
print(f'Ответ: x-> (- ~, {round(x1, 1)}), ({round(x2, 1)}, {round(x3, 1)}), ({round(x4, 1)}, + ~)')
