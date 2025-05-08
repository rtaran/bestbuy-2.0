import pytest
from products import Product, SecondHalfPrice, ThirdOneFree, PercentDiscount
from store import Store


def test_second_half_price_promotion():
    """Test that the Second Half Price promotion works correctly."""
    # Create a promotion
    second_half_price = SecondHalfPrice("Second Half price!")

    # Create a product with the promotion
    macbook = Product("MacBook Air M2", price=1450, quantity=100)
    macbook.promotion = second_half_price

    # Create a store with the product
    store = Store([macbook])

    # Test with separate purchases
    shopping_list = [(macbook, 1), (macbook, 1)]
    total_price = store.order(shopping_list)

    # Test with a single purchase of 2 MacBooks
    macbook.quantity = 100  # Reset quantity
    shopping_list_single = [(macbook, 2)]
    total_price_single = store.order(shopping_list_single)

    # Verify both approaches give the same result
    assert total_price == total_price_single
    assert total_price == 2175.0  # 1450 + (1450 * 0.5)


def test_third_one_free_promotion():
    """Test that the Third One Free promotion works correctly."""
    # Create a promotion
    third_one_free = ThirdOneFree("Third One Free!")

    # Create a product with the promotion
    headphones = Product("Bose QuietComfort Earbuds", price=250, quantity=100)
    headphones.promotion = third_one_free

    # Create a store with the product
    store = Store([headphones])

    # Test buying 3 items (should pay for 2)
    shopping_list = [(headphones, 3)]
    total_price = store.order(shopping_list)

    assert total_price == 500.0  # Pay for 2 items only


def test_percent_discount_promotion():
    """Test that the Percent Discount promotion works correctly."""
    # Create a promotion
    thirty_percent_off = PercentDiscount("30% off!", 30)

    # Create a product with the promotion
    laptop = Product("Dell XPS", price=1000, quantity=50)
    laptop.promotion = thirty_percent_off

    # Create a store with the product
    store = Store([laptop])

    # Test buying with 30% discount
    shopping_list = [(laptop, 2)]
    total_price = store.order(shopping_list)

    assert total_price == 1400.0  # 2000 * 0.7
