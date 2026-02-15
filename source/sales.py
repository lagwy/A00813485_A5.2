"""
Sales Record

This module contains the Sales class.
"""


from sale import Sale


class Sales:
    """
    A sales is a collection of sales.
    """

    def __init__(self):
        """
        Initialize a sales.
        """
        self.sales = {}

    def add_sale(self, sale):
        """
        Add a sale to the sales.
        If a sale with the same sale_id already exists,
        only its items are added.
        """
        sale_id = sale.get_sale_id()
        if sale_id in self.sales:
            existing_sale = self.sales[sale_id]
            for item in sale.get_sale_items():
                existing_sale.add_sale_item(item)
        else:
            self.sales[sale_id] = sale

    def get_sale_by_sale_id(self, sale_id):
        """
        Get a sale from the sales by sale id.
        """
        if sale_id not in self.sales:
            raise ValueError(f"Sale {sale_id} not found in sales record")
        return self.sales[sale_id]

    def get_all_sales(self):
        """
        Get all sales from the sales.
        """
        return list(self.sales.values())

    def import_sales(self, list_of_sales):
        """
        Import sales from a list of dictionaries.
        """
        for sale in list_of_sales:
            self.add_sale(Sale.from_dict(sale))

    def print_sales(self):
        """
        Print all sales.
        """
        for sale in self.sales.values():
            print("--------------------------------")
            sale.print_sale()
