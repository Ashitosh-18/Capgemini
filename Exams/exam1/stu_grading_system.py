def cal_grade(percentage):
    if percentage >= 90:
        return 'A'
    elif percentage >= 75:
        return 'B'
    elif percentage >= 50:
        return 'C'
    else:
        return 'Fail'
    
    
def main():
    student_name = input("Enter the student's name: ")
    
    marks = []
    for i in range(1, 6):
        mark = int(input(f"Enter marks for subject {i}: "))
        marks.append(mark)
    
    total_marks = sum(marks)
    percentage = (total_marks / 500) * 100
    
    grade = cal_grade(percentage)
    
    print(f"\nStudent Name: {student_name}")
    print(f"Total Marks: {total_marks}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")

main()
