import math
import random

# Описание "INKBLOT"
print(" " * 26 + "INKBLOT")
print(" " * 20 + "CREATIVE COMPUTING")
print(" " * 18 + "MORRISTOWN, NEW JERSEY")
print("\n" * 3)

# Выбор числа эллипсов (5 до 12)
M = random.randint(5, 12)

# Массив для эллипсов
A = [[0] * 14 for _ in range(M + 1)]

# Генерация параметров эллипсов
for L in range(1, M + 1):
    A[L][1] = 34 * random.random()
    A[L][2] = 80 * random.random()
    A[L][3] = (15 * random.random() + 2) ** 2
    A[L][4] = (15 * random.random() + 2) ** 2
    T = math.pi * random.random()
    A[L][5] = math.cos(T) ** 2
    A[L][6] = math.sin(T) ** 2
    A[L][7] = math.cos(T) * math.sin(T)
    A[L][8] = A[L][1] ** 2 * A[L][6]
    A[L][9] = A[L][1] ** 2 * A[L][5]
    A[L][10] = A[L][1] * A[L][7]
    A[L][11] = -2 * A[L][1] * A[L][6]
    A[L][12] = -2 * A[L][1] * A[L][5]
    A[L][13] = A[L][6] / A[L][4] + A[L][5] / A[L][3]

# Границы (определение "$$$$")
B = "$" * 36
print(B + B)
print(B + B)

# Луп по Y для построения линий
for Y in [79.9 - 1.6 * i for i in range(50)]:
    A_line = "$" + " " * 34

    for E in range(1, M + 1):
        Y1 = Y - A[E][2]
        Y2 = Y1 ** 2
        Y3 = Y1 * A[E][10]
        Y4 = Y1 * A[E][7]
        B_val = (A[E][12] + Y4) / A[E][3] + (-Y4 + A[E][11]) / A[E][4]
        C_val = (
            (Y2 * A[E][6] + A[E][9] - Y3) / A[E][3]
            + (Y2 * A[E][5] + A[E][8] + Y3) / A[E][4]
            - 1
        )

        # Корни квадратного уравнения
        R = B_val ** 2 - 4 * A[E][13] * C_val
        if R < 0:
            continue

        R = math.sqrt(R)
        R1 = int(-(B_val + R) / (2 * A[E][13]) + 1)
        R2 = int((R - B_val) / (2 * A[E][13]))

        if R1 > 34 or R2 < 1:
            continue

        R1 = max(R1, 1)
        R2 = min(R2, 34)

        for J in range(R1 + 1, R2 + 1):
            A_line = A_line[:J] + "$" + A_line[J + 1:]

    # Вывод строки изображения
    print(A_line, end="")
    print(A_line[::-1])

# Нижняя граница
print(B + B)
print(B + B)
input("Нажмите Enter, чтобы выйти...")
