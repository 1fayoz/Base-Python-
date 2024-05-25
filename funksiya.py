"""def greet():
    print('hello world')

print(greet())"""


#def add(a: int,b: int) -> int:
"""
    this function for add two nombers.
    it returns integer number
    """
#    return a + b
#x = add(1,2)
#print(x)


"""def my_func(fname: str, age = 17):
    print(fname + ' fayoz', age)
my_func('aziz')
my_func('men', 20)
my_func('diyor', 50)"""


"""def is_perfect(son: int):
    sum = 1
    for i in range(2, son):
        if son % i == 0:
            sum += i
    return sum == son

def perfect_number(son: int):
    result = []
    for i in range(2, son):
        if is_perfect(i):
            result.append(i)
    return result
print(perfect_number(100))"""



#homework 2
"""
def square(son: int):
    return son ** 2
print(square(12))"""



#homework 3

"""def list1(son):
    result = []
    for i in range(1, son+1):
        result.append(i)
    return result
print(list1(7))"""

#homework 4

"""def big(son1: int, son2: int, son3: int):
    if son1 > son2 and son1 > son3:
        return son1
    elif son2 > son1 and son2 > son3:
        return son2
    elif son3 > son2 and son3 > son1:
        return son3

print(big(10,20,30))"""

#homework 5











# intermediate homework 1

"""def teskari_matn(matn):
    index = len(matn) - 1
    while index > 0 :
        print (matn[index], end="")
        index -= 1
print(teskari_matn('fayoz , aziz '))"""   


#intermediate homework 2

"""def ajratish(matn):
    kotta = 0
    kichik = 0
    for i in matn:
        if i.isupper() :
            kotta += 1
        elif i.islower():
            kichik += 1
    return kotta, kichik




men = 'FAYOZ  fayoz pyhton tillida yaratilgan narsa'
ka , ki = ajratish(men)
print(ka , ki)"""


#intermediate homework 3

def ispalendron(matn):
    start =  0
    end = len(matn) - 1
    while start < end :
        matn[start] != matn[end]
        return False
        start += 1
        end -= 1
    return True

print(ispalendron("madam)") )   













































































































































































































































































