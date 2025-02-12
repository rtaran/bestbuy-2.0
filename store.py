from products import Product # Import the Product class
from typing import List, Tuple

class Store:
    def __init__(self, products: List[Product]):
        """Initializes the store with a list of products."""
        self.products = products

    def add_product(self, product: Product):
        """Adds a new product to the store."""
        self.products.append(product)

    def remove_product(self, product: Product):
        """Removes a product from the store."""
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        """Returns the total number of items in the store."""
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self) -> List[Product]:
        """Returns all active products in the store."""
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list: List[Tuple[Product, int]]) -> float:
        """
        Processes an order, purchasing multiple products at once.
        :param shopping_list: A list of tuples [(Product, quantity)]
        :return: Total price of the order.
        """
        total_price = 0
        for product in shopping_list:
            product, quantity = product
            total_price += product.buy(quantity)

        return total_price