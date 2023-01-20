#Задайте список из n чисел последовательности (1 + 1/n)**n, выведеите его на экран, 
#  а так же сумму элементов списка. 
# Пример: 
# Для n=4 -> [2, 2.25, 2.37, 2.44] 
# Сумма 9.06 
 
#первое решение

'''number = int(input('Введите число: ')) 
 
my_list = [] 
 
x = 1 
sum = 0 
 
for i in range(1, number + 1): 
 
  x = round(((1 + 1 / i)** i),2) 
  my_list.append(x) 
  sum = sum + x 
 
print(*my_list, sep = ', ') 
print(f'Сумма элементов = {sum}')'''

# второе решение

n = int(input('Введите число: '))
my_list = [round(((1 + 1 / n)**n), 2) for n in range(1, n + 1)]
print(my_list)

print(f'Сумма элементов = {sum(my_list)}')