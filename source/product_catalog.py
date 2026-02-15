"""
Product Catalog

This module contains the ProductCatalog class.
"""


from product import Product


class ProductCatalog:
    """
    A product catalog is a collection of products.
    """

    def __init__(self):
        """
        Initialize a product catalog.
        """
        self.products = {}

    def add_product(self, product):
        """
        Add a product to the catalog.
        """
        self.products[product.get_title()] = product

    def get_product_by_title(self, title):
        """
        Get a product from the catalog by title.
        """
        if title not in self.products:
            raise ValueError(f"Product {title} not found in catalog")
        return self.products[title]

    def get_all_products(self):
        """
        Get all products from the catalog.
        """
        return list(self.products.values())

    def import_products(self, list_of_products):
        """
        Import products from a list of dictionaries.
        """
        for product in list_of_products:
            self.add_product(Product.from_dict(product))

    def print_products(self):
        """
        Print all products.
        """
        for product in self.products.values():
            print("--------------------------------")
            product.print_product()
