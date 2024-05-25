"""def add(a,b):
    return lambda c, d: a+b+c+d

print(add(1,2)(3,4))"""



"""sonlar = [3,4,5,6,1]
result  = list(map(lambda x: x**3, sonlar))
print(result)"""

"""
result = ['hdc','123','wdqd','dscc', '123']

def tekshirish(a):
    if a.isdigit():
        return True
    return False


a = list(map(tekshirish, result))

print(a)"""


"""a  =[ 4,2,3,4,6]
b  = [20,30,43,22]

result = list(map(lambda x,y: x +y , a,b))
print(result)"""

"""
a  = [30,20,10,4]

result = list(map(lambda x: x>10,a))
print (result)"""

# filtr :har birini boolinga tiqadi  va ture qaytarganlarini qoldiradi qolgani ochiradi
# map : 



#homrwork 1

"""a = [1,2,3]
b = [4,5,6]
c = [7,8,9]

result = list(map(lambda x ,y, z: x + y + z , a, b, c))

print(result)"""

#homework 2

"""color = ['red', 'blue', 'yellow', 'green']

result = list(map(list , color))
print(result)"""

#homework 3

"""chards = {'a','b','c','d','e','f'}

result = set(map(lambda x: (x.upper(), x.lower()), chards))
print(result)"""

#homework 4

"""a = [6,5,3,9]
b = [0,1,7,7]

result = list(map(lambda x,y: (x + y , x - y), a ,b))
print(result)"""

#homework 5

"""student_data = [('alberto framse', '15/05/2002','35kg'), ('gino misnel','17/05/2002','37kg'), ('royan parkes','16/02/1999','39kg'),('eisha hinton', '25/09/1998','35kg')]
name = list(map(lambda x: x[0],student_data))
date = list(map(lambda x: x[1],student_data))
kg = list(map(lambda x: x[2],student_data))
print(name)
print(date)
print(kg)"""

#homework 6

"""a = [1,2,3,4,5,6,7,8]
b = [2,2,3,1,2,6,7,9]

result = list(filter(lambda x: x[0]==x[1] , zip(a,b )))

print(len(result))"""














































































































































































































































































































































































































