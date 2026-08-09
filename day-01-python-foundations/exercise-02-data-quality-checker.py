"""
Exercise: Data Quality Checker
Student: Amir Katuwal
Day: 1
"""

# Input Data

total_rows = 2000
missing_rows = 120
duplicate_rows = 30

# Data Quality Calculations

# Add missing and duplicate rows to find the total number of problematic rows.
# Missing and duplicate rows are assumed not to overlap.
data_issue_rows = missing_rows + duplicate_rows

data_issue_rate = (data_issue_rows / total_rows) * 100

# Classify the dataset based on the percentage of problematic rows.
if data_issue_rate <= 2:
    quality_rating = "Excellent"
elif data_issue_rate <= 5:
    quality_rating = "Acceptable"
else:
    quality_rating = "Needs Cleaning"

# Output

print(f"Total rows: {total_rows}")
print(f"Problematic rows: {data_issue_rows}")
print(f"Problem percentage: {data_issue_rate:.2f}%")
print(f"Final classification: {quality_rating}")