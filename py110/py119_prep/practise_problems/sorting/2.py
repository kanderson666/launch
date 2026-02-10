"""
Problem 2: Sort List of Dictionaries  3min to have both solutions (w and w/o lambda)
Difficulty: Intermediate

Create a function that takes a list of dictionaries, 
where each dictionary represents a student with 'name' and 'grade' keys. 
Return a new list of dictionaries sorted by the students' grades in descending order (highest grade first).

"""
def sort_students_by_grade(students):
    def sort_by_grade(student):
        return student['grade']

    # students.sort(key=lambda student: student['grade'], reverse=True)
    students.sort(key=sort_by_grade, reverse=True)
    return students

# Test Cases
students_1 = [
    {'name': 'Alice', 'grade': 91},
    {'name': 'Bob', 'grade': 84},
    {'name': 'Charlie', 'grade': 95},
]
expected_1 = [
    {'name': 'Charlie', 'grade': 95},
    {'name': 'Alice', 'grade': 91},
    {'name': 'Bob', 'grade': 84},
]
print(sort_students_by_grade(students_1) == expected_1)

students_2 = [
    {'name': 'David', 'grade': 78},
    {'name': 'Eve', 'grade': 89},
]
expected_2 = [
    {'name': 'Eve', 'grade': 89},
    {'name': 'David', 'grade': 78},
]
print(sort_students_by_grade(students_2) == expected_2)
print(sort_students_by_grade([]) == [])