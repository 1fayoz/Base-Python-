# matn = "Hello World"
# res = matn[-4:-1]
# print(res)

# matn = "Hello World"
# res = matn[::-1]

# help(str)


# ism = input("Ismingizni yozing>>>_ ")
# yosh = int(input("Yoshingizni yozing>>>_ "))

# # res = "Ism:" + ism + " " + "Yoshi:" + str(yosh)
# res = "Ism : %s,\nYoshi : %s" % (ism, yosh)
# print(res)

# --------------------

# matn = "Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\t Up above the world so high,\n\t\t Like a diamond in the sky.\nTwinkle, twinkle, little star,\n\t How I wonder what you are"

# print(matn)


# ---------------------

# matn = input("Matn kiriting>>>__ ")
# res = matn.title()[::-1]
# print(res)

# ---------------------

# s, n = input("So'z va son kiriting >>> __ ").split(" ")
# res = s.replace(s[int(n)], " ")
# print(res) 


# ---------------------

# matn = input("Matn kiriting>>>__ ")
# res = matn.rstrip()
# print(res)


# ---------------------

# matn, char = input("Matn kiriting>>>__ ").split(", ")
# res = matn.count(char)

# print(res)

# ---------------------

# matn = input("Matn kiriting>>>__ ").split(" ")
# res = len(matn)
# print(res)


# ---------------------

# n = input("4 xonli son kiriting>>>__ ")
# res = f"{n[0]}+{n[1]}+{n[2]}+{n[3]}={int(n[0])+int(n[1])+int(n[2])+int(n[3])}"
# print(res)

# ---------------------



from math import exp, fabs, tan, cos, sin
 

# a = 3j
# c = a+6
# print(type(a))
# print(c*5)
# print(4**2)

# a = 31536
# n = int(input("Nechi yil ketti>>_ "))
# res =  n * a
# print(res)

# x = float(input("x = "))
# y = float(input("y = "))
# a = x + y 
# b = y**2 + fabs((y**2+2)/(x+((x**3)/5))) 
# c = exp(y+2)
# res = a/b+c
# print(round(res,2))

# x = float(input("x = "))

# a = 2*tan(x+2) - cos(x + 2**x)
# b = 1+(cos(x+2))**2
# c = sin(x**2)/(x**2+3)
# res = (a/b)**.5+c
# print(round(res, 2))


# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))
# d = int(input("d = "))
# x = float(input("x = "))
# A = (a*x**2+b*x+c)/(x*a**3+a**2+a**(b-c))
# B = cos((a*x+b)/(c*x+d+2**c))
# res = A+B
# print(round(res, 2))





# n = int(input("Musbat son kiriting = "))
# res = n**3
# print(res)


# v = int(input("v = "))
# s = int(input("s = "))
# res = s/v
# print(res)


# h = int(input("Son kiriting = "))


# y = 11

# if y<18:
#     print("18")
# elif y<12:
#     print("12")
# else:
#     print("else")







# ---------------Misol------------------------

# a,b,c = map(float, input("3 ta son kiriting (a,b,c):>>>_ ").split(','))
# if b<a<c and b>a>c:
#     print(f"The median is: {a}")
# elif a<b<c and a>b>c:
#     print(f"The median is: {b}")
# elif a<c<b and a>c>b:
#     print(f"The median is: {b}")

# age = int(input("Yoshingizni kiriting:___ "))

# if age < 16:
#     print("Siz hali pasport yoshiga yetmagansiz")
# else:
#     print("Siz pasport ola olasiz")



# n = int(input("Son kiriting:__ "))

# if not n%5 and not n%7:
#     print("Noway")
# elif not n%5:
#     print("Five")
# elif not n%7:
#     print("Seven")
# else:
#     print("False")

# matn = input("Matn kiriting:__ ")

# if matn.isdigit():
#     print(True)
# else:
#     print(False)


# matn = input("Matn kiriting:__ ")

# if "yozuv" in matn:
#     print(True)
# else:
#     print(False)



# matn = input("Matn kiriting:__ ")

# if "@gmail.com" in matn:
#     print("“Sizda ruhsat mavjud”")
# else:
#     print("No'tog'ri email kiritdingiz")


# print(True+1)     




# a = [1,2,3,4]
# b = "5678"
# c = [int(b[0]),int(b[1]),int(b[2]),int(b[3])]
# a.extend(c)
# print(a)

# a = ('salom', "daodk", "slk", "BMW", [1,2,3,4])
# a[4].append(5)
# print(a)



# a = ('salom', "daodk", "slk", "BMW", [1,2,3,4])
# a[3]="Mers"
# print(a)


# nl = list(input("5 xonali sonlarni kiriting >>> __ "))
# a = []
# print(nl)
# if int(nl[0]) % 2:
#     a.append(int(nl[0]))

# if int(nl[1]) % 2:
#     a.append(int(nl[1]))

# if int(nl[2]) % 2:
#     a.append(int(nl[2]))

# if int(nl[3]) % 2:
#     a.append(int(nl[3]))

# if int(nl[4]) % 2:
#     a.append(int(nl[4]))

# print(a)
# print(sum(a))

# l = list(input("Matn kiriting >>> __ ").strip())
# if len(l):
#     print(f"Sizning ro'yxatingizda {len(l)}ta element bor")
# else:
#     print("Ro'yxatingiz bo'sh")



# l = list(input("Matn kiriting >>> __ "))
# c = l[::]
# c.append("first")
# c.append("second")
# c.append(3)
# print(l)
# print(c)

# l = list(input("Matn kiriting >>> __ ").split(","))
# l[1] = "change"
# print(l)



# l = list(input("Matn kiriting >>> __ ").split(" "))
# print(l)



# Set = {1,2,3,4,5}
# for i in Set:
#     print(i)

# print(Set, type(Set))



# for i in range(1500,2700):
#     if i % 5 == 0 and i % 7 == 0:
#         print(i)
    


# a = 6
# for n in range(a):
#     for i in range(n):
#         print("*", end="")
#     print()
# for i in range(n, -1, -1):
#     for _ in range(i):   
#         print("*", end="")
#     print()



# datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]

# for el in datalist:
#     print(f"Type of  {el}  is  {type(el)}")





# for i in range(0,7):
#     if i % 3:
#         print(i)


# matn = input("Matn kiriting:>__ ")
# n=0
# m=0
# for i in matn:
#     if i.isdigit():
#         n+=1
#     else:
#         m+=1
# print(f"{n}ta son, {m}ta harf qatnashgan")

# n = int(input("Son kiriting: "))
# for i in range(n+1):
#     for son in range(1,i+1):
#         print(i, end='')
#     print()

# row, col = input("Qator va ustun sonlarini kiriting: ").split(" ")
# for r in range(row):
#     for c in range(col):




# n = [2,9,11,15,4,5,6,7,8] 
# t = 9
# # print(nums.index(11))
# def twosum(nums, tar):
#     for i, el in enumerate(nums):
#         for n in nums:
#             if el + n == tar and nums.index(el) != nums.index(n):
#                 return [nums.index(el), nums.index(n)]
# print(twosum(n,t))
# x = 121
# def isPalindrome(self, x: int) -> bool:
#         # return x == int(str(x[::-1]))

# print(isPalindrome(n))
# print(x == int(str(x)[::-1]))
# print(str(x) == str(x[::-1]))


# strs = ["flower","flow","flight"]

# strs.sort(key=len)
# print(strs)



# res = (2,)*2
# print(res)


# a = 5
# while a>=1:
#     print(a)
#     a -= 1

# for i in range(5, 0, -1):
#     print(i)

# fruits = ["apple", "banana", "cherry", "new"]


# i = 0
# while i < len(fruits):
#     print(fruits[::-1][i])
#     i += 1


# matn = "Hello World"
# l = len(matn)
# i = 0
# while i < l:
#     print(matn[i])
#     i += 1



# i = 2
# while i <= 20:
#     print(i)
#     i += 3
# else:
#     print("Tsikl yakunlandi.")






import random as ran

# Ai = ran.randrange(1,11)
# while True:
#     user = int(input("1 dan 11 gacha son kiriting: "))
#     if Ai == user:
#         print(f"Tabriklaymiz topdingiz AI {Ai} son o'yladi Siz {user} sonini")
#         break
#     else:
#         print(f"Topa olmadingiz Ai soni {Ai}")
#         Ai = ran.randrange(1,11)

    
# user = int(input("1 dan 11 gacha son kiriting: "))
# count = 0
# while True:
#     Ai = ran.randrange(1,11)
#     count += 1
#     if Ai == user:
#         print(f"Tabriklaymiz siz {count} ta urinishda topdingiz")
#         break
#     else:
#         print(f"Topa olmadingiz Ai soni {Ai}")


# user = int(input("Son kiriting: "))
# i = 0
# summa = 0
# while i < user:
#     if i % 2 == 0:
#         summa += i
#     i += 1
# print(summa)


# user = int(input("Son kiriting: "))
# i = 0
# summa = 0
# while i < user:
#     if i % 2 == 0:
#         summa += i
#     i += 1
# print(summa)


# print(23/2)





# def func(arg):
#     print("Hello world")
#     return



# print(func)

# def func(a):
#     ls = []
#     res = ''
#     for i in a:
#         if i != ' ':
#             res += i
#         else:
#             ls.append(res)
#             res = ''
#     if not res.strip():
#         ls.append(res)
#     return ls
    

# matn = "Hello World I'm a  devoloper"

# print(func(matn))





# def tup(a: int):
#     if a < 2:
#         return False
#     for i in range(2, a//2+1):
#         if a % i == 0:
#             return False
#     return True
# print(tup(4))



# def sqrt(a: int):
#     return a**2
# print(sqrt(4))



# def opposite(a):
#     r = 1
#     res = ''
#     while r <= len(a):
#         res += a[-r]
#         r += 1
#     return res
# # matn = "Hello world"
# # print(opposite(matn))

# def isPalindrome(soz: str):
#     return soz.lower() == opposite(soz.lower())
# print(isPalindrome("Kiyik"))



# def func(a):
#     ...



# from datetime import datetime

# print(datetime.now(), datetime.today())
# # print(datetime.today())




# row, col =  int(input("Row > ")), int(input("Col > "))
# res = []





from datetime import datetime, timedelta

# print(datetime.today())

# now_date = datetime.now().date()
# res = now_date.strftime("%Y")
# print(res)
# res = now_date.strftime("%B")
# print(res)
# res = now_date.strftime("%U")
# print(res)
# res = now_date.strftime("%w")
# print(res)
# res = now_date.strftime("%j")
# print(res)
# res = now_date.strftime("%d")
# print(res)

# print(datetime.today().time())

# req = input("Jan 1  2014  2:43PM")

# input_date = "Jan 1 2014 2:43PM"

# # Parse INPUT string according to its format
# parsed_date = datetime.strptime(input_date, "%b %d %Y %I:%M%p")

# # Convert parsed date to desired format
# output_date = parsed_date.strftime("%Y-%m-%d %H:%M:%S")

# print("OUTPUT:", output_date)

# kiritilgan_son = int(input("Iltimos, bir son kiriting: "))
# xozirgi_sana = datetime.now()
# oldingi_sana = xozirgi_sana - timedelta(days=kiritilgan_son)
# print(f"Foydalanuvchi kiritgan {kiritilgan_son} kun oldingi sana: {oldingi_sana.strftime('%Y-%m-%d')}")



# now_date = datetime.today().date()

# day = timedelta(days=1)
# last_day = now_date - day
# print(f"Kechagi sana {last_day}")
# print(f"Bugungi sana {now_date}")

# tomarrow = now_date + day
# print(f"Ertangi sana {tomarrow}")

# now_date = datetime.today()

# five_minute = timedelta(minutes=5)
# res = now_date + five_minute

# print(now_date)
# print(res)




# def func(a,b):
#     return lambda c, d: sum([a,b,c,d])

# res = func(3,4)
# print(res(5,6))


# def func(*args):
#     return ...



# nums = [3,4,5,6,1]
# res = list(map(lambda x: x**3, nums))
# print(res)

# arr = ['asd', '12', 'dac', '21', 's34', '65', 'ak74']
# res = list(map(lambda x: x.isdigit(), arr))
# print(res)
# arr1 = [4,2,3,4,6]
# arr = [20,10,30,43,22]

# res = list(map(lambda x: x<10, arr))
# print(res)


# res = list(filter(lambda x: x>10, arr))
# print(res)


# a = [3214, 'sda', 43, "loo", True, 2.32]
# res = list(filter(lambda x: x.isalpha(), a))
# print(res)



# a,b,c = [1,2,3], [4,5,6], [7,8,9]
# nums_sum = list(map(lambda x,y,z: x+y+z, a,b,c))
# print(nums_sum)


# arr = ['Red', 'Blue', 'Black', 'White', 'Pink'] 
# list_arr = list(map(lambda x: list(x), arr))
# print(list_arr)


# chars = {'a', 'b', 'E', 'f', 'u', 'i', 'o', 'U', 'a'}

# alp_chars = list(map(lambda x: (x.upper(), x.lower()) , list(chars)))
# print((set(alp_chars)))


# a,b = [6, 5, 3, 9], [0, 1, 7, 7]
# nums_sum = list(map(lambda x,y: (x+y,x-y), a,b))
# print(nums_sum)

# student_data  = [('Alberto Franco', '15/05/2002','35kg'), ('Gino Mcneill','17/05/2002','37kg'), ('Ryan Parkes','16/02/1999', '39kg'), ('Eesha Hinton','25/09/1998', '35kg')]

# a = list(map(lambda x : x[0], student_data))
# b = list(map(lambda x : x[1], student_data))
# c = list(map(lambda x : x[2], student_data))
# print(a,b,c)

# nums1 = [1,2,3,4,5,6,7,8]
# nums2 = [2,2,3,1,2,6,7,9]

# equal = list(map(lambda x, y: x==y, nums1, nums2))
# print(sum(equal))




# 1 - misol 
# matn = "Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\t Up above the world so high,\n\t\t Like a diamond in the sky.\nTwinkle, twinkle, little star,\n\t How I wonder what you are"

# print(matn)


# # 2 - misol 
# a = float(input("a son kiriting>>> "))
# b = float(input("b son kiriting>>> "))

# t = a**(1/5)
# s = (a + b)/2*b+a*b
# q = (a**2+(b**2)+2)  
# k = (b*s)**(1/4)
# res = t + k * q
# print(res)

# 3 - misol 

# lists = ["Anvar", "Zokir", "Zafar", "Jamshid", "Abdulla"]
# setlist = set()
# for el in lists:
#     setlist.add(el[0])
# listset = list(setlist)
# print(listset)

# 4 - misol 

# r = int(input("Qator sonini kiriting>>> "))
# c = int(input("Ustun sonini kiriting>>> "))

# for s in range(r):
#     for i in range(c):
#         print(s*2,end="")
#     print()

    

# 5 - misol 

# matn = "While loop"   

# l = len(matn)
# i = 0
# while i < l :
#     print(matn[i])
#     i += 1



# 6 - misol


# nums = list(map(int, list(input("Sonlar kiriting>>> "))))
# res = int("".join(list(map(str, nums))))+1
# res =  list(map(int, list(str(res))))
# print(res)

# 6 - misol

# n =  int(input("Son kitiring>>> "))
# res = False
# if n % 2 != 0:
#     print(res)
# for i in range(2,n+1,2):
#     if 2**i == n:
#         res = True
#         print(res)
# if res != True:
#     print(res)
  






















