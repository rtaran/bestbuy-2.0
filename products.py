class Product:
    def __init__(self, name: str, price: float, quantity: int):
        """Initializes a new product with name, price, and quantity."""
        if not name:
            raise ValueError("Product name cannot be empty.")
        if price < 0:
            raise ValueError("Product price cannot be negative.")
        if quantity < 0:
            raise ValueError("Product quantity cannot be negative.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True  # Product is active when created

    def get_quantity(self) -> int:
        """Returns the current quantity of the product."""
        return self.quantity

    def set_quantity(self, quantity: int):
        """Updates the product quantity. Deactivates if quantity is 0."""
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
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
        return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}"

    def buy(self, quantity: int) -> float:
        """Processes a purchase and updates the stock."""
        if quantity <= 0:
            raise ValueError("Purchase quantity must be greater than zero.")
        if quantity > self.quantity:
            raise ValueError("Not enough stock available.")

        total_price = self.price * quantity
        self.set_quantity(self.quantity - quantity)
        return total_price


# ✅ NonStockedProduct (No Quantity Tracking)
class NonStockedProduct(Product):
    def __init__(self, name: str, price: float):
        """Non-stocked products always have quantity set to 0."""
        super().__init__(name, price, quantity=0)

    def set_quantity(self, quantity: int):
        """Non-stocked products should never have their quantity changed."""
        raise ValueError("Cannot change quantity of a non-stocked product.")

    def buy(self, quantity: int) -> float:
        """Purchase is always valid for non-stocked products."""
        if quantity <= 0:
            raise ValueError("Purchase quantity must be greater than zero.")
        return self.price * quantity  # No stock reduction

    def show(self) -> str:
        """Display product details indicating it's a non-stocked product."""
        return f"{self.name}, Price: ${self.price}, Quantity: Unlimited"


# ✅ LimitedProduct (Restrict Max Purchase Per Order)
class LimitedProduct(Product):
    def __init__(self, name: str, price: float, quantity: int, maximum: int):
        """Limited products have a purchase restriction per order."""
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, quantity: int) -> float:
        """Restricts purchase to the allowed maximum per order."""
        if quantity > self.maximum:
            raise ValueError(f"Error while making order! Only {self.maximum} is allowed from this product!")
        return super().buy(quantity)

    def show(self) -> str:
        """Display product details including purchase restriction."""
        return f"{self.name}, Price: ${self.price}, Limited to {self.maximum} per order!"


# ✅ Example Testing Code (Copy-Paste to main.py for Testing)
if __name__ == "__main__":
    # Sample Product List with New Classes
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
        NonStockedProduct("Windows License", price=125),
        LimitedProduct("Shipping", price=10, quantity=250, maximum=1),
    ]

    # Print Product Details
    for product in product_list:
        print(product.show())