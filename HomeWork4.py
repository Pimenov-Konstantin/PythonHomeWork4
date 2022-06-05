# 1. Дан список чисел. Создать список, в который попадают числа,
# описываемые возрастающую последовательность.
# *Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.*
# ***Порядок элементов менять нельзя***
print('')
print('Task2')
nums = [1, 5, 2, 3, 4, 6, 1, 7]

def up(nums):
    ups = [nums[0]]
    for i in nums:
        if i > max(ups):
            ups.append(i)
    return ups
    
print(up(nums))

# 2. Создать и заполнить файл случайными целыми значениями. 
# Выполнить сортировку содержимого файла по возрастанию. 
print('')
print('Task2')
from random import randint

my_filename = 'task2.txt'

my_list = [randint(0,100) for _ in range(randint(0,100))]

print(my_list)

with open(my_filename,'w') as f:
    f.write("\n".join(map(str,my_list)))

my_list = []
with open(my_filename,'r') as f:
    my_list = f.readlines()
    my_list = list(map(int, my_list))
    my_list.sort()

with open(my_filename,'w') as f:
    f.write("\n".join(map(str,my_list)))

    print(my_list)