# Description: A class to manage stock batches and approve sales based on available stock.

from collections import deque

class StockManager:
    """
    A class to manage stock batches and approve sales based on available stock.
    """
    def __init__(self, batch: list):
        """
        Initialize the StockManager with stock batches.

        Args:
            batch (list): List of tuples (quantity, price) for each stock batch.
        """
        self.batches = deque(batch)  # FIFO structure for stock management
        self.total_stock = sum(qty for qty, _ in self.batches)

    def get_next_batch(self, sale_qty_needed: int):
        """
        Approves stock for a sale based on FIFO.

        Args:
            sale_qty_needed (int): The quantity required for the sale.

        Returns:
            list: Tuples of (used_quantity, price) from the stock.

        Raises:
            ValueError: If requested quantity exceeds available stock or is invalid.
        """
        if sale_qty_needed <= 0:
            raise ValueError("Sale quantity must be greater than zero.")

        if sale_qty_needed > self.total_stock:
            raise ValueError("Insufficient stock for the requested sale.")

        used_batch = []
        remaining_qty_needed = sale_qty_needed

        while remaining_qty_needed > 0 and self.batches:
            current_qty, price = self.batches.popleft()

            if current_qty <= remaining_qty_needed:
                # Use the entire batch
                used_batch.append((current_qty, price))
                self.total_stock -= current_qty
                remaining_qty_needed -= current_qty
            else:
                # Use part of the batch
                used_batch.append((remaining_qty_needed, price))
                self.batches.appendleft((current_qty - remaining_qty_needed, price))
                self.total_stock -= remaining_qty_needed
                remaining_qty_needed = 0

        return used_batch


