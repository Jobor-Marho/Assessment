#Script to create a SalesOrder object for orders with multiple items and calculate total revenue. Also demonstrates error handling.

from classes import SalesOrder

if __name__ == "__main__":
    # Create a SalesOrder object
    sales_order = SalesOrder()

    # Add orders to the SalesOrder object
    orders = [
        {"id": 1, "items": [{"name": "item1", "price": 10, "qty": 2}]},
        {"id": 2, "items": [{"name": "item2", "price": 20, "qty": 1}, {"name": "item3", "price": 30, "qty": 3}]},
        {"id": 3, "items": [{"name": "item4", "price": 30, "qty": 4}]},
    ]
    # Error handling for invalid orders or items.
    try:
        sales_order.add_order(orders)
        # Calculate total revenue
        total_revenue = sales_order.calc_total_revenue()
        print(f"Total revenue: ${total_revenue}")
    except ValueError as e:
        print(f"Error: {e}")

