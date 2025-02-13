class Basket:
    def __init__(self, data):
        self.data = data
        self.products = []
    
    def add(self, product):
        self.products.append(product)

    def remove(self, product):
        self.products.remove(product)

    def show(self):
        if self.products:
            for i in self.products:
                print(i)
        else:
            print("Hech narsa yo'q")

b1 = Basket(12)

b1.add('phone')

# b1.show()

b1.remove('phone')

b1.show()