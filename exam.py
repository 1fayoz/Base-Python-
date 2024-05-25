from json import dumps, dump , loads, load
#  1 - masala
#     1.  Student nomli class yarating va uning (student_id,
# student_name va class_name xususiyatlari bo’lsin  va shu classdan  bir nechta obyektlar yarating 

# class Student:
#     def __init__(self, id, ism, sinf_nomi) -> None:
#         self.__id = id
#         self.name = ism
#         self.class_name = sinf_nomi
        
#     def get_info(self):
#         return f"Student id: {self.__id} \nStudent name: {self.name} \nClass name: {self.class_name}"
    
    
#     def get_name(self):
#         return f"Student name: {self.name}"
    
#     def get_class(self):
#         return f"Student class name: {self.class_name}"
    
    
    
#  2 - masala
 
#  
 
# python_obj = {
#              "name": "David",
#              "class":"I",
#              "age": 6,
#              "married": True  
#             }

# result = dumps(python_obj)
# print(result)




# 3 - masala 

# arr = []
# with open("countries.json", 'r') as f:
#     data = load(f)
#     for k in data:
#         arr.append(k)
        

# with open("natija.txt", "w+") as f:
#     for i in arr:
#         f.write(f"{dump(i, f, indent=4)} \n")


# 4-masala

# with open("context.txt", "r") as f:
#     doc = {}
#     arr = f.read().split()
#     for i in arr:
#         doc[i] = arr.count(i)
#     print(doc) 




#  5-masala

# with open("context.txt", "r") as f:
#     print(len(f.readlines()))

#  6- malsala 

from datetime import datetime, timedelta, date as d

# now_date = datetime.now().date()
# day = timedelta(days=1)
# res = f"Today: {now_date}, Yesterday: {now_date-day}, Tomarrow: {now_date+day}"
# print(res)


#  7- masala
# new_date = datetime.now().date()
# minutes = timedelta(minutes=5)
# print(f"Now date {new_date+minutes}")

# 8-masala

# def print_sundays(year):
#     sundays = []
#     for month in range(1, 13):
#         for day in range(1, 32):
#             try:
#                 date = d(year, month, day)
#                 if date.weekday() == 6:
#                     sundays.append(date)
#             except ValueError:
#                 pass
#     print(f"Yil {year}da {len(sundays)} yakshanba kunlari bor:")
#     for sunday in sundays:
#         print(sunday)
    

# year = int(input("Yilni kiriting: "))
# print_sundays(year)

# 9-masala
# def tub(n):
#     if n <= 1:
#         return False
#     if n <= 3:
#         return True
#     if n % 2 == 0 or n % 3 == 0:
#         return False
#     i = 5
#     while i * i <= n:
#         if n % i == 0 or n % (i + 2) == 0:
#             return False
#         i += 6
#     return True

# def func(a):
#     arr = []
#     for i in range(1, n+1):
#         if tub(i):
#             arr.append(i)
#     return arr
            
                

# n = int(input("son kiriting: "))

# print(func(n))

# 10 -masala
# text = "Python is a widely used high-level, general-purpose, interpreted, dynamic programming language.Its design philosophy emphasizes code readability"

# res = text.replace("a", "9")
# print(res)





























































