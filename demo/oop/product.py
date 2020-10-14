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

    def __gt__(self, other):
        return self.price > other.price


class DiscountProduct(Product):
    # Constructor
    def __init__(self, name, price, disrate, qoh=0):
        super().__init__(name, price, qoh)
        self.disrate = disrate

    def getprice(self):
        discount = self.price * self.disrate / 100
        discounted_price = self.price - discount
        return (discounted_price * Product.taxrate / 100) + discounted_price


# Create an object of Product class
p1 = Product("Bose Headphones", 25000, 3)
p1.sell(1)
p1.display()  # Call method

print(p1.getprice())
Product.change_taxrate(15)
print(p1.getprice())

p2 = DiscountProduct("Wacom Tablet", 7000, 20)
print(p2.getprice())

products = [Product("iPhone 12", 120000, 10),
            DiscountProduct("iPhone 11 pro", 80000, 20, 5),
            Product("Apple Watch", 30000, 20)
            ]

for p in sorted(products):
    print(p.getprice())  # Polymorphism
