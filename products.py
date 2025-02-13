from abc import ABC, abstractmethod
from typing import Optional


class Promotion(ABC):
    """Abstract class for promotions."""

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity: int) -> float:
        """Applies the promotion to the given product and quantity."""
        pass

    def __str__(self):
        return self.name


# 🎁 Promotion 1: Percentage Discount
class PercentDiscount(Promotion):
    def __init__(self, name: str, percent: float):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity: int) -> float:
        """Applies a percentage discount to the total price."""
        discount = self.percent / 100
        return product.price * quantity * (1 - discount)


# 🎁 Promotion 2: Second Item at Half Price
class SecondHalfPrice(Promotion):
    def apply_promotion(self, product, quantity: int) -> float:
        """Applies the 'Second Item at Half Price' discount."""
        full_price_items = quantity // 2 + quantity % 2
        half_price_items = quantity // 2
        return (full_price_items * product.price) + (half_price_items * product.price * 0.5)


# 🎁 Promotion 3: Buy 2, Get 1 Free
class ThirdOneFree(Promotion):
    def apply_promotion(self, product, quantity: int) -> float:
        """Applies the 'Buy 2, Get 1 Free' discount."""
        payable_items = quantity - (quantity // 3)
        return payable_items * product.price


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
        self.promotion: Optional[Promotion] = None  # Default: No promotion

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
        """Returns a string representation of the product, including any promotion."""
        promo_text = f", Promotion: {self.promotion}" if self.promotion else ", Promotion: None"
        return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}" + promo_text

    def buy(self, quantity: int) -> float:
        """Processes a purchase and updates the stock."""
        if quantity <= 0:
            raise ValueError("Purchase quantity must be greater than zero.")
        if quantity > self.quantity:
            raise ValueError("Not enough stock available.")

        # Apply promotion if exists
        total_price = self.promotion.apply_promotion(self, quantity) if self.promotion else self.price * quantity
        self.set_quantity(self.quantity - quantity)
        return total_price

    def set_promotion(self, promotion: Promotion):
        """Assigns a promotion to the product."""
        self.promotion = promotion

    def get_promotion(self) -> Optional[Promotion]:
        """Returns the current promotion."""
        return self.promotion


class NonStockedProduct(Product):
    """A product that does not have a stock limit (e.g., software licenses)."""

    def __init__(self, name: str, price: float):
        super().__init__(name, price, quantity=0)  # Always 0 quantity

    def set_quantity(self, quantity: int):
        """Quantity of non-stocked products should never change."""
        raise ValueError("Non-stocked products cannot have a quantity.")

    def buy(self, quantity: int) -> float:
        """Non-stocked products have unlimited availability."""
        return self.promotion.apply_promotion(self, quantity) if self.promotion else self.price * quantity


class LimitedProduct(Product):
    """A product that has a purchase limit per order (e.g., shipping fee)."""

    def __init__(self, name: str, price: float, quantity: int, maximum: int):
        super().__init__(name, price, quantity)
        self.maximum = maximum  # Maximum quantity allowed per order

    def buy(self, quantity: int) -> float:
        """Prevents buying more than the allowed quantity per order."""
        if quantity > self.maximum:
            raise ValueError(f"Error while making order! Only {self.maximum} is allowed from this product!")
        return super().buy(quantity)