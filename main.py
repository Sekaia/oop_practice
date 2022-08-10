class Item:
    def __init__(self, name: str, price: float, quantity):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than zero!"
        assert quantity >= 0, f"Price {quantity} is not greater than zero!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return self.name

    def calculate_total_price(self):
        return self.price * self.quantity


item1 = Item("Laptop", 1000, 2)
item2 = Item("Phone", 100, 4)

print(item1)
print(item2)
