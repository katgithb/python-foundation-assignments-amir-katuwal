"""
Exercise: Sales Summary
Student: Amir Katuwal
Day: 1
"""

# Input Data
product_name = "Wireless Mouse"
unit_price = 1500
quantity_sold = 12
discount_percentage = 0.10

# Sales Calculations

# Calculate total revenue before any reduction.
total_sales = unit_price * quantity_sold

# Apply the discount rate to the gross sales to find the discount amount.
discount_value = total_sales * discount_percentage

# Subtract the discount from gross sales to get the actual amount earned.
net_sales = total_sales - discount_value

# Output
print(f"Product: {product_name}")
print(f"Gross sales: NPR {total_sales:.2f}")
print(f"Discount: NPR {discount_value:.2f}")
print(f"Final sales: NPR {net_sales:.2f}")