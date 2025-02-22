from classes import StockManager

if __name__ == "__main__":
    # Create a StockManager object
    stock_manager = StockManager([(10, 100), (20, 200), (30, 300)])
                                #  qty price  qty price  qty price

    # Approve a sale of 25 items
    try:
        approved_stock = stock_manager.get_next_batch(25)
        print(f"Approved stock: {approved_stock}")
    except ValueError as e:
        print(f"Error: {e}")

    # Approve a sale of 40 items
    try:
        approved_stock = stock_manager.get_next_batch(40)
        print(f"Approved stock: {approved_stock}")
    except ValueError as e:
        print(f"Error: {e}")