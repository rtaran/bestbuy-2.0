from abc import ABC, abstractmethod
from typing import Optional


class Promotion(ABC):
    """Abstract class for promotions."""

    def __init__(self, name: str):
        """
        Initialize a promotion with a name.

        :param name: The name of the promotion
        """
        self.name = name
        self._active = True  # Use _active to avoid shadowing is_active property

    @abstractmethod
    def apply_promotion(self, product, quantity: int) -> float:
        """
        Applies the promotion to the given product and quantity.

        :param product: The product to apply the promotion to
        :param quantity: The quantity of the product
        :return: The discounted price
        """
        pass

    def __str__(self):
        """Return the string representation of the promotion."""
        return self.name


class PercentDiscount(Promotion):
    """Promotion that applies a percentage discount to the product price."""

    def __init__(self, name: str, percent: float):
        """
        Initialize a percentage discount promotion.

        :param name: The name of the promotion
        :param percent: The discount percentage
        """
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity: int) -> float:
        """
        Applies a percentage discount to the total price.

        :param product: The product to apply the promotion to
        :param quantity: The quantity of the product
        :return: The discounted price
        """
        return product.price * quantity * (1 - self.percent / 100)


class SecondHalfPrice(Promotion):
    """Promotion that applies 'Second Item at Half Price' discount."""

    def apply_promotion(self, product, quantity: int) -> float:
        """
        Applies the 'Second Item at Half Price' discount.

        :param product: The product to apply the promotion to
        :param quantity: The quantity of the product
        :return: The discounted price
        """
        full_price_items = quantity // 2 + quantity % 2
        half_price_items = quantity // 2
        return (full_price_items * product.price) + (half_price_items * product.price * 0.5)


class ThirdOneFree(Promotion):
    """Promotion that applies 'Buy 2, Get 1 Free' discount."""

    def apply_promotion(self, product, quantity: int) -> float:
        """
        Applies the 'Buy 2, Get 1 Free' discount.

        :param product: The product to apply the promotion to
        :param quantity: The quantity of the product
        :return: The discounted price
        """
        payable_items = quantity - (quantity // 3)
        return payable_items * product.price


class Product:
    """Base class for all products in the store."""

    def __init__(self, name: str, price: float, quantity: int):
        """
        Initializes a new product with name, price, and quantity.

        :param name: The name of the product
        :param price: The price of the product
        :param quantity: The initial quantity of the product
        :raises ValueError: If name is empty, price or quantity is negative
        """
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

        # Deactivate product if quantity is 0
        if quantity == 0:
            self.deactivate()

    @property
    def name(self) -> str:
        """
        Get the name of the product (read-only).

        :return: The product name
        """
        return self._name

    @property
    def price(self) -> float:
        """
        Get the price of the product.

        :return: The product price
        """
        return self._price

    @price.setter
    def price(self, new_price: float):
        if new_price < 0:
            raise ValueError("Product price cannot be negative.")
        self._price = new_price

    @property
    def quantity(self) -> int:
        """
        Get the current quantity of the product.

        :return: The product quantity
        """
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

    @property
    def promotion(self) -> Optional[Promotion]:
        """
        Get the current promotion applied to the product.

        :return: The promotion object or None if no promotion is applied
        """
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
        if self._promotion:
            total_price = self._promotion.apply_promotion(self, quantity)
        else:
            total_price = self._price * quantity
        self._quantity -= quantity
        return total_price

    # 📝 Magic Method: Convert to string
    def __str__(self) -> str:
        """Return the string representation of the product."""
        if self._promotion:
            promo_text = f", Promotion: {self._promotion}"
        else:
            promo_text = ", Promotion: None"
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
        """
        Initialize a non-stocked product with name and price.

        :param name: The name of the product
        :param price: The price of the product
        """
        super().__init__(name, price, quantity=0)  # Always 0 quantity
        self._active = True  # Always active

    @Product.quantity.setter
    def quantity(self, new_quantity: int):
        """
        Quantity of non-stocked products should never change.

        :param new_quantity: Attempted new quantity value
        :raises ValueError: Always raises this error
        """
        raise ValueError("Non-stocked products cannot have a quantity.")

    def buy(self, quantity: int) -> float:
        """
        Non-stocked products have unlimited availability.

        :param quantity: The quantity to buy
        :return: The total price
        """
        if self._promotion:
            return self._promotion.apply_promotion(self, quantity)
        else:
            return self._price * quantity

    def __str__(self) -> str:
        """Return the string representation of the non-stocked product."""
        if self._promotion:
            promo_text = f", Promotion: {self._promotion}"
        else:
            promo_text = ", Promotion: None"
        return f"{self._name}, Price: ${self._price}, Quantity: Unlimited" + promo_text


class LimitedProduct(Product):
    """A product that has a purchase limit per order (e.g., shipping fee)."""

    def __init__(self, name: str, price: float, quantity: int, maximum: int):
        """
        Initialize a limited product with name, price, quantity, and maximum purchase limit.

        :param name: The name of the product
        :param price: The price of the product
        :param quantity: The initial quantity of the product
        :param maximum: The maximum quantity allowed per order
        """
        super().__init__(name, price, quantity)
        self._maximum = maximum  # Maximum quantity allowed per order

    def buy(self, quantity: int) -> float:
        """
        Prevents buying more than the allowed quantity per order.

        :param quantity: The quantity to buy
        :return: The total price
        :raises ValueError: If quantity exceeds the maximum allowed
        """
        if quantity > self._maximum:
            raise ValueError(f"Error while making order! Only {self._maximum} is allowed from this product!")
        return super().buy(quantity)

    def __str__(self) -> str:
        """Return the string representation of the limited product."""
        if self._promotion:
            promo_text = f", Promotion: {self._promotion}"
        else:
            promo_text = ", Promotion: None"
        return f"{self._name}, Price: ${self._price}, Limited to {self._maximum} per order!" + promo_text
