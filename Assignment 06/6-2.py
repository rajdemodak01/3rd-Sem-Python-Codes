def calculate_average(marks_list):
    return sum(marks_list) / len(marks_list)

def calculate_grade(average_score):
    if average_score >= 90:
        return "A"
    elif average_score >= 80:
        return "B"
    elif average_score >= 70:
        return "C"
    elif average_score >= 60:
        return "D"
    else:
        return "F"

# students = [
#     {
#         'name': "James Potter",
#         "assignment": [82, 56, 44, 30],
#         "test": [80, 80],
#         "lab": [67.90, 78.72]
#     },
#     # Add more student dictionaries here
# ]

# for student in students:
#     assignment_score = calculate_average(student["assignment"])
#     test_score = calculate_average(student["test"])
#     lab_score = calculate_average(student["lab"])

#     final_score = (0.1 * assignment_score) + (0.7 * test_score) + (0.2 * lab_score)
#     grade = calculate_grade(final_score)

#     print(f"{student['name']} - Average Marks: {final_score:.2f} - Grade: {grade}")


def take_dictionary_input():
    repl_dict = {}
    num_entries = int(input("Enter the number of entries in the dictionary: "))
    
    for i in range(num_entries):
        key = input("Enter key {}: ".format(i + 1))
        value = input("Enter value for key {}: ".format(i + 1))
        repl_dict[key] = value
    
    return repl_dict

students = take_dictionary_input()
print("Dictionary:", students)
print(list(students["assignment"]))
assignment_score=calculate_average(list(students["assignment"]))
test_score=calculate_average(students["test"])
lab_score=calculate_average(students["lab"])
final_score = (0.1 * assignment_score) + (0.7 * test_score) + (0.2 * lab_score)
grade = calculate_grade(final_score)

print(f"{students['name']} - Average Marks: {final_score:.2f} - Grade: {grade}")