
#clasmthod
#--------------------decorator-------------
"""
class user:
    def __init__(self,f_name,email,yosh,parol) -> None:
        self.f_name = f_name
        self.email = email
        self.yosh = yosh
        self.parol = parol

    @classmethod
    def c_user(cls, f_name, email,parol):
        if len(f_name) < 5:
            yosh = 0
        else:
            yosh = len(f_name)
        return cls(f_name, yosh,email,parol)

                 
user = user.c_user("jhddddd","hdcb@gmail.com",44444)
print(user.yosh)
"""



#-------------------------------------------------------------------------------
#chala
"""
class Restaran:
    def __init__(self,menu_items,book_table,costomer_order ):
        self.menu_items = {}
        self.book_table = []
        self.costomer_order = {}

    def add_item_to_menu(self, item: str, price: int):
        self.menu_items[item] = price
        print(self.menu_items)

    def book_tables(self, number):
        if number in self.book_table:
            print("Uzur bu stol band")
        else:
            self.book_table.append(number)

    def costomer_orderes(self,stol_number,item,):
        """



# chala 
"""
class car:
    def __init__(self, menu_cars, booked_cars, costumer_order, number_cars ) :
        self.menu_cars = {}
        self.booked_car = []
        self.costomer_order = {}
        self.number_cars = {}

    def add_cars_to_menu(self,madeli: str, narxi: int):
        self.menu_cars[madeli] = narxi
        print(self.menu_cars)

    def booked_cars(self, models: str):
        ...cft6

        """



# toliq


"""class Restaran:
    def __init__(self,menu_items = None ,book_table = None ,costomer_order = None ):
        self.menu_items = {}
        self.book_table = []
        self.costomer_order = {}

    def add_item_to_menu(self, item: str, price: int):

        self.menu_items[item] = price
        print(self.menu_items)

    def book_tables(self, number):

        if self.book_table in number:
            print("bu stol allaqachon olingan ")
        else:
            self.book_table.append(number)

    def costumer_orders(self, stol_nomer, item, count):

        if  stol_nomer not in self.costomer_order:
            self.costomer_order[stol_nomer] = {}

        if  stol_nomer not in self.costomer_order:
            self.costomer_order[stol_nomer][item] = count
        else:
            self.costomer_order[stol_nomer][item] += count

    def order(self, stol_nomer):
        text = ""
        foods = self.costomer_order[stol_nomer]
        jami_narx = 0
        for item, soni in foods.items():
            narx = self.menu_items[item] * soni
            text = f" ovqat:{item}, soni: {soni}, narh: {narx} "
            jami_narx = narx

        text += f"jami narx : {jami_narx}"
        print(text)



fayoz = Restaran()

fayoz.add_item_to_menu("osh", 30000)
fayoz.add_item_to_menu("somsa", 20000)
fayoz.add_item_to_menu("lagmon", 25000)

fayoz.book_tables(2)
fayoz.book_tables(2)

fayoz.costumer_orders(2,"osh",2)
fayoz.costumer_orders(2,"somsa",5)

print(fayoz.order(2))
"""
    


















































































































