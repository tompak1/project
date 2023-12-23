

from db import create_table_db, read_db
from product_manager import manage_products
import pprint
# from shopping_cart import add_item, remove_item, checkout
NAME_DATABASE = "Tickets.csv"

if __name__ == "__main__":
    create_table_db("Tickets", ["name", "count", "price_per_one", "sold"])
    data = read_db(NAME_DATABASE)

    pprint.pprint(data)
    manage_products()
