from Item import Item

class Phone(Item):

    def __init__(self, name: str, price: float, quantity=1, broken_phones=0):
        # Call to super function to have access to all attributes / method
        super().__init__(
            name, price, quantity
        )

        # Run validations to the received arguments
        assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater than zero!"

        # Assign to self object
        self.broken_phones = broken_phones

        # Actions to execute