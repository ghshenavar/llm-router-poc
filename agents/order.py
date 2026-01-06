def order_status(order_id: str) -> str:
    orders = {
        "12345": "Shipped",
        "67890": "Processing",
        "54321": "Delivered",
    }
    status = orders.get(order_id, "Order not found.")
    return f"Order {order_id} status: {status}"
