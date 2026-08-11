"""
Exercise: Dataset Comparison
Student: Amir Katuwal
Day: 2
"""

# Input Data

dataset_a = {
    "customer",
    "sales",
    "product",
    "employee"
}

dataset_b = {
    "sales",
    "product",
    "supplier",
    "inventory"
}

# Dataset Comparison

# Combine both datasets to find every unique dataset name.
all_dataset_names = dataset_a | dataset_b

# Find the dataset names shared by both groups.
shared_dataset_names = dataset_a & dataset_b

# Find the dataset names that exist only in the first group.
first_group_only = dataset_a - dataset_b

# Find the dataset names that exist only in the second group.
second_group_only = dataset_b - dataset_a

# Output

print(f"All unique dataset names: {all_dataset_names}")
print(f"Datasets found in both groups: {shared_dataset_names}")
print(f"Datasets only in dataset A: {first_group_only}")
print(f"Datasets only in dataset B: {second_group_only}")