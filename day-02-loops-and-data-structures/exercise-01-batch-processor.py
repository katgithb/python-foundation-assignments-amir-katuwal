"""
Exercise: Batch Processor
Student: Amir Katuwal
Day: 2
"""

# Input Data

batch_limit = 10
checkpoint_interval = 3

# Batch Processing

# Process each batch from 1 through the configured batch limit.
for batch_number in range(1, batch_limit + 1):
    print(f"Processing batch {batch_number}")

    # Display a checkpoint after every checkpoint_interval batches.
    if batch_number % checkpoint_interval == 0:
        print("Checkpoint reached")