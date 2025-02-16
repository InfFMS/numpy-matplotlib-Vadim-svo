# Задача:
# Создайте игровое поле для "Сапёра" размером 10×10.
# Поле должно быть представлено в виде двумерного массива.
# Разместите 15 мин случайным образом (обозначьте их числом −1).
# Для каждой клетки без мины подсчитайте количество мин в соседних клетках.
# Визуализируйте:
# Само поле (где мины выделены красным).
# Поле с числами, где указано количество мин вокруг каждой клетки (для наглядности).

import matplotlib.pyplot as plt
import numpy as np

pole = np.zeros((10, 10), dtype=int)

mines = np.random.choice(10 * 10, 15, replace=False)
row_indices = mines // 10
col_indices = mines % 10
pole[row_indices, col_indices] = -1

for i in range(10):
    for j in range(10):
        if pole[i, j] != -1:
            count = 0
            for x in range(max(0, i - 1), min(10, i + 2)):
                for y in range(max(0, j - 1), min(10, j + 2)):
                    if pole[x, y] == -1:
                        count += 1
            pole[i, j] = count

plt.figure(figsize=(8, 8))
plt.imshow(pole, cmap='Reds_r', interpolation='nearest')

print(pole)
plt.show()
