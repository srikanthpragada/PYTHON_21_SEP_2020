class Product:
    # class attribute or static attribute
    taxrate = 12

    @staticmethod
    def change_taxrate(newrate):
        Product.taxrate = newrate

    @classmethod
    def create(cls, name, price):
        # process
        return cls(name, price)

    # Constructor
    def __init__(self, name, price, qoh=0):
        # Object Attributes
        self.name = name
        self.price = price
        self.qoh = qoh

    def display(self):
        print("Name  : ", self.name)
        print("Price : ", self.price)
        print("Qoh   : ", self.qoh)

    def sell(self, qty):
        self.qoh -= qty

    def getprice(self):
        return (self.price * Product.taxrate / 100) + self.price


# Create an object of Product class
p1 = Product("Bose Headphones", 25000, 3)
p1.price = 10000
p1.sell(1)
p1.display()  # Call method

print(p1.getprice())
Product.change_taxrate(15)
print(p1.getprice())

p2 = Product("Wacom Tablet", 7000)
p2.display()  # Call method
