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

# Data Cleaning Using List Comprehension

# Filter the same valid integer values using a concise list comprehension.
cleaned_values_compact = [
    value for value in raw_values
    if isinstance(value, int)
]

# Output

print(f"Cleaned values using loop: {cleaned_values}")
print(f"Cleaned values using list comprehension: {cleaned_values_compact}")