class Product:
    def __init__(self, name:str, price:float, quantity:int):
        """Initializes a new product with name, price, and quantity."""
        if not name:
            raise ValueError("Product name cannot be empty")
        if price < 0:
            raise ValueError("Product cannot be valued as negative value")
        if quantity < 0:
            raise ValueError("Product cannot be less than zero")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> int:
        """Returns the current quantity of the product."""
        return self.quantity

    def set_quantity(self, quantity:int):
        """Updates the product quantity. Deactivates if quantity is 0."""
        if  quantity < 0:
            raise ValueError ("Quantity can not be below zero")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        """Returns True if the product is active, otherwise False."""
        return self.active

    def activate(self):
        """Activates the product."""
        self.active = True

    def deactivate(self):
        """Deactivates the product."""
        self.active = False


    def show(self) -> str:
        """Returns a string representation of the product."""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity:int):
        """Processes a purchase and updates the stock."""
        if quantity <= 0:
            raise ValueError ("Purchase quantity must be greater than zero")
        if quantity > self.quantity:
            raise ValueError ("Out of stock for the quantity requested")

        total_price = self.price * quantity
        self.set_quantity(self.quantity-quantity)
        return total_price