from products import Product, SecondHalfPrice
from store import Store

# Create a promotion
second_half_price = SecondHalfPrice("Second Half price!")

# Create a product with the promotion
macbook = Product("MacBook Air M2", price=1450, quantity=100)
macbook.promotion = second_half_price

# Create a store with the product
store = Store([macbook])

# Create a shopping list with the product added twice
shopping_list = [(macbook, 1), (macbook, 1)]

# Process the order
total_price = store.order(shopping_list)

# Print the result
print(f"Total price for 2 MacBooks with Second Half Price promotion: ${total_price:.2f}")
print(f"Expected price: $2175.00 (1 full price + 1 half price)")

# Test with a single purchase of 2 MacBooks
shopping_list_single = [(macbook, 2)]
total_price_single = store.order(shopping_list_single)
print(f"Total price for 2 MacBooks in a single purchase: ${total_price_single:.2f}")
print(f"Expected price: $2175.00 (1 full price + 1 half price)")

# Verify both approaches give the same result
if total_price == total_price_single:
    print("✅ Fix successful! Both approaches give the same result.")
else:
    print("❌ Fix failed! The results are different.")