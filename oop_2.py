#xususiyatlarini ozlashtirish --- qayta ishlata olish uchun --- 

#qayta yozish --- 

#
"""class animal:     # >>> super class or ota class

    def __init__(self,name ,age):
        self.name = name
        self.age = name
    def full_info (self);
        return f"{self.name},{self.age}"



class cat(animal):        #inheritence >>> voris 
    ...
tom = cat("Tom", 10)



class dog(animal):         #inheritence >>> voris
    def __init__(self, name, age,collor,birth_data):
        super().__init__(name, age)
        self.collor = collor
        self.birth_data = birth_data"""


"""class BankAccount():
    def __init__(self , account_number, data_of_openig, balance , customer_name, ):
        self.account_number = account_number
        self.data_of_openig = data_of_openig
        self.balance = float(balance)
        self.customer_name = customer_name
    def __str__(self) -> str:
        return f" {self.account_number}, {self.data_of_openig},{self.balance}, {self.customer_name}"

    def deposit(self) :
        amount = float(input('kartaga qancha yuborishingizni yozing: '))
        all_money = float(self.balance) + float(amount)
        return all_money
    def withdraw(self ):
        amount_1 = float(input("qancha yechmoqchi ekanligingizni kiriting: "))
        all_money_2 = self.balance - amount_1
        return all_money_2
    def chek_balance(self):
        return self.balance
    def print_cutomer_detail(self):
        return f"karta raqam: {self.account_number}, karta ochilagan sana: {self.data_of_openig}, karta nomi: {self.customer_name}, karta blansi: {self.balance} "
   
a = BankAccount(7777777,17,14000,'humo')
print(BankAccount.print_cutomer_detail)"""



"""class Restaran:
    def __init__(self,menu_items,book_table,costomer_order ):
        self.menu_items = menu_items
        self.book_table = book_table
        self.costomer_order = costomer_order
    def __str__(self) -> str:
        return f"{self.menu_items},{self.book_table},{self.costomer_order}"
    
    def add_item_to_menu(self,yangi):
        if self.menu_items not in yangi:
            return self.add_item_to_menu + yangi

    def book_tables(self):
        ...

    def costomer_orderes(self):
        ...

a = Restaran("osh,somsa",3,"osh")

print(Restaran.menu_items)"""

"""
class person:
    def __init__(self,ism,yosh) -> None:
        self.ism = ism
        self.yosh = yosh
    def get_full_info(self):
        return f"ism: {self.ism}, yosh: {self.yosh}"
"""
"""class student:
    def __init__(self,ism,yosh,degree,mark) -> None:
        self.ism = ism
        self.yosh = yosh
        self.degree = degree
        self.mark = mark
    def get_full_info(self):
        return f"ism: {self.ism}, yosh: {self.yosh} darja: {self.degree}, baho: {self.baho}"

"""


"""class student(person):
    def __init__(self,ism,yosh,degree,mark):
        super().__init__(ism,yosh)
        self.degree = degree
        self.mark = mark
    def get_full_info(self):
        text = super().get_full_info
        return f"{text} darja: {self.degree}, baho: {self.baho}"
"""
"""class pupil(student):
    school = "19-maktab"
    def __init__(self, sinf,ism,yosh,degree,mark,togarak) -> None:
        super().__init__(ism,yosh,degree,mark)
        self.sinf = sinf
        self.togarak = togarak
"""




































































































































































