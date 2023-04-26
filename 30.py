# Задача 30: Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

a = int(input('Enter the initial number: '))
d = int(input('Enter the step: '))
c = int(input('Enter the size: '))

for i in range(1,c+1):
    result = a + (i-1) * d
    print(result) 