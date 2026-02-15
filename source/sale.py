"""
Sales

This module contains the Sale class, which is a sale.
"""


from sale_item import SaleItem


class Sale:
    """
    A sale is a record of a sale.
    """

    def __init__(
        self,
        sale_id,
        sale_date,
    ):
        """
        Initialize a sale.
        """
        self.sale_id = sale_id
        self.sale_date = sale_date
        self.sale_items = []

    def add_sale_item(self, sale_item):
        """
        Add a sale item to the sale.
        """
        self.sale_items.append(sale_item)

    def get_sale_id(self):
        """
        Get the sale id of the sale.
        """
        return self.sale_id

    def get_sale_date(self):
        """
        Get the sale date of the sale.
        """
        return self.sale_date

    def get_sale_items(self):
        """
        Get the sale items of the sale.
        """
        return self.sale_items

    @staticmethod
    def from_dict(sale_row_dict):
        """
        Create a Sale from a single row (one sale item) dictionary.
        """
        sale = Sale(
            sale_row_dict["SALE_ID"],
            sale_row_dict["SALE_Date"]
        )
        sale.add_sale_item(SaleItem.from_dict(sale_row_dict))
        return sale

    def print_sale(self):
        """
        Print the sale.
        """
        print(f"Sale ID: {self.sale_id}")
        print(f"Sale Date: {self.sale_date}")
        for sale_item in self.sale_items:
            print(f"{sale_item.get_quantity()} x {sale_item.get_product()}")
