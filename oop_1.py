

"""class dog:
    def __init__(self,name , age , collor, type): #  obyekt xususiyatlar elon qilinagigon metod
        self.name = name 
        self.age = age
        self.collor = collor
        self.type = type
        
    def bark(self): # obyektga tegishli metod
        return self.name +" "+ "vouw dedi"
    

reks = dog("reks", 3 , "blue", "apcharka") # obyekt, self = reks
print(reks.bark())"""
# object oriented programming (OOP)

"""class employer:
  
 def __init__(self, name, age, salary, degree):
        self.name = name
        self.age = age
        self.salary = salary
        self.degree = degree
# ozgartirmoqchi bolsa shunga tenglab qoyamiz misol uchun 
        # aziz.name = javohir qilsak boladi

        def __str__(self):
            return f"ism {self.name}"



Aziz = employer("Aziz",19, "10  mln ", "admistrator" )
print(Aziz.age)


class student:
    #class atributi
    univer = "IDU" # bu hamma student uchun bir hill boladi
    def __init__(self, ism, yosh, yonalish , univer) -> None:
        self.ism = ism
        self.yosh = yosh
        self.yonalish = yonalish"""

         







"""class employer:

    def __init__(self, name, age, salary, degree):
            self.name = name
            self.age = age
            self.salary = salary
            self.degree = degree
    def get_degree(self):
          return self.degree
    
   
    
class copmny: 
    def __init__(self, name ) :
            self.name = name
            self.max_employers = 0
            self.employers = []
    def add_employers(self, employerr):
          if  employerr not in employer:
                self.employerr.append(employer)"""

"""
def f(x , y ):
    print('start f()')
    s = "fayoz"
    print(locals())


def g():
    print("start g()")
    
    z = 'bar'
    print(locals())

    print('end g()')

g()

print('end f()')"""



# homework 1


"""class student :
    def __init__(self,student_id, student_name, class_name):
        self.id = student_id
        self.name = student_name
        self.class_name = class_name

Aziz = student(2210,"Aziz", "A")
Diyor = student(2211, "Diyor", "B")

print(locals())
print(Aziz)
print(Diyor)"""

# homework 2

"""def student_data(id, name = None, clas = None):
    result = f"Studen_ID: {id} Student class: {clas}"
    if name or clas :
        result += f'Student Name: {name} '

    return result

a = student_data("110m")
print(a)
"""

# homework 3 

"""class student():
    ...

aziz = student()
print(type(aziz))


class marks():
    ...

diyor = marks()
print(type(diyor))"""

#homework 4

"""class student():
    def __init__(self, name , mark, age = 18):
        
        self.name = name
        self.mark = mark
        self.age = age

aziz = student('aziz',55)
print(aziz.age)"""

#homework 5 

"""class turtburchak():
    def __init__(self, uzunligi , kengligi):
        self.uzunligi = uzunligi
        self.kengligi = kengligi
    def tortbuzchak_yuzi(uzunligi = int, kengligi = int):
        result = (uzunligi * kengligi)

        return result

print(turtburchak.tortbuzchak_yuzi(4,5))"""

# homework 6

"""class user():
    def __init__(self, ism , familya , tugilgan_kuni, email, parol):
        self.ism = ism
        self.familya = familya
        self.tugilgan_kuni = tugilgan_kuni
        self.email = email
        self.parol = parol
    def get_info(ism,familya,tugilgan_kuni,email,parol):
        return f" Ism : {ism} , Familya  { familya} , Tugilgan kun : {tugilgan_kuni} , Email: {email} , Parol : {parol}"

print(user.get_info("Fayoz", 'Turaqulov',10,"ffayoz@gmail.com","123456789")) """

#homework 7
"""
class employer():
    def __init__(self, name,  salary, department ):
        self.name = name
        self.salary = salary
        self.department = department


    def conculate_emp_salary():
        ...
    def emp_assign_department():
        ...
    def print_empoyee_details():
        ...

adams = employer("Adams", "E7876", "aconunting")
jones = employer("Jones", "E7499","Researcher")
print(adams.name, adams.salary, adams.department)  """

# homework 8            
"""class BankAccount():
    def __init__(self , account_number, data_of_openig, balance , customer_name, ):
        self.account_number = account_number
        self.data_of_openig = data_of_openig
        self.balance = balance = int
        self.customer_name = customer_name

    def deposit(amount = int ) -> int:
        amount = int(input('kartaga qancha yuborishingizni yozing: '))
        return  amount
    def withdraw(amoun ):
        ...
    def chek_balance():
        ...
    def print_cutomer_detail():
        ..."""


        





#------------------------------------------------------------------------------------

"""class dog:
    ferma = "nimadut MCHJ"
    def __init__(self,ism, yosh,rang,zot ):
        self.ism = ism
        self.yosh = yosh
        self.rang = rang
        self.zot = zot



    def bark(self):
        print('vouv')


    def __str__(self) -> str:
        return f'{self.ism}, {self.yosh}'
        

bobik = dog("bobik", 10,"oq","nomalum")
reks = dog("reks",18,"qora","nomalum")
bobik.ism = bobik.rang[::-1]
print(bobik)"""

#yangi qiymayga o'zgartirish:
#bobik.yosh = 14

"""if __name__ == "__main__":
    print(type(d))"""



class student:
    def __init__(self,ism, yosh ,yonalish) -> None:
        self.ism = ism
        self.yosh = yosh
        self.yonalish = yonalish
        








































































































































