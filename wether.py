# Задача:
# Создайте массив из 365 случайных чисел, представляющих дневную температуру (например, от −10 до 35).
# Найдите:
# Среднюю температуру за год.
# Количество дней с температурой выше 25.
# Самую длинную последовательность дней, когда температура была ниже 0.
# Визуализируйте:
# Линейный график температуры по дням.
# Гистограмму распределения температуры.
# Подсветку "холодных" и "жарких" дней на линейном графике.
import matplotlib.pyplot as plt
import numpy as np
import itertools

a = np.random.randint(-10, 35, 365) #sozdaem tp

sred = np.sum(a) // 365 #srednyaya tp

hot_days = np.sum(a > 25) #vishe 25

#nizhe 0
cold_days = np.where(a < 0)[0]
if len(cold_days) > 0:
    diffs = np.diff(cold_days)
    max_cold_days = max(sum(1 for _ in g) for k, g in itertools.groupby(diffs) if k == 1) + 1
else:
    max_cold_days = 0

#graphic po dnyam
plt.figure(figsize=(12, 6))
plt.plot(a, label='Температура')

#podsvetka
cold_days = a < 0
hot_days_indices = np.where(a > 25)[0]
plt.scatter(np.where(cold_days)[0], a[cold_days], color='blue', label='Холодные дни', s=20)
plt.scatter(hot_days_indices, a[hot_days_indices], color='red', label='Жаркие дни', s=20)

# Гистограмма
plt.figure(figsize=(8, 6))
plt.hist(a, bins=20, edgecolor='pink')


print(a)
print(sred)
print(max(sum(1 for a in v) for _,v in itertools.groupby(a)))
plt.show()
