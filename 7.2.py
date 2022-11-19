def naoborot(A):
    reverse = A.split(" ")[::-1]

    return ' '.join(reverse)

a = str(input('Введите строку:'))
print(naoborot(a))
