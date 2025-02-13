import pytest
from products import Product

def test_product_creation():
    """Test that creating a normal product works."""
    product = Product("Laptop", 1000, 10)
    assert product.name == "Laptop"
    assert product.price == 1000
    assert product.quantity == 10  # ✅ Use property instead of method


def test_product_inactive_when_zero():
    """Test that when a product reaches 0 quantity, it becomes inactive."""
    product = Product("Smartphone", 800, 1)
    product.quantity = 0  # ✅ Use property setter instead of method
    assert product.quantity == 0
    assert product.is_active is False  # ✅ is_active is now a property


def test_product_purchase():
    """Test that product purchase modifies the quantity and returns the right output."""
    product = Product("Headphones", 300, 5)
    total_price = product.buy(3)
    assert total_price == 900  # ✅ Keeping original logic
    assert product.quantity == 2  # ✅ Use property instead of method


def test_buy_too_much():
    """Test that buying a larger quantity than exists invokes exception."""
    product = Product("Smartphone", 800, 2)
    with pytest.raises(ValueError):
        product.buy(5)  # ✅ Should raise an exception


def test_creating_prod_invalid_details():
    """Test that creating a product with invalid details (empty name, negative price) invokes an exception."""
    with pytest.raises(ValueError):
        Product("", 1450, 100)  # ✅ Empty name

    with pytest.raises(ValueError):
        Product("MacBook Air M2", -10, 100)  # ✅ Negative price