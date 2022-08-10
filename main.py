class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def calculate_total_price(self, x, y):
        return x * y
    def __str__(self):
        return f"{self.name}: ${str(self.price)} x{str(self.quantity)} |  Total: ${self.calculate_total_price(self.price,self.quantity)}"


item1 = Item("Laptop", 1000, 3)

item2 = Item("Phone", 100, 20)

print(item1)
print(item2)