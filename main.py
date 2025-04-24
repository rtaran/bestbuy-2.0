from products import Product, NonStockedProduct, LimitedProduct, PercentDiscount, SecondHalfPrice, ThirdOneFree
from store import Store

# Create promotions
second_half_price = SecondHalfPrice("Second Half price!")
third_one_free = ThirdOneFree("Third One Free!")
thirty_percent_off = PercentDiscount("30% off!", 30)

# Setup initial stock of inventory
product_list = [
    Product("MacBook Air M2", price=1450, quantity=100),
    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    Product("Google Pixel 7", price=500, quantity=250),
    NonStockedProduct("Windows License", price=125),
    LimitedProduct("Shipping", price=10, quantity=1000, maximum=1)
]

# Apply promotions to products
product_list[0].promotion = second_half_price
product_list[1].promotion = third_one_free
product_list[3].promotion = thirty_percent_off

# Create a Store instance
best_buy = Store(product_list)

def list_products(store):
    print("------")
    products = store.get_all_products()
    if not products:
        print("🚫 No products available.")
    else:
        for idx, product in enumerate(products, start=1):
            print(f"{idx}. {product}")
    print("------")

def show_total_quantity(store):
    total_quantity = store.get_total_quantity()
    print("\n---------------------------------------")
    print(f"✨ TOTAL AMOUNT IN STORE: {total_quantity} items ✨")
    print("---------------------------------------")

def make_order(store):
    products = store.get_all_products()
    shopping_list = []

    if not products:
        print("🚫 No products available to order.")
        return

    print("------")
    for idx, product in enumerate(products, start=1):
        print(f"{idx}. {product}")
    print("------")

    while True:
        product_num = input("Which product # do you want? (Press Enter to finish order) ")
        if product_num.strip() == "":
            break

        try:
            product_num = int(product_num)
            if product_num < 1 or product_num > len(products):
                print("❌ Invalid product number, please try again.")
                continue

            quantity = input("What amount do you want? ")
            quantity = int(quantity)
            selected_product = products[product_num - 1]
            shopping_list.append((selected_product, quantity))
            print("Product added to list!")
        except ValueError:
            print("❌ Invalid input. Please enter a valid number.")

    if shopping_list:
        try:
            total_price = store.order(shopping_list)
            print(f"✅ Order placed successfully! Total cost: ${total_price:.2f}")
        except ValueError as e:
            print(f"❌ Order failed: {e}")
    else:
        print("❌ No items were ordered.")

def quit_program():
    print("👋 Goodbye! Thank you for shopping at Best Buy 🛒")
    exit()

def start(store: Store):
    """
    Starts the user interface for interacting with the store.
    :param store: Store object containing the inventory
    """
    menu_options = {
        "1": lambda: list_products(store),
        "2": lambda: show_total_quantity(store),
        "3": lambda: make_order(store),
        "4": quit_program
    }

    while True:
        print("\n   Store Menu   ")
        print("   ----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose a number: ")
        action = menu_options.get(choice)
        if action:
            action()
        else:
            print("❌ Invalid choice, please enter a number between 1-4.")

if __name__ == "__main__":
    start(best_buy)