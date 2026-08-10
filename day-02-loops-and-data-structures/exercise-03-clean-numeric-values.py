"""
Exercise: Clean Numeric Values
Student: Amir Katuwal
Day: 2
"""

# Input Data

raw_values = [100, None, 250, "invalid", 300, None, 450]

# Data Cleaning Using a Loop

cleaned_values = []

# Check each value and skip anything that is not an integer.
for value in raw_values:
    if not isinstance(value, int):
        continue

    cleaned_values.append(value)

# Output

print(f"Cleaned values using loop: {cleaned_values}")