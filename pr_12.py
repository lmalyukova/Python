#Блок А №2
def ost(a,b):
    print(a%b)
ost(5,10)

#Блок Б №3
def poisk():
    k = [int(i) for i in input('Введите последовательность:').split() if int(i)]
    print(*k[::2])
poisk()