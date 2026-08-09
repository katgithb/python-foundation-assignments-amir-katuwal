"""
Exercise: File Validator
Student: Amir Katuwal
Day: 1
"""

# Input Data

file_name = input("Enter a file name: ")

# File Validation

# Remove surrounding spaces and convert the filename to lowercase
# so the extension check works consistently for different user input.
file_name = file_name.strip().lower()

supported_formats = (".csv", ".json", ".parquet")

# Check whether the filename ends with one of the supported file formats.
if file_name.endswith(supported_formats):
    validation_result = "Valid file format"
else:
    validation_result = "Invalid file format"

# Output

print(f"File: {file_name}")
print(f"Validation result: {validation_result}")