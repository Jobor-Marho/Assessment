# Description: A class to represent a SalesOrder. Orders can
# be added and total revenue can be calculated.

class SalesOrder:
    """
    A class to represent a SalesOrder. Orders can be added and total revenue can be calculated."""
    def __init__(self):
        self.orders = []

    def add_order(self, orders: list):
        """
        Add orders to the SalesOrder object.
        -   Each order should contain an id and a list of items.
            -   Each item should contain a name, price, and quantity.
        """
        for order in orders:
            if 'id' in order and 'items' in order:
                for item in order["items"]:
                    if all(k in item for k in ["name", "price", "qty"]):
                        self.orders.append(order)
                        break  # Add the order once if items are valid
                else:
                    raise ValueError("Invalid item object supplied")
            else:
                raise ValueError("Invalid order object supplied")

    def calc_total_revenue(self):
        """
        Calculate the total revenue from all orders.
        """
        total = 0
        for order in self.orders:
            for item in order['items']:
                total += int(item['price']) * int(item['qty'])
        return total
