"""
Exercise: Dataset Access Decision
Student: Amir Katuwal
Day: 1
"""

# Input Data

user_role = "manager"
is_active = False
requested_dataset = "salary_data"

allowed_roles = ["analyst", "scientist", "engineer"]
restricted_datasets = ["salary_data", "personal_data"]

# Access Decision

# Deny access immediately when the user's account is inactive.
if not is_active:
    access_decision = "Denied"
    decision_message = "Access denied because the user is inactive."

# Check whether the user's role is included in the list of allowed roles.
elif user_role not in allowed_roles:
    access_decision = "Denied"
    decision_message = "Access denied because the role is not allowed."

# Check whether the requested dataset is included in the restricted list.
elif requested_dataset in restricted_datasets:
    access_decision = "Denied"
    decision_message = "Access denied because the dataset is restricted."

# Grant access when all required conditions are satisfied.
else:
    access_decision = "Granted"
    decision_message = "Access granted."

# Output

print(f"User role: {user_role}")
print(f"Requested dataset: {requested_dataset}")
print(f"Access decision: {access_decision}")
print(decision_message)