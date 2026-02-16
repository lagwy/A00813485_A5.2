"""
SaleItem

This module contains the SaleItem class, which is a sale item.
"""


class SaleItem:
    """
    A sale item is a item that was sold.
    """

    def __init__(
        self,
        product,
        quantity
    ):
        """
        Initialize a sale item.
        """
        self.product = product
        self.quantity = quantity

    @staticmethod
    def from_dict(sale_item_dict):
        """
        Create a sale item from a dictionary.
        """
        return SaleItem(
            sale_item_dict["Product"],
            sale_item_dict["Quantity"]
        )

    def get_product(self):
        """
        Get the product of the sale item.
        """
        return self.product

    def get_quantity(self):
        """
        Get the quantity of the sales record.
        """
        return self.quantity

    def line_total(self, catalog):
        """
        Return the line total (quantity * unit price) using the catalog.
        """
        product = catalog.get_product_by_title(self.product)
        if product is None:
            return None
        return self.quantity * product.get_price()
