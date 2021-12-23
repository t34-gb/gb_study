from pylab import *
from scipy.optimize import fsolve
import numpy as np
import matplotlib.pyplot as plt


def f(x_, k_, a_, b_):
    return k_ * np.cos(x_ - a_) + b_


print('Задание № 1. График функции: y=k*cos(x-a)+b')
num = input('Введите числовые значения k, a, b через пробел для 1-го графика: ').split()
k1, a1, b1 = tuple(map(float, num))
num = input('Введите числовые значения k, a, b через пробел для 2-го графика: ').split()
k2, a2, b2 = tuple(map(float, num))

x1 = np.linspace(-3 * np.pi, 3 * np.pi, 201)
plt.plot(x1, f(x1, k1, a1, b1))
plt.plot(x1, f(x1, k2, a2, b2))
plt.plot([-10, 10], [0, 0], color='red', linewidth=0.75, linestyle="--")
plt.xlabel('x')
plt.ylabel('y')
plt.title('График функции: y=k*cos(x-a)+bv')
plt.grid(True)
plt.show()
print('*' * 100)


# ===================================================================================


def f_dec(p1, t1):
    x_ = p1 * cos(t1)
    y_ = p1 * sin(t1)
    return x_, y_


print('Задание № 3.1а. Перевод полярных координат в декартовые.')
num = input('Введите числовые значения полярных координат (p, t) через пробел: ').split()
p, t = tuple(map(float, num))
print('Декартовые координаты: (x, y) = ', f_dec(p, t))


def f_pol(x_, y_):
    p_ = np.sqrt(x_ ** 2 + y_ ** 2)
    t_ = np.arctan(y_ / x_)
    return p_, t_


print('Задание № 3.1b. Перевод декартовых координат в полярные.')
num = input('Введите числовые значения декартовых координат (x, y) через пробел: ').split()
x, y = tuple(map(float, num))
print('Полярные координаты: (p, t) = ', f_pol(x, y))
print('*' * 100)
# ==================================================================================

print('Задание № 3.2. График окружности в полярных координатах.')
r = float(input('Введите радиус окружности: '))
a = np.linspace(0, 2 * np.pi, 180)
x1 = r * cos(a)
y1 = r * sin(a)
plt.plot(x1, y1)
plt.plot([-10, 10], [0, 0], color='red', linewidth=0.75, linestyle="--")
plt.xlabel('x')
plt.ylabel('y')
plt.scatter(0, 0, c='r')
plt.title(f'Окружность в декартовых координатах через полярные координаты: r = {r}')
plt.grid(True)
plt.show()

plt.figure()
t = np.linspace(0, 2 * np.pi, 360)
for i in t:
    plt.polar(i, r, 'g.')
plt.scatter(0, 0)
t = np.linspace(-np.pi / 2, np.pi / 2, 180)
plt.polar(t, 2 * r * cos(t))
plt.scatter(0, r)
t = np.linspace(0, np.pi, 180)
plt.polar(t, 2 * r * sin(t))
plt.scatter(pi / 2, r)
plt.title(f'Окружности в полярных координатах: r = {r}')
plt.show()

plt.figure()
a = 5
b = 3
t = np.linspace(0, 2 * np.pi, 360)
for i in t:
    r = (a * b) / np.sqrt((a * sin(i)) ** 2 + (b * cos(i)) ** 2)
    plt.polar(i, r, 'g.')
c = np.sqrt(a ** 2 - b ** 2)
plt.scatter(0, c)
plt.text(0, c, f'C1({0}, {round(c)})',
         horizontalalignment='center', verticalalignment='bottom')
plt.scatter(pi, c)
plt.text(pi, c, f'C2({180}, {round(c)})',
         horizontalalignment='center', verticalalignment='bottom')
plt.title(f'Эллипс в полярных координатах.')
plt.show()
print('*' * 100)
# ==================================================================================

print('Задание № 3.3. График прямой в полярных координатах.')
num = input('Введите числовые значения (A, B, C)!=0 через пробел для уравнения прямой: ').split()
A, B, C = tuple(map(float, num))

x = np.linspace(-5, 5, 21)
y = -A * x / B - C / B
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title(f'График прямой {A}x + {B}y + {C} = 0 в декартовых координатах.')
plt.show()

plt.figure()
P = abs(C) / np.sqrt(A ** 2 + B ** 2)
print(P)
if C > 0:
    alfa = arccos(A / np.sqrt(A ** 2 + B ** 2))
    theta = np.linspace(alfa - pi / 4, alfa + pi / 4, 400)
    for sigma in theta:
        p = P / cos(sigma - alfa)
        plt.polar(sigma, p, 'b.')
elif C < 0:
    alfa = arccos(-A / np.sqrt(A ** 2 + B ** 2))
    theta = np.linspace(alfa - pi / 4, alfa + pi / 4, 400)
    for sigma in theta:
        p = P / cos(sigma - alfa)
        plt.polar(sigma, p, 'b.')
elif C == 0:
    alfa = arccos(-A / np.sqrt(A ** 2 + B ** 2))
    p = np.linspace(0, 10, 400)
    for i in p:
        plt.polar(alfa, i, 'b.')
        plt.polar(alfa - pi, i, 'b.')

plt.thetagrids([theta * 30 for theta in range(360 // 30)])  # сетка лучей
plt.title(f'График прямой {A}x + {B}y + {C} = 0 в полярных координатах.')
plt.show()
print('*' * 100)
# ==================================================================================

print('Задание № 4.1. Численное и графическое решение системы уравнений:\n'
      ' exp(x)+x(1-y)=1 и y=x^2-1')


def equations(p_):
    x_, y_ = p_
    return y_ - x_ ** 2 + 1, np.exp(x_) + x_ * (1 - y_) - 1


x1, y1 = fsolve(equations, (-2, 2))
print('x1, y1: ', x1, y1)
x2, y2 = fsolve(equations, (2, 5))
print('x2, y2: ', x2, y2)

x = np.linspace(-2, 3, 201)
plt.plot(x, 1 + (np.exp(x) - 1) / x)
plt.plot(x, x ** 2 - 1)
plt.xlabel('x')
plt.ylabel('y')
plt.ylim(-2, 8)
plt.grid(True)
plt.show()
print('*' * 100)
# ==================================================================================

print('Задание № 4.2. Численное и графическое решение системы неравенств:\n'
      ' exp(x)+x(1-y)-1>0 и y=x^2-1')

print(f'Область решений:\n y=x^2-1 для x!=0, x=({x1}, {x2})')
