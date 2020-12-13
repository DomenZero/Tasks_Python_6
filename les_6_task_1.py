'''
1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:
a. выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
b. написать 3 варианта кода (один у вас уже есть);
проанализировать 3 варианта и выбрать оптимальный;

c. результаты анализа (количество занятой памяти в вашей среде разработки) вставить в виде комментариев в файл с кодом.
Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;
d. написать общий вывод: какой из трёх вариантов лучше и почему.
'''
'''
Задача 4 из урока 3
Определить, какое число в массиве встречается чаще всего

Test1 
test = [1, 2, 3, 4, 5, 6]

'''
import random
import cProfile
import sys


def show_size(x, level=0):
    sum_size = sys.getsizeof(x)
    # print('Переменные занимают', sum_size)
    # print('\t' * level, f'type={x.__class__},size={sys.getsizeof(x)},object={x}')  # тип объекта, значение байт

    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for xx, value in x.items():
                show_size(xx, level + 1)
                show_size(value, level + 1)
                sum_size = sum_size + sys.getsizeof(xx) + sys.getsizeof(value)
        elif not isinstance(x, str):
            for xx in x:
                show_size(xx, level + 1)
                sum_size = sum_size + sys.getsizeof(xx)
    return sum_size


# Решение 1
def detect(num):
    ln = len(num) - 1
    ch = 0
    first = num[0]
    k = 0
    max_am = 0
    max_ch = 0
    for i in range(ln):
        first = num[i]
        if num[i] == first and first != 'n':
            for i, item in enumerate(num[:]):
                if num[i] == first and num[i] != 'n':
                    ch += 1
                    num[i] = 'n'
            if max_am < ch:
                max_am = ch
                max_ch = first
            k += 1
            ch = 0

    sum_size_1 = show_size(ln)
    sum_size_1 = sum_size_1 + show_size(ch)
    sum_size_1 = sum_size_1 + show_size(first)
    sum_size_1 = sum_size_1 + show_size(k)
    sum_size_1 = sum_size_1 + show_size(max_am) + show_size(max_ch) + show_size(num)
    print(f'Код 1. Задействовано памяти: {sum_size_1}')

    return max_ch, max_am


test = [1, 2, 3, 4, 5, 6]
# test=[random.randint(2,5) for _ in range(10)]
detect(test)
'''
Переменные занимают 28
 type=<class 'int'>,size=28,object=5
Переменные занимают 24
 type=<class 'int'>,size=24,object=0
Переменные занимают 28
 type=<class 'int'>,size=28,object=5
Переменные занимают 28
 type=<class 'int'>,size=28,object=5
Переменные занимают 28
 type=<class 'int'>,size=28,object=1
Переменные занимают 28
 type=<class 'int'>,size=28,object=1
Переменные занимают 104
 type=<class 'list'>,size=104,object=['n', 'n', 'n', 'n', 'n', 6]
Переменные занимают 50
	 type=<class 'str'>,size=50,object=n
Переменные занимают 50
	 type=<class 'str'>,size=50,object=n
Переменные занимают 50
	 type=<class 'str'>,size=50,object=n
Переменные занимают 50
	 type=<class 'str'>,size=50,object=n
Переменные занимают 50
	 type=<class 'str'>,size=50,object=n
Переменные занимают 28
	 type=<class 'int'>,size=28,object=6
Код 1. Задействовано памяти: 546
'''

# Решение 2
def detect2(num):
    u_num = {i: 0 for i in set(num)}
    for i in num:
        u_num[i] += 1

    max_x = 0
    for key, item in u_num.items():
        if item > max_x:
            max_ch = key
            max_x = item

    sum_size_1 = show_size(u_num)
    sum_size_1 = sum_size_1 + show_size(i)
    sum_size_1 = sum_size_1 + show_size(num)
    sum_size_1 = sum_size_1 + show_size(u_num)
    sum_size_1 = sum_size_1 + show_size(max_x) + show_size(key) + show_size(item) + show_size(max_ch)
    print(f'Код 2. Задействовано памяти: {sum_size_1}')
    return max_ch


detect2(test)
'''
Переменные занимают 232
 type=<class 'dict'>,size=232,object={6: 1, 'n': 5}
Переменные занимают 28
	 type=<class 'int'>,size=28,object=6
Переменные занимают 28
	 type=<class 'int'>,size=28,object=1
Переменные занимают 50
	 type=<class 'str'>,size=50,object=n
Переменные занимают 28
	 type=<class 'int'>,size=28,object=5
Переменные занимают 28
 type=<class 'int'>,size=28,object=6
Переменные занимают 104
 type=<class 'list'>,size=104,object=['n', 'n', 'n', 'n', 'n', 6]
Переменные занимают 50
	 type=<class 'str'>,size=50,object=n
Переменные занимают 50
	 type=<class 'str'>,size=50,object=n
Переменные занимают 50
	 type=<class 'str'>,size=50,object=n
Переменные занимают 50
	 type=<class 'str'>,size=50,object=n
Переменные занимают 50
	 type=<class 'str'>,size=50,object=n
Переменные занимают 28
	 type=<class 'int'>,size=28,object=6
Переменные занимают 232
 type=<class 'dict'>,size=232,object={6: 1, 'n': 5}
Переменные занимают 28
	 type=<class 'int'>,size=28,object=6
Переменные занимают 28
	 type=<class 'int'>,size=28,object=1
Переменные занимают 50
	 type=<class 'str'>,size=50,object=n
Переменные занимают 28
	 type=<class 'int'>,size=28,object=5
Переменные занимают 28
 type=<class 'int'>,size=28,object=5
Переменные занимают 50
 type=<class 'str'>,size=50,object=n
Переменные занимают 28
 type=<class 'int'>,size=28,object=5
Переменные занимают 50
 type=<class 'str'>,size=50,object=n
Код 2. Задействовано памяти: 1298
'''
# Решение 3
def detect3(num):
    dict = {}
    for item in num:
        if item in dict.keys():
            dict[item] += 1
        else:
            dict[item] = 1
    result = max(dict, key=lambda k: dict[k])
    sum_size_1 = show_size(num)
    sum_size_1 = sum_size_1 + show_size(dict)
    sum_size_1 = sum_size_1 + show_size(item)
    print(f'Код 3. Задействовано памяти: {sum_size_1}')
    return result


detect3(test)
'''
Переменные занимают 104
 type=<class 'list'>,size=104,object=['n', 'n', 'n', 'n', 'n', 6]
Переменные занимают 50
	 type=<class 'str'>,size=50,object=n
Переменные занимают 50
	 type=<class 'str'>,size=50,object=n
Переменные занимают 50
	 type=<class 'str'>,size=50,object=n
Переменные занимают 50
	 type=<class 'str'>,size=50,object=n
Переменные занимают 50
	 type=<class 'str'>,size=50,object=n
Переменные занимают 28
	 type=<class 'int'>,size=28,object=6
Переменные занимают 232
 type=<class 'dict'>,size=232,object={'n': 5, 6: 1}
Переменные занимают 50
	 type=<class 'str'>,size=50,object=n
Переменные занимают 28
	 type=<class 'int'>,size=28,object=5
Переменные занимают 28
	 type=<class 'int'>,size=28,object=6
Переменные занимают 28
	 type=<class 'int'>,size=28,object=1
Переменные занимают 28
 type=<class 'int'>,size=28,object=6
Код 3. Задействовано памяти: 776
'''

''' 
Test 2: test=[random.randint(2,5) for _ in range(10)]
Код 1. Задействовано памяти: 870
Код 2. Задействовано памяти: 1510
Код 3. Задействовано памяти: 1044
Результат: 
Первый код более эффективен по памяти, т.к. не использует не dict, не множества
Третий код использует dict и он по памяти выигрывает перед set
'''