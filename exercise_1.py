# 1 x = str(int(float(5))) = <class 'str'>
# 2 x = 'aa' == 'AA' =  <class 'bool'>
# 3 x = {i: i**2 for i in range(5)} =  <class 'dict'>
# 4 x = set(list((5, 6, 7))) = <class 'set'>
# 5 a = {1: 1, 2: 4, 3: 9} x = a.get(4) = <class 'NoneType'> <class 'dict'>
# 6 x = [].append('j') = <class 'list'>
# 7 for i in range(10): if i < 5: x = 'hello' else: x = 5 = <class 'int'>
# 8 x = input('Enter and integer: ') = <class 'str'>
# 9 a = 5 b = [1, 3, 5, ] x = 'x' a, b, x = x, a, b = <class 'list'>
# 10 def func(x, y=5): return x + y x = func('Jaguar ', 'hunter') = <class 'str'>

def func(x, y=5):

    return x + y
    x = func('Jaguar', 'hunter')

print(type(x))

