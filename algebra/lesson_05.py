import numpy as np
from scipy.special import factorial
import matplotlib.pyplot as plt
import itertools

print('Задание № 1: Модель выпадения поля в рулетке (с учетом поля зеро).')
for i in range(0, 10):
    a = input()
    num = np.random.randint(0, 37)
    if num == 0:
        print("green")
    elif num in (1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36):
        print("red")
    else:
        print("black")
print('*' * 100)
# ==========================================================================================

print('Задание № 2.1a: Проверка теоремы сложения вероятности на примере рулетки.')
r, b, z = 0, 0, 0
n = 100
for i in range(0, n):
    num = np.random.randint(0, 37)
    if num == 0:
        z += 1
    elif num in (1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36):
        r += 1
    else:
        b += 1
Pz = z / n
Pr = r / n
Pb = b / n
print(f'zero={z}, red={r}, black={b}')
print(f'Pz={Pz}, Pr={Pr}, Pb={Pb}, (Pz + Pr + Pb)={Pz + Pr + Pb}')
print('*' * 100)
# ==========================================================================================

print('Задание № 2.1b: Проверка теоремы умножения вероятности на примере рулетки.')
r, b, m = 0, 0, 0
n = 100
for i in range(0, n):
    num = np.random.randint(0, 37)
    if num == 1:
        m += 1
    elif num in (1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36):
        r += 1
    else:
        b += 1
Pm = m / n
Pr = r / n
Pb = b / n
print(f'num_1={m}, red={r}, black={b}')
print(f'Pm={Pm}, Pr={Pr}, Pb={Pb}, (Pm * Pr)={Pm * Pr}')
print('*' * 100)
# ==========================================================================================

print('Задание № 2.2: Гистограмма распределения случайной суммы десяти выборок случайных чисел.')
all_sums = []
for i in range(11):
    x = np.random.rand(10)
    all_sums.append(sum(x))
num_bins = 10
n, bins, patches = plt.hist(all_sums, num_bins)
print(n)
plt.xlabel('summa')
plt.ylabel('Probability')
plt.title('Histogram')
plt.show()
print('*' * 100)
# ==========================================================================================

print('Задание № 3.1: Рассчёт вероятностей через биномиальное распределение.')
kol, long = 0, 10000
n = 4       # количество испытаний (случайных векторов из 0 и 1 по long элементов)
k = 2       # количество успехов (1) среди n-испытаний
x = [0 for _ in range(long)]
# генерация n-х случайных векторов из 0 и 1 по long элементов
a = [np.random.randint(0, 2, long) for _ in range(0, n)]

for i in range(0, n):
    x += a[i]
for i in range(0, long):
    if x[i] == k:
        kol += 1

# вероятность выпадения среди n-испытаний k-успехов по формуле Бернулли
Ck = factorial(n) / (factorial(k) * factorial(n - k))
print(f'Для n={n} и k={k} Ck={Ck}')
P1 = (0.5 ** k) * (0.5 ** (n - k)) * Ck  # по формуле Бернулли
print(f'Количество выпадений успеха: k={kol}\nДлина последовательности: long={long}\n'
      f'Относительная частота успеха: k/long={kol/long}\nВероятность выпадения успеха: P1={P1}')
print('*' * 100)
# ==========================================================================================

print('Задание № 4: Генерация возможных вариантов размещений, перестановок и сочетаний для значений n и k.')
i = 0
n = 3
pos = '01'
k = len(pos)
print(f'Все возможные размещения чисел "{pos}" в последовательности длиной n={n}')
for p in itertools.product(pos, repeat=n):
    print(''.join(p))
    i += 1
print(i)
print(f'Количество размещений c повторениями (A=n^k): A={k ** n}')
print('*' * 100)

i = 0
pos = '0123'
n = len(pos)
k = 2
print(f'Все возможные размещения {k}-х первых чисел в последовательности "{pos}" длиной n={n}')
for p in itertools.permutations(pos, k):
    print(''.join(p))
    i += 1
print(i)
print(f'Количество размещений без повторений (A=n!/(n-k)!):A={factorial(n) / factorial(n - k)}')
print('*' * 100)

i = 0
pos = '0124'
n = len(pos)
k = n
print(f'Все возможные перестановки чисел {pos} в последовательности длиной n={n}')
for p in itertools.permutations(pos, k):
    print(''.join(str(x) for x in p))
    i += 1
print(i)
print(f'Количество перестановок без повторений (А=n!): A={factorial(n)}')
print('*' * 100)

i = 0
pos = '01234'
n = len(pos)
k = 3
print(f'Все возможные сочетания {k}-х первых чисел с другими из последовательности {pos}')
for p in itertools.combinations(pos, k):
    print(''.join(p))
    i += 1
print(i)
print(f'Количество сочетаний без повторений (С=n!/(k!*(n-k)!): '
      f'C={factorial(n) / (factorial(k) * factorial(n - k))}')
print('*' * 100)
# ==========================================================================================

print('Задание № 5: Расчёт коэффициента корреляции x и y для линейной регрессии.')
# построение графика линейной регрессии
n = 100
r = 0.7
x = np.random.rand(n)
y = r * x + (1 - r) * np.random.rand(n)
plt.plot(x, y, 'o')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)

# расчёт коэффициентов a, b для прямой y=a*x+b, выражающей линейную регрессию
a = (np.sum(x) * np.sum(y) - n * np.sum(x * y)) / (np.sum(x) * np.sum(x) - n * np.sum(x * x))
b = (np.sum(y) - a * np.sum(x)) / n

# расчёт коэффициента корреляции x и y
Xm = np.sum(x) / len(x)
Ym = np.sum(y) / len(y)
R = np.sum((x - Xm) * (y - Ym)) / np.sqrt(np.sum((x - Xm) ** 2) * np.sum((y - Ym) ** 2))
print(f'a={a}, b={b}')
print(f'Коэффициент корреляции: R={R}')

# вариант расчёта коэффициентов a, b, R с помощью встроенных библиотек
A = np.vstack([x, np.ones(len(x))]).T
a1, b1 = np.linalg.lstsq(A, y)[0]
R1 = np.corrcoef(x, y)
print(f'a1={a1}, b1={b1}')
print(f'Коэффициент корреляции: R1=\n{R1}')

plt.plot([0, 1], [b, a + b])
plt.show()
