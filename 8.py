def maxel(m, n, d):
    mx = []
    for row in d:
        if row == sorted(row) or row == sorted(row, reverse=True):
            mx.append(max(row))
    return mx


M = int(input('Введите число строк:'))
N = int(input('Введите число столбцов:'))
mat = []
for i in range(M):
    bat = []
    for j in range(N):
        bat.append((int(input('Введите элемент матрицы:'))))
    mat.append(bat)
for i in range(M):
    for j in range(N):
        print(mat[i][j], end=' ')
    print()
print(maxel(M, N, mat))
