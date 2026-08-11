"""
Exercise: Sales List Analysis
Student: Amir Katuwal
Day: 2
"""

# Input Data

monthly_sales = [85000, 120000, 95000, 140000, 75000, 160000]

# Sales Analysis

# Sort the sales amounts from highest to lowest.
ranked_sales = sorted(monthly_sales, reverse=True)

# Filter the sales amounts that are above NPR 100,000.
high_value_sales = [
    amount for amount in monthly_sales
    if amount > 100000
]

# Add 13% tax to each sales amount.
tax_inclusive_sales = [
    round(amount * 1.13, 2) for amount in monthly_sales
]

# Calculate the total sales amount.
total_revenue = sum(monthly_sales)

# Calculate the average sales amount.
average_revenue = total_revenue / len(monthly_sales)

# Output

print(f"Sales from highest to lowest: {ranked_sales}")
print(f"Sales above NPR 100000: {high_value_sales}")
print(f"Sales with 13% tax: {tax_inclusive_sales}")
print(f"Total sales: NPR {total_revenue:.2f}")
print(f"Average sales: NPR {average_revenue:.2f}")