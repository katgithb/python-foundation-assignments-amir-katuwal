"""
Exercise: Pipeline Health Status
Student: Amir Katuwal
Day: 1
"""

# Input Data

rows_loaded = 9900
rows_failed = 100
runtime_minutes = 30

# Pipeline Health Calculations

# Combine successfully loaded and failed rows to find the total rows processed.
processed_rows = rows_loaded + rows_failed

pipeline_issue_rate = (rows_failed / processed_rows) * 100

# Pipeline Status

# Classify the pipeline status based on the failure rate and runtime.
if pipeline_issue_rate > 5:
    pipeline_status = "Critical"
elif pipeline_issue_rate <= 2 and runtime_minutes <= 20:
    pipeline_status = "Healthy"
else:
    pipeline_status = "Warning"

# Output

print(f"Failure rate: {pipeline_issue_rate:.2f}%")
print(f"Final pipeline status: {pipeline_status}")