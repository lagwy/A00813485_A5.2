"""
Compute sales

This program reads two files:
1. a catalog of products and their prices in JSON format.
2. a record of all sales in the company in JSON format.
It calculates the total cost for all sales.
"""

import sys
import time
import json
from io import StringIO

from product_catalog import ProductCatalog
from sales import Sales


def read_catalog(catalog_file):
    """Read the catalog file and return a list of products."""
    catalog = {}

    try:
        with open(catalog_file, 'r', encoding='utf-8') as file:
            catalog = json.load(file)
    except json.JSONDecodeError:
        print(f"Error: {catalog_file} is not a valid JSON file.")
        sys.exit(1)
    except FileNotFoundError:
        print(f"Error: {catalog_file} file not found.")
        sys.exit(1)
    except Exception as error:
        print(f"Error: {error}")
        sys.exit(1)
    return catalog


def load_catalog(catalog_file):
    """Load the catalog from the file and return a ProductCatalog object."""
    catalog = read_catalog(catalog_file)
    product_catalog = ProductCatalog()
    product_catalog.import_products(catalog)
    return product_catalog


def load_sales(sales_file):
    """Load the sales from the file and return a Sales object."""
    sales = read_sales(sales_file)
    sales_collection = Sales()
    sales_collection.import_sales(sales)
    return sales_collection


def read_sales(sales_file):
    """Read the sales from the file and return a list of sales."""
    sales = []

    try:
        with open(sales_file, 'r', encoding='utf-8') as file:
            sales = json.load(file)
    except json.JSONDecodeError:
        print(f"Error: {sales_file} is not a valid JSON file.")
        sys.exit(1)
    except FileNotFoundError:
        print(f"Error: {sales_file} file not found.")
        sys.exit(1)
    except Exception as error:
        print(f"Error: {error}")
        sys.exit(1)
    return sales


def write_results_to_file(sales_output, elapsed_time,
                          filename="SalesResults.txt"):
    """Write sales output and elapsed time to a file."""
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(sales_output)
        file.write(f"Elapsed time: {elapsed_time:.3f} seconds\n")


def main():
    """Main function to run the calculations."""
    # Check the command line arguments
    if len(sys.argv) != 3:
        print("Usage: python computeSales.py <catalog_file> <sales_file>")
        sys.exit(1)

    catalog_file = sys.argv[1]
    sales_file = sys.argv[2]

    # Start timing
    start_time = time.time()

    # Load the catalog
    product_catalog = load_catalog(catalog_file)

    # Load the sales
    sales = load_sales(sales_file)
    sales.set_catalog(product_catalog)

    # Capture sales print output for file and console
    buffer = StringIO()
    old_stdout = sys.stdout
    sys.stdout = buffer
    sales.print_sales()
    sys.stdout = old_stdout
    sales_output = buffer.getvalue()
    print(sales_output, end="")

    # End timing
    end_time = time.time()
    elapsed_time = end_time - start_time

    # Print the elapsed time
    print(f"Elapsed time: {elapsed_time:.3f} seconds")

    # Write results to file (sales output + total + elapsed time)
    write_results_to_file(sales_output, elapsed_time)


if __name__ == "__main__":
    main()
