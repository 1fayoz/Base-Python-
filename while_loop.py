"""for i in range(1,6):
    print(i)"""




"""i = 1

while i < 6 :
    print(i)
    i += 1"""

#teskarisi

"""for i in range(5 , 0, -1):
    print(i)"""


"""i = 5
while i > 0:
    print(i)
    i -= 1 """


"""a = ['apple', 'banana', 'cherry', 'new']

start = 0
end = len(a)
while start < end:
    print(a[end-1])
    end -= 1"""

#  

"""a = 'Hello world'

b = 0
c = len(a)
while b < c:
    print(a[b])
    b += 1"""



"""i = 2

while i < 21 :
    print(i)
    i += 3
else:
    print('sikl yakunlandi')"""




import random

computer_think  = random.randrange(1,10)
i = 0


while True:
    my_think = int(input('Computer think number , you try to find it: '))
    i += 1
    if computer_think == my_think:
        print(i, 'fine , you found')
        break
    print("sorry , you don't found")




"""import random
my_think = int(input('i white number , you try to find it: '))

i = 0


while True:
    computer_think  = random.randrange(1,10)
    i += 1
    if computer_think == my_think:
        print(i, 'fine , you found')
        break"""
    #print("sorry , you don't found")



# homework 1 
"""
a = int(input('son kiriting: '))

result = 0

i = 1
while result < a + 1:
    result += i
    i += 1

print(result)    """

# homework  2 

"""import  random 

computer_think = random.randrange(1,10)
i = 0
while True:
    my_think = int(input('Computer think number, you try to find it: '))
    i += 1
    if computer_think == my_think:
        print('you found', i)
        break
    else:
        print('sorry, you don\'t found')"""



#   homework 3

"""import random

my_think = int(input('enter '))
i = 0
while True:
    computer_think = random.randrange(1,10)
    i += 1
    if computer_think == my_think:
        print('you found', i)
        break"""


# homework 4

        


"""son = int(input(" son kiriting: "))

a = True
divisor = 2

while divisor <= son ** 0.5:
    if son % divisor == 0:
        a = False
        break
    divisor += 1

print(a)"""

"""
son = int(input(" son kiriting: "))

result = 1
i = 1
while i <= son:
    result *= i
    i += 1

print(result)"""

# homework last


"""user = input("Iltimos, matn kiriting: ")
text = ""

index = len(user) - 1

while index >= 0:
    text += user[index]
    index -= 1

print(text)"""






from random import randrange

com_think = int(input)



















































































































