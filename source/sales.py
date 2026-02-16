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
        self.catalog = None

    def set_catalog(self, catalog):
        """
        Set the product catalog used for totals and printing.
        """
        self.catalog = catalog

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
            return None
        return self.sales[sale_id]

    def get_all_sales(self):
        """
        Get all sales from the sales.
        """
        return list(self.sales.values())

    def get_total(self):
        """
        Return the grand total for all sales using the catalog for prices.
        """
        if self.catalog is None:
            raise ValueError("Catalog not set; call set_catalog() first")
        return sum(
            sale.get_total(self.catalog) for sale in self.sales.values()
            )

    def import_sales(self, list_of_sales):
        """
        Import sales from a list of dictionaries.
        """
        for sale in list_of_sales:
            self.add_sale(Sale.from_dict(sale))

    def print_sales(self):
        """
        Print all sales and their totals (requires catalog to be set).
        """
        if self.catalog is None:
            raise ValueError("Catalog not set; call set_catalog() first")
        for sale in self.sales.values():
            print("--------------------------------")
            sale.print_sale(self.catalog)
        print("--------------------------------")
        print(f"Grand Total: ${self.get_total():.2f}")
        print("--------------------------------")
