# class Transport:
#     def __init__(self, name, speed):
#         self.name = name
#         self.speed = speed

#     def info(self):
#         return f"Transport nomi : {self.name},\nTezligi : {self.speed}"
    
# class Car(Transport):
#     def info(self):
#         return f"Mashina nomi : {self.name},\nTezligi : {self.speed}"
    
# class Bicycle(Transport):
#     def info(self):
#         return f"Velosiped nomi : {self.name},\nTezligi : {self.speed}"
    

# class Product:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
    
#     def info(self):
#         return f"{self.name} mahsulot soni -> {self.quantity}\nNarxi -> {self.price}"
    
#     def sell(self, amount):
#         if amount <= self.quantity:
#                 self.quantity -= amount
#         else:
#              print('Mahsulot yetarli emas')
        
#     def restock(self, amount):
#             self.quantity += amount


# class Electronics(Product):
#     def __init__(self, name, price, quantity, warranty):
#           super().__init__(name, price, quantity)
#           self.warranty = warranty
#     def info(self):
#         information = f"Mahsulot nomi - {self.name}; yaroqlilik muddati - {self.warranty}\n"
#         information += f"Soni - {self.quantity} x Narxi - {self.price}"


# class Food(Product):
#     def __init__(self, name, price, quantity, expiration_date):
#           super().__init__(name, price, quantity)
#           self.expiration_date = expiration_date

#     def info(self):
#         information = f"Mahsulot nomi - {self.name}; yaroqlilik muddati - {self.expiration_date}\n"
#         information += f"Soni - {self.quantity} x Narxi - {self.price}"
