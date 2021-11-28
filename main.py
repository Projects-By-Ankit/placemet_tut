# class Mobile:
#     def __init__(self, brand, price):
#         print("Inside constructor")
#         self.brand = brand
#         self.price = price
#
#
# class Mobile:
#     def __init__(self, brand, price):
#         print("Inside constructor")
#         self.brand = brand
#         self.price = price
#
#     def purchase(self):
#         print("Purchasing a mobile")
#         print("This mobile has brand", self.brand, "and price", self.price)
#
#
# print("Mobile-1")
# mob1 = Mobile("Apple", 20000)
# mob1.purchase()
#
# print("Mobile-2")
# mob2 = Mobile("Samsung", 3000)
# mob2.purchase()
# class Mobile:
#     def display(self):
#         print("Displaying details")
#
#     def purchase(self):
#         self.display()
#         print("Calculating price")
#
#
# Mobile().purchase()
# class Mobile:
#     def __init__(self, price, brand):
#         print(id(self))
#         self.price = price
#         self.brand = brand
#
#     def return_product(self):
#         print(id(self))
#         print("Brand being returned is ", self.brand, " and price is ", self.price)
#
#
# mob1 = Mobile(1000, "Apple")
# print("Mobile 1 has id", id(mob1))
#
# mob2 = Mobile(2000, "Samsung")
# print("Mobile 2 has id", id(mob2))
#
# mob2.return_product()
# Mobile.return_product(mob2)

# class Mobile:
#     def fun1(xyz,abc):
#         print("hello world:",abc)
#
# obj1 = Mobile()
# obj1.fun1(55)

# print((12.4).is_integer())
