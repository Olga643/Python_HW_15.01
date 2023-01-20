# Напишите программу, которая найдёт произведение пар чисел списка.
#  Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random

# первое решение

'''my_list = []

for i in range(5):
    my_list.append(int(random.uniform(0, 10)))
print(my_list)

x = 1
new_list = []


for i in range (len(my_list) // 2 + 1):
    x = my_list[i] * my_list[len(my_list) - i - 1]
    new_list.append(x)

print(new_list)'''

# второе решение
my_list = list((random.randint(1, 10) for i in range (5)))
print(my_list)

new_len = len(my_list) // 2 + 1 if len(my_list) % 2 != 0 else len(my_list) // 2
new_list = [my_list[i] * my_list[len(my_list) - i - 1] for i in range(new_len)]

print(new_list)