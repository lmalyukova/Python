def poisk(N, A, B, C):
    s = 0
    for i in range(100, N):
        if i % 10 == (A or B or C) and i % 100 // 10 == (A or B or C) and i // 100 == (A or B or C):
            s += 1
    return s


N = int(input('Введите число больше 210 и меньше 231:'))
while not 210 < N < 231:
    N = int(input('Введите число больше 210 и меньше 231:'))
a = int(input('Введите первое цифру:'))
b = int(input('Введите вторую цифру:'))
c = int(input('Введите третью цифру:'))
print(poisk(N, a, b, c))
