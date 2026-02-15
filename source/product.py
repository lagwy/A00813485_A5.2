"""
Product

This module contains the Product class, which is a product.
"""


class Product:
    """
    A product is a item that can be sold.
    """

    def __init__(
        self,
        title,
        product_type,
        description,
        filename,
        height,
        width,
        price,
        rating
    ):
        """
        Initialize a product.
        """
        self.title = title
        self.product_type = product_type
        self.description = description
        self.filename = filename
        self.height = height
        self.width = width
        self.price = price
        self.rating = rating

    @staticmethod
    def from_dict(product_dict):
        """
        Create a product from a dictionary.
        """
        return Product(
            product_dict["title"],
            product_dict["type"],
            product_dict["description"],
            product_dict["filename"],
            product_dict["height"],
            product_dict["width"],
            product_dict["price"],
            product_dict["rating"]
        )

    def get_title(self):
        """
        Get the title of the product.
        """
        return self.title

    def get_type(self):
        """
        Get the type of the product.
        """
        return self.product_type

    def get_description(self):
        """
        Get the description of the product.
        """
        return self.description

    def get_filename(self):
        """
        Get the filename of the product.
        """
        return self.filename

    def get_height(self):
        """
        Get the height of the product.
        """
        return self.height

    def get_width(self):
        """
        Get the width of the product.
        """
        return self.width

    def get_price(self):
        """
        Get the price of the product.
        """
        return self.price

    def get_rating(self):
        """
        Get the rating of the product.
        """
        return self.rating
