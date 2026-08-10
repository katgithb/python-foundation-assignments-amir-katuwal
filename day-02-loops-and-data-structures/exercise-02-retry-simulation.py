"""
Exercise: Retry Simulation
Student: Amir Katuwal
Day: 2
"""

# Input Data

attempt = 1
max_attempts = 3
operation_successful = False

# Retry Processing

# Continue retrying while attempts remain.
while attempt <= max_attempts:
    print(f"Attempt {attempt}")

    # Simulate a successful operation on the second attempt.
    if attempt == 2:
        operation_successful = True

    # Exit the loop when the operation is successful.
    if operation_successful:
        break

    # Move to the next attempt when the current attempt is unsuccessful.
    attempt += 1

# Output

if operation_successful:
    print("Operation completed successfully")
else:
    print("Operation failed after three attempts")