#Вариант 10

#Задание 1
N=int(input('Введите кол-во элементов в массиве'))
x=[]
y=[]
for i in range (N):
   print('Введите i элемент:')
   x.append(int(input()))
print('Массив: ',x)
for i in range (N):
    y = [item for item in set(x) if x.count(item) > 1]
if not y:
        print('Повторяющихся элеиентов нет')
else:
        print('Повторяющиеся элементы: ',y)

#Задание 2
x=[2,45,13,9,34,19,3,67,117,14,3,4,111,12,11]
y=[]
print('Первоначальный массив: ',x)
for i in range (15):
    if (x[i]<10):
        x[i]=0
        y.append(x[i])
    if (x[i]>10) and (x[i]<20):
         y.append(x[i])
    if (x[i]>20):
        x[i]=1
        y.append(x[i])
print('Измененный массив: ',y)