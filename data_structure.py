"""a = [1,2,3]
b = "6789"
c = list(b)

a.extend(c)

print(a)"""

#homework 1

"""a = [1,2,3,4,5]
b = 0
if int(a[0])%2==1:
    b += int(a[0])
if int(a[0])%2==1:
    b += int(a[1])
if int(a[0])%2==1:
    b += int(a[2])
if int(a[0])%2==1:
    b += int(a[3])
if int(a[0])%2==1:
    b += int(a[4])


print(b)"""


#homework 2

"""a = [1,2,3,4,5]
b = a[0] * a[1] * a[2] * a[3] * a[4]

print(b)"""

#homework 3

"""list = []

if list == []:
    print('list bosh: ')
else:
    print('list bosh')"""



#homework 4


"""a = [1,1,1,1,1]
b = a[::]
c = ['first', 'second', 3]
a.extend(c)

print(a)"""



#homework 5


"""a = ["Bran", 11,      22, 33,'Stark', 22, 33, 11]

a[1]= 'change'


print(a)"""


#homework 6

"""a = [ 'Fayoz', 'Aziz', 'Akmal', 'Toxir', 'Javohir' ]

b = []

ism1 = a[0][0]
ism2 = a[1][0]
ism3 = a[2][0]
ism4 = a[3][0]
ism5 = a[4][0]

if ism1 not in b :
    b.append(ism1)
if ism2 not in b :
    b.append(ism2)
if ism3 not in b :
    b.append(ism3)
if ism4 not in b :
    b.append(ism4)
if ism5 not in b :
    b.append(ism5)

print(b)"""



#homework 7

"""lis = ["man", 'san']
index = (0)

if isinstance(lis[index], int):
    print(lis[index])
else:
    print('not fount')"""













#homework 8

"""name = ['Fayozz', 'Aziz', 'Akmal', 'Diyor']



print(name.sort(key = len))
print(name)"""


# dict/ set

#homework 1

"""a = {0: 10, 1: 20}

a[2] = 30

print(a)"""

#homework 2 

"""c = {
    "a":11,
    "b":22
}
f = input('Qiymat kiriting: ')
if f in c:
    print('allaqchon bor ')
else:
    value = input('value kiriting: ')
    c[f] = value
    print(c)"""
# homework 3

"""d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200}

d2.update(d1)

print(d2)"""

# homework 4

"""a = {
    'Javohir': 20, 
    'Sanjar': 25, 
    'Jamshid': 27
}
print('ism    yosh')

for i,k in a.items():
    print(i,k)"""

# homework 5

"""a = {
    'Javohir': 20, 
    'Sanjar': 25, 
    'Jamshid': None
}

b = a.copy()
for i in b.items():
    if None in i:
        a.pop(i[0])


print(a)"""


# homework 6

"""a = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]

b = {}
for i in a:
    if i[0] not in b.keys():
        b.update({ i[0] : [i[1]]})
    else:
        b.update({ i[0] : b[i[0]] + [i[1]]})



print(b)
"""

# HOMEWORK 7

"""a = {1,2,3,4,5} 
b = input('kiriting: ')


if b in a:
    a.discard(b)
    print(a)
else:
    print('Not Found')   
"""

#homework 8

"""sn1 = {1,2,3,4,5} 

sn2 = {4,5,6,7,8} 

a = sn1.difference(sn2)

print(a)"""

# homework 9

"""a = {'Good morning', 'Hello', 'bye', 'hi'}

b = sorted(a, key=len)

print(b)"""

# homework 10


"""students = {
  'Theodore': 19,
  'Roxanne': 22,
  'Mathew': 21,
  'Betty': 20
} 

a = min(students, key=students.get)
b = max(students, key=students.get)
print(a)
print(b)"""

#homework 11

"""a = {'Red': 1, 'Green': 3, 'White': 5, 'Black': 2, 'Pink': 4}

b = a.items()


print(b)"""


#homework 12


"""k = ['a', 'b', 'c', 'd', 'e', 'f']

v = [1, 2, 3, 4, 5]

f = dict(zip(k,v))
print(f)"""

#homework 13

"""students = [
   {'student_id': 1, 'name': 'Jean Castro', 'class':'V'}, 
   {'student_id': 2, 'name': 'Lula Powell', 'class':'V'},
   {'student_id': 3, 'name':'Brian Howell','class':'VI'},
]


a = input('key  kiriting: ')
b = input('value kiriting: ')

if a in students[0].keys() and b in students[0].values():
    print('true')
else:
    print('false')"""

#homework 14

"""colors = [{"id" : 1, "color" : "Red"}, 
          {"id" : 2, "color" : "Maroon"}, 
          {"id" : 3, "color" : "Yellow"},
]
a = int(input('value kiriting: '))

if a in colors[0].values():
    a = colors.pop(a)
    print(a)"""



"""a = {1,2,3,4,5,6,77,}
b = {1,2,3,4,5,6,77,}
print(a.issubset(b))"""





































































































