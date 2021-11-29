#
# Напишите 3 функции
#
# 1-ая должна принимать список.
# Добавлять в этот список элементы 'Element', 'start', 'finish'.
# Все элементы первоначального списка должны находиться между элементами 'start', 'finish'
#
# Пример:
#
# print(func(['hello', 5, 'John', ])) # ['Element', 'start', 'hello', 5, 'John', 'finish']
# 2-ая должна принимать производное количество аргументов и возвращать словарь,
# где ключами являются принятые аргументы, а значениями числа от 1 до количества принятых аргументов
#
# Пример:
#
# print(func('x', 5, 'John')) # {'x':1, 5:2, 'John':3}
# 3-я должна принять кортеж. Превращать этот кортеж в список и, используя анономные функции, выдавать нам на выход 2 списка.
# 1-ый список должен состоять из всех чётных чисел введённого кортежа.
# 2-ой со всеми элементами введённого кортежа возведёнными в квадратную степень
#
# Пример:
# a, b = func((1,2,3,4,5)) print(a) #[2, 4] print(b) #[1, 4, 9, 16, 25

# Первая функция
lst = [ 'Element', 'start', 'finish']

def append_str(str_lst):
    lst.insert(2, str_lst[2])
    lst.insert(2, str_lst[1])
    lst.insert(2,str_lst[0])
    return lst

print(append_str(['hello', 5, 'John']))


#
# append_str('John')
# append_str(5)
# append_str('hello')
# print(lst)


# Вторая функция

def func(lst):
    a = 0
    dic ={}
    for i in lst:
        a = a + 1
        dic.update({i:a})
    print(dic)

lst = ['x', 5, 'John',]
dict = func(lst)

# Третья Функция

def tuple_pep(i):
    a = list(filter(lambda x:x % 2 == 0, i))
    b = list(map(lambda x:x **2,i))
    print(a)
    print(b)
tuple_pep((1,2,3,4,5))