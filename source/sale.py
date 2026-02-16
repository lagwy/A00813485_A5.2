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

    def get_total(self, catalog):
        """
        Return the total amount for this sale using the catalog for prices.
        """
        total = 0
        for item in self.sale_items:
            line_total = item.line_total(catalog)
            if line_total is not None:
                total += line_total
        return total

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

    def print_sale(self, catalog):
        """
        Print the sale and its total (requires catalog for prices).
        """
        print(f"Sale ID: {self.sale_id}")
        print(f"Sale Date: {self.sale_date}")
        for sale_item in self.sale_items:
            product_name = sale_item.get_product()
            product = catalog.get_product_by_title(product_name)
            if product is None:
                print(f"Product {product_name} not found in catalog")
                continue
            unit_price = product.get_price()
            subtotal = sale_item.line_total(catalog)
            print(
                f"{sale_item.get_quantity()} x {product_name} "
                f"@ ${unit_price:.2f} = ${subtotal:.2f}"
            )
        print(f"Total: ${self.get_total(catalog):.2f}")
