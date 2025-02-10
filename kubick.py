# Задача:
# Смоделируйте 1000 бросков игрального кубика.
# Найдите:
# Сколько раз выпадало каждое значение (от 1 до 6).
# Вероятность выпадения каждого значения.
# Максимальное количество подряд выпавших одинаковых значений.
# Визуализируйте результаты в виде гистограммы.

import random as ran
import matplotlib.pyplot as plt
import numpy as np
import itertools

#делаем список
x = []
count = [0, 0, 0, 0, 0, 0]
for i in range (1000):
    x.append(ran.randint(1, 6))

#сортируем списко
y = x.copy()
y.sort()

#считаем значения
c = 0
b = 1
for i in range(1000):
    if y[i] == b:
        count[c] += 1
    else:
        count[y[i]-1] += 1
        b += 1
        c += 1

#считаем вероятнлости
ver = []
for i in range(6):
    ver.append(count[i]/1000)


print(x)
print(y)
print(count)
print(ver)
print(max(sum(1 for x in v) for _,v in itertools.groupby(x)))

#

plt.hist(y, color = 'pink', bins = int(180/5))


# Add labels
plt.title('броски кубика')
plt.xlabel('значения')
plt.ylabel('количество')

plt.show()