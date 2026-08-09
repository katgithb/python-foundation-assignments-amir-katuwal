"""
Exercise: Customer Record Cleaner
Student: Amir Katuwal
Day: 1
"""

# Input Data

raw_name = "  sAgar THAPA "
raw_city = "kATHMANDU "
raw_age = "27"
raw_email = " SAGAR@MAIL.COM "

# Customer Data Cleaning

# Remove surrounding spaces and standardize capitalization for the customer's name and city.
customer_name = raw_name.strip().title()
customer_city = raw_city.strip().title()

# Convert the age string to an integer after removing any surrounding spaces.
customer_age = int(raw_age.strip())

# Remove surrounding spaces and convert the email address to lowercase for consistency.
customer_email = raw_email.strip().lower()

# Customer Status

# Determine whether the customer is an adult or a minor based on their age.
age_status = "Adult" if customer_age >= 18 else "Minor"

# Output

print(f"Name: {customer_name}")
print(f"City: {customer_city}")
print(f"Age: {customer_age}")
print(f"Email: {customer_email}")
print(f"Status: {age_status}")