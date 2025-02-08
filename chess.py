# Задача:
# Создайте шахматную доску размером 8×8, где чёрные клетки обозначены числом 1, а белые — 0.
# Укажите координаты клетки, где находится ферзь, например, [4,4].
# Определите клетки, которые атакует ферзь (в строке, столбце и диагоналях).
# Визуализация: Используйте тепловую карту (imshow), чтобы показать шахматную доску. Отметьте положение ферзя и атакуемые клетки цветами.

import matplotlib.pyplot as plt
import numpy as np

#создаём доску
bruh, ferz = plt.subplots()
x = np.array([[1,0,1,0,1,0,1,0],[0,1,0,1,0,1,0,1],[1,0,1,0,1,0,1,0],[0,1,0,1,0,1,0,1],[1,0,1,0,1,0,1,0],[0,1,0,1,0,1,0,1],[1,0,1,0,1,0,1,0], [0,1,0,1,0,1,0,1]])
plt.imshow(x, cmap = 'hot', interpolation='nearest')
col_labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
row_labels = range(1, 9)
plt.xticks(range(8), col_labels)
plt.yticks(range(8), row_labels)

#вводим координаты ферзя
X_ferz = int(input())
Y_ferz = int(input())



#считаем где он и куда может атаковать
for i in range(8):
    #x[Y_ferz][i] = 6
    ferzat = plt.Circle((int(Y_ferz),int(i)), 0.314, facecolor='pink')
    ferz.add_patch(ferzat)
    #x[i][X_ferz] = 6
    ferzat = plt.Circle((int(i), int(X_ferz)), 0.314, facecolor='pink')
    ferz.add_patch(ferzat)
    #x[abs(Y_ferz-i)][abs(X_ferz-i)] = 6
    ferzat = plt.Circle((int(Y_ferz-i), int(X_ferz-i)), 0.314, facecolor='pink')
    ferz.add_patch(ferzat)
    ferzat = plt.Circle((int(Y_ferz+i), int(X_ferz+i)), 0.314, facecolor='pink')
    ferz.add_patch(ferzat)
    ferzat = plt.Circle((int(Y_ferz - i), int(X_ferz + i)), 0.314, facecolor='pink')
    ferz.add_patch(ferzat)
    ferzat = plt.Circle((int(Y_ferz + i), int(X_ferz - i)), 0.314, facecolor='pink')
    ferz.add_patch(ferzat)

ferzat = plt.Circle((int(Y_ferz), int(X_ferz)), 0.414, facecolor='brown')
ferz.add_patch(ferzat)



plt.show()