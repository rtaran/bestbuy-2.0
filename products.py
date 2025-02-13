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
        return product.price * quantity * (1 - self.percent / 100)


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

        self._name = name
        self._price = price
        self._quantity = quantity
        self._active = True  # Product is active when created
        self._promotion: Optional[Promotion] = None  # Default: No promotion

    # 🏷️ Property for name (read-only)
    @property
    def name(self) -> str:
        return self._name

    # 💲 Property for price with validation
    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, new_price: float):
        if new_price < 0:
            raise ValueError("Product price cannot be negative.")
        self._price = new_price

    # 📦 Property for quantity
    @property
    def quantity(self) -> int:
        return self._quantity

    @quantity.setter
    def quantity(self, new_quantity: int):
        if new_quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self._quantity = new_quantity
        if self._quantity == 0:
            self.deactivate()

    # ✅ Property for active status (read-only)
    @property
    def is_active(self) -> bool:
        return self._active

    def activate(self):
        """Activates the product."""
        self._active = True

    def deactivate(self):
        """Deactivates the product."""
        self._active = False

    # 🎁 Property for promotion
    @property
    def promotion(self) -> Optional[Promotion]:
        return self._promotion

    @promotion.setter
    def promotion(self, new_promotion: Promotion):
        self._promotion = new_promotion

    def buy(self, quantity: int) -> float:
        """Processes a purchase and updates the stock."""
        if quantity <= 0:
            raise ValueError("Purchase quantity must be greater than zero.")
        if quantity > self._quantity:
            raise ValueError("Not enough stock available.")

        # Apply promotion if exists
        total_price = self._promotion.apply_promotion(self, quantity) if self._promotion else self._price * quantity
        self._quantity -= quantity
        return total_price

    # 📝 Magic Method: Convert to string
    def __str__(self) -> str:
        promo_text = f", Promotion: {self._promotion}" if self._promotion else ", Promotion: None"
        return f"{self._name}, Price: ${self._price}, Quantity: {self._quantity}" + promo_text

    # 🔼🔽 Magic Methods: Compare prices
    def __gt__(self, other) -> bool:
        """Returns True if this product is more expensive than another product."""
        if not isinstance(other, Product):
            return NotImplemented
        return self._price > other._price

    def __lt__(self, other) -> bool:
        """Returns True if this product is cheaper than another product."""
        if not isinstance(other, Product):
            return NotImplemented
        return self._price < other._price


class NonStockedProduct(Product):
    """A product that does not have a stock limit (e.g., software licenses)."""

    def __init__(self, name: str, price: float):
        super().__init__(name, price, quantity=0)  # Always 0 quantity

    @Product.quantity.setter
    def quantity(self, new_quantity: int):
        """Quantity of non-stocked products should never change."""
        raise ValueError("Non-stocked products cannot have a quantity.")

    def buy(self, quantity: int) -> float:
        """Non-stocked products have unlimited availability."""
        return self._promotion.apply_promotion(self, quantity) if self._promotion else self._price * quantity


class LimitedProduct(Product):
    """A product that has a purchase limit per order (e.g., shipping fee)."""

    def __init__(self, name: str, price: float, quantity: int, maximum: int):
        super().__init__(name, price, quantity)
        self._maximum = maximum  # Maximum quantity allowed per order

    def buy(self, quantity: int) -> float:
        """Prevents buying more than the allowed quantity per order."""
        if quantity > self._maximum:
            raise ValueError(f"Error while making order! Only {self._maximum} is allowed from this product!")
        return super().buy(quantity)