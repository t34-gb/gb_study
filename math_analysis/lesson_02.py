from itertools import product

print('Задание. Даны три множества A,B и C. Необходимо выполнить все изученные виды бинарных '
      'операций над всеми комбинациями множеств.')

A = {-1, 0, 1, 3, 5}
B = {-2, 0, 2, 3, 8}
C = set('ab')
print('Множество A: ', A)
print('Множество B: ', B)
print('Множество C: ', C)

print('*'*20 + ' Объединение множеств с помощью оператора "|" или функцией union(). ' + '*'*20)
print('A | B: ', A | B)
print('B.union(A): ', B.union(A))
print('A | C: ', A | C)
print('C.union(A): ', C.union(A))
print('C | B: ', C | B)
print('B.union(C): ', B.union(C))

print('*'*20 + ' Пересечение с помощью оператора "&" или функция intersection(). ' + '*'*20)
print('A & B: ', A & B)
print('B.intersection(A): ', B.intersection(A))
print('B & A: ', B & A)
print('A.intersection(B): ', A.intersection(B))
print('C & B: ', C & B)
print('B.intersection(C): ', B.intersection(C))

print('*'*20 + ' Разность с помощью оператора "-" или функция difference(). ' + '*'*20)
print('A - B: ', A - B)
print('A.difference(B): ', A.difference(B))
print('B - A: ', B - A)
print('B.difference(A): ', B.difference(A))
print('C - B: ', C - B)
print('C.difference(B): ', C.difference(B))
print('B - C: ', B - C)
print('B.difference(C): ', B.difference(C))

print('*'*20 + ' Симметричная разность с помощью оператора "^" или функция symmetric_difference(). ' + '*'*20)
print('A ^ B: ', A ^ B)
print('A.symmetric_difference(B): ', A.symmetric_difference(B))
print('B ^ A: ', B ^ A)
print('B.symmetric_difference(A): ', B.symmetric_difference(A))
print('C ^ B: ', C ^ B)
print('C.symmetric_difference(B): ', C.symmetric_difference(B))
print('B ^ C: ', B ^ C)
print('B.symmetric_difference(C): ', B.symmetric_difference(C))

print('*'*20 + ' Обмен значениями множеств с помощью симметричной разности "^" . ' + '*'*20)
A = A ^ B
print('A = A ^ B: ', A)
B = A ^ B
print('B = A ^ B: ', B)
A = A ^ B
print('A = A ^ B: ', A)

print('*'*20 + ' Декартово произведение с помощью itertools.product и без него. ' + '*'*20)
D = {el for el in product(C, B)}
print('D: ', D)
D = {(c, b) for c in C for b in B}
print('D: ', D)
