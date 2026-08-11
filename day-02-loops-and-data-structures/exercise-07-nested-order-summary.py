"""
Exercise: Nested Order Summary
Student: Amir Katuwal
Day: 2
"""

# Input Data

orders = {
    "ORD-001": {
        "customer": "Anisha",
        "amount": 2500,
        "status": "Completed"
    },
    "ORD-002": {
        "customer": "Ravi",
        "amount": 1800,
        "status": "Pending"
    },
    "ORD-003": {
        "customer": "Maya",
        "amount": 3200,
        "status": "Completed"
    }
}

# Order Analysis

# Display each order ID along with its customer.
print("All orders:")
for order_id, order_details in orders.items():
    print(f"{order_id}: {order_details['customer']}")

# Find completed orders and calculate their total amount.
completed_total = 0

print("\nCompleted orders:")
for order_id, order_details in orders.items():
    if order_details["status"] == "Completed":
        print(f"{order_id}: {order_details['customer']} - NPR {order_details['amount']}")
        completed_total += order_details["amount"]

# Count orders that are still pending.
pending_count = 0

for order_details in orders.values():
    if order_details["status"] == "Pending":
        pending_count += 1

# Add a new order to the existing order dictionary.
orders["ORD-004"] = {
    "customer": "Shyam",
    "amount": 2100,
    "status": "Pending"
}

# Output

print(f"\nTotal completed order amount: NPR {completed_total}")
print(f"Pending orders: {pending_count}")
print(f"New order added: ORD-004 - {orders['ORD-004']['customer']} - NPR {orders['ORD-004']['amount']} - {orders['ORD-004']['status']}")