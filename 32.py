# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
from random import randint

size = int(input('Enter size of the list: '))
min = int(input('Enter min in the range: '))
max = int(input('Enter max in the range: '))

list =[]
for i in range(size):
    list.append(randint(0,9))
    print(i, end='  ')
print(' ')
print(list)

for i in range(len(list)):
    if list[i] >=min and list[i] <= max:
        print(i, end=' ')
