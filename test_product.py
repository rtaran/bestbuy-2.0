import pytest
from products import Product

# ✅ Test 1: Creating a normal product
def test_product_creation():
    product = Product("Laptop", 1000, 10)
    assert product.name == "Laptop"
    assert product.price == 1000
    assert product.get_quantity() == 10  # ✅ Fix: Using get_quantity() to match original logic

# ✅ Test 2: Creating a product with invalid details should raise an exception
def test_invalid_product_creation():
    with pytest.raises(ValueError):
        Product("", 1450, 100)  # Empty name

    with pytest.raises(ValueError):
        Product("MacBook Air M2", -10, 100)  # Negative price

# ✅ Test 3: When a product reaches 0 quantity, it becomes inactive
def test_product_inactive_when_zero():
    product = Product("Smartphone", 800, 1)
    product.set_quantity(0)  # ✅ Fix: Using set_quantity() to update stock
    assert product.is_active() is False  # ✅ Fix: Correct check for active status

# ✅ Test 4: Buying a product modifies quantity and returns the correct output
def test_product_purchase():
    product = Product("Headphones", 300, 5)
    total_price = product.buy(3)
    assert total_price == 900  # ✅ Fix: Keeping original logic that returns total price
    assert product.get_quantity() == 2  # ✅ Fix: Using get_quantity()

# ✅ Test 5: Buying more than available stock should raise an exception
def test_buying_more_than_stock():
    product = Product("Tablet", 500, 5)
    with pytest.raises(ValueError):
        product.buy(10)  # Not enough stock available