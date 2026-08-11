"""
Exercise: Student Score Dictionary
Student: Amir Katuwal
Day: 2
"""

# Input Data

student_scores = {
    "Anish": 78,
    "Ravi": 55,
    "Shyam": 92,
    "Sagar": 61,
    "Rima": 48
}

# Student Score Analysis

# Display each student's name and their score.
print("Student scores:")
for student_name, score in student_scores.items():
    print(f"{student_name}: {score}")

# Keep only students who meet the minimum passing score of 60.
passing_students = {
    student_name: score
    for student_name, score in student_scores.items()
    if score >= 60
}

# Find the student whose score is the highest.
top_student = max(
    student_scores,
    key=student_scores.get
)

highest_score = student_scores[top_student]

# Calculate the average score across all students.
score_total = sum(student_scores.values())
average_score = score_total / len(student_scores)

# Output

print(f"\nPassing students: {passing_students}")
print(f"Highest-scoring student: {top_student}")
print(f"Highest score: {highest_score}")
print(f"Average score: {average_score:.2f}")