from products import Product
from store import Store

def main():
    # Creating a list of products
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
    ]

    # Creating a Store instance
    best_buy = Store(product_list)

    # Get all active products
    available_products = best_buy.get_all_products()
    print(f"Total Products Available: {len(available_products)}")

    # Print total quantity of all items
    print(f"Total quantity in store: {best_buy.get_total_quantity()}")

    # Placing an order
    order_cost = best_buy.order([
        (available_products[0], 1),  # MacBook Air M2 x1
        (available_products[1], 2)   # Bose Earbuds x2
    ])
    print(f"Order cost: ${order_cost}")

if __name__ == "__main__":
    main()