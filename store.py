from typing import List, Tuple
from products import Product, NonStockedProduct


class Store:
    """Class representing a store with products."""

    def __init__(self, products: List[Product]):
        """
        Initializes the store with a list of products.

        :param products: List of products to initialize the store with
        """
        self._products = products

    @property
    def products(self) -> List[Product]:
        """
        Get the list of products in the store.

        :return: List of products
        """
        return self._products

    @products.setter
    def products(self, new_products: List[Product]):
        """
        Set the list of products in the store.

        :param new_products: New list of products
        """
        self._products = new_products

    def add_product(self, product: Product):
        """
        Adds a new product to the store.

        :param product: Product to add
        """
        self._products.append(product)

    def remove_product(self, product: Product):
        """
        Removes a product from the store.

        :param product: Product to remove
        """
        self._products.remove(product)

    def get_total_quantity(self) -> int:
        """
        Returns the total number of items in the store.

        :return: Total quantity of all active products
        """
        return sum(product.quantity for product in self._products if product.is_active)

    def get_all_products(self) -> List[Product]:
        """
        Returns all active products in the store.

        :return: List of active products with quantity > 0 or non-stocked products
        """
        return [product for product in self._products 
                if product.is_active and 
                (product.quantity > 0 or isinstance(product, NonStockedProduct))]

    def order(self, shopping_list: List[Tuple[Product, int]]) -> float:
        """
        Processes an order, purchasing multiple products at once.

        This method consolidates quantities for the same product and then
        processes the order by calling the buy method on each product.

        :param shopping_list: A list of tuples [(Product, quantity)]
        :return: Total price of the order
        """
        total_price = 0

        # Consolidate quantities for the same product
        consolidated_list = {}
        for product, quantity in shopping_list:
            if product in consolidated_list:
                consolidated_list[product] += quantity
            else:
                consolidated_list[product] = quantity

        # Process the consolidated order
        for product, quantity in consolidated_list.items():
            total_price += product.buy(quantity)

        return total_price
