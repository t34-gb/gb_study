# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

print('Задание № 5.1а: Свойства сложения и умножения для векторов.')
a = np.array([0, 1, 2, 3, 4, 5])
print('Исходный вектор: ', a)

print('*'*20 + ' (k*l)*A = k*(l*A) ' + '*'*20)
print('(2*2)*a: ', (2*2)*a)
print('2*(2*a): ', 2*(2*a))

print()
b = a + 1
print('b = a + 1: ', b)

print()
print('*'*20 + ' Произведение векторов ' + '*'*20)
print('a * b: ', a * b)

print('np.outer(a, b): \n', np.outer(a, b))
print('np.outer(a.T, b): \n', np.outer(a.T, b))
print('np.outer(b, a): \n', np.outer(b, a))
print()

print('*'*20 + ' k*(A+B) = k*A+k*B ' + '*'*20)
print('3*(a+b): ', 3*(a+b))
print('3*a+3*b: ', 3*a+3*b)

print('*'*20 + ' (k+l)*A = k*A+l*A ' + '*'*20)
print('(2+3)*a: ', (2+3)*a)
print('2*a+3*a: ', 2*a+3*a)

print()
c = b * 2
print('c = b * 2: ', c)

print('*'*20 + ' A*(B*C) = (A*B)*C ' + '*'*20)
print('a*(b*c): ', a*(b*c))
print('(a*b)*c: ', (a*b)*c)

print('*'*20 + ' (A+B)*C = A*C+B*C ' + '*'*20)
print('(a+b)*c: ', (a+b)*c)
print('a*c+b*c: ', a*c+b*c)

print('*'*20 + ' A*(B+C) = A*B+A*C ' + '*'*20)
print('a*(b+c): ', a*(b+c))
print('a*b+a*c: ', a*b+a*c)

print()
print('Задание № 5.1b: Вычислите (5E_), где Е – единичная матрица размера 5х5.')
e = np.identity(5)
print('Е – единичная матрица размера 5х5:\n', e)
a = 5*e
print('Матрица (5E):\n', a)
a_ = np.linalg.inv(a)
print('Обратная матрица (5E_):\n', a_)
print('Проверка свойства обратной матрицы A*A_=E:\n', np.dot(a, a_))

print()
print('=*'*50)
print('Задание № 5.2: Вычислите определитель.')
a = np.array([[1, 2, 3], [4, 0, 6], [7, 8, 9]])
print(a)

d = np.linalg.det(a)
print('det(a) = ', d)

print()
print('=*'*50)
print('Задание № 5.3a: Вычислите матрицу, обратную данной.')
a_ = np.linalg.inv(a)
print(a_)
print()
print(np.dot(a, a_))

print()
print('=*'*50)
print('Задание № 5.3b: Приведите пример матрицы 4х4, ранг которой равен 1.')
b = np.array([[1, 2, 3, 4], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
print(b)
print('det(b) = ', np.linalg.det(b))
rank = np.linalg.matrix_rank(b)
print('rank(b) = ', rank)

print()
print('=*'*50)
print('Задание № 5.4: Вычислите скалярное произведение двух векторов.')
a = np.array([1, 5])
b = np.array([2, 8])
print(f'Cкалярное произведение векторов a={a} и b={b}:')
print('np.dot(a, b): ', np.dot(a, b))
print('np.dot(a.T, b): ', np.dot(a.T, b))
print('np.inner(a, b): ', np.inner(a, b))
s = a[0]*b[0]+a[1]*b[1]
print('a0*b0+a1*b1: ', s)

print()
print('Квадрат длины вектора: np.dot(a, a) = ', np.dot(a, a))
long_a = np.linalg.norm(a)
print('Длина вектора: np.linalg.norm(a) = ', long_a)
print('Квадрат длины вектора: np.dot(b, b) = ', np.dot(b, b))
long_b = np.linalg.norm(b)
print('Длина вектора: np.linalg.norm(b) = ', long_b)
print('cos@ = ', s/(long_a*long_b))

X, Y = np.array([0, 0, a[0]]), np.array([0, 0, a[1]])
U, V = np.array([a[0], b[0], b[0]-a[0]]), np.array([a[1], b[1], b[1]-a[1]])

plt.quiver(X, Y, U, V, angles='xy', scale_units='xy', scale=1)

plt.xlim(-1, 2)
plt.ylim(-1, 8)
plt.grid(True)
plt.show()

print()
print('=*'*50)
print('Задание № 5.5: Вычислите смешанное произведение трех векторов.')
a = np.array([1, 5, 0])
b = np.array([2, 8, 7])
c = np.array([7, 1.5, 3])
v = np.cross(a, b)
print('(a x b) = ', v)
print('(a x b)*c = ', np.inner(v, c))
w = np.cross(b, c)
print('(b x c) = ', w)
print('(b x c)*a = ', np.inner(w, a))

X, Y, Z = np.array([0, 0, 0]), np.array([0, 0, 0]), np.array([0, 0, 0])
U, V, W = np.array([a[0], b[0], c[0]]), np.array([a[1], b[1], c[1]]), np.array([a[2], b[2], c[2]])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.quiver(X, Y, Z, U, V, W)

ax.set_xlim([0, 7])
ax.set_ylim([0, 8])
ax.set_zlim([0, 7])
ax.grid(True)
plt.show()
