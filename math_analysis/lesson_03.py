from scipy.special import factorial
import numpy as np
import matplotlib.pyplot as plt

print('Задание: Алгоритм вычисляющий численно предел с точностью sigma.')

sigma = 10**(-7)
print('Требуемая точность: sigma =', sigma)
n = [i for i in range(1, 171)]
y = [(i*factorial(i)**(-1/i)) for i in n]

plt.plot(n, y)
plt.xlabel('n')
plt.ylabel('y')
plt.plot([0, 170], [np.e, np.e], color='red', linewidth=0.75, linestyle="--")
plt.scatter(0, np.e, c='red')
plt.text(0, np.e, f'e', horizontalalignment='right', verticalalignment='top')
plt.title('График функции: y = n/n!^(1/n)')
plt.grid(True)
plt.show()

print('='*200)
print('Алгоритм, использующий формулу Стирлинга для вычисления факториала '
      'при рассчёте предела с точностью sigma.')
n1 = [i for i in range(1, 1500)]
y1 = [(np.e*(2*np.pi*i)**(-1/(2*i))) for i in n1]

plt.plot(n1, y1)
plt.xlabel('n')
plt.ylabel('y')
plt.plot([0, 1500], [np.e, np.e], color='red', linewidth=0.75, linestyle="--")
plt.scatter(0, np.e, c='red')
plt.text(0, np.e, f'e', horizontalalignment='right', verticalalignment='top')
plt.title('График функции: y = n/n!^(1/n) = e*(2*pi*n)^(-1/2n)')
plt.grid(True)
plt.show()

n_max = 11500
lim_sigma = np.e*(2*np.pi*n_max)**(-1/(2*n_max))
lim_sigma1 = np.e*(2*np.pi*(n_max+1))**(-1/(2*(n_max+1)))

while lim_sigma1 - lim_sigma > sigma:
      n_max += 1
      lim_sigma = np.e * (2 * np.pi * n_max) ** (-1 / (2 * n_max))
      lim_sigma1 = np.e * (2 * np.pi * (n_max + 1)) ** (-1 / (2 * (n_max + 1)))

print(f'Численный предел последовательности с точностью sigma = {sigma}\n'
      f'lim_sigma = {lim_sigma} для n(sigma) = {n_max}')

print('='*200)
print('Сравнение алгоритмов, использующихся при рассчёте предела с точностью sigma.')
n_169 = 169*factorial(169)**(-1/169)
print('n_169 =', n_169)
n_170 = 170*factorial(170)**(-1/170)
print('n_170 =', n_170)
print('n_170 - n_169 =', n_170 - n_169)

print('*'*20 + ' С использованием формулы Стирлинга ' + '*'*20)
n_169s = np.e * (2 * np.pi * 169) ** (-1 / (2 * 169))
print('n_169s =', n_169s)
n_170s = np.e * (2 * np.pi * 170) ** (-1 / (2 * 170))
print('n_170s =', n_170s)
print('n_170s - n_169s =', n_170s - n_169s)

y2 = [(np.e*(2*np.pi*i)**(-1/(2*i))) for i in n]

plt.plot(n, y)
plt.plot(n, y2)
plt.xlabel('n')
plt.ylabel('y')
plt.plot([0, 170], [np.e, np.e], color='red', linewidth=0.75, linestyle="--")
plt.scatter(0, np.e, c='red')
plt.text(0, np.e, f'e', horizontalalignment='right', verticalalignment='top')
plt.title('График функции: y = n/n!^(1/n)')
plt.grid(True)
plt.show()