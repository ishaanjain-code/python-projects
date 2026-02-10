def student_data():
    num_student=int(input("Enter number of students: "))
    students={}
    for i in range(num_student):
        name=input("\nenter name of the student: ")
        students[name]={}
        num_subjects=int(input(f"\nenter number of subjects for {name}: "))
        for j in range(num_subjects):
            subject=input("\nenter name of subject: ")
            students[name][subject]=int(input(f"\nenter marks for {subject}: "))
    return students
def percentage(students):
    full_marks=int(input("enter the maximum marks of one subject: "))
    for name , subjects in students.items():
        total_marks=sum(subjects.values())
        max_marks=len(subjects)*full_marks
        percentage=total_marks/max_marks*100
        print(f"total percentage of {name}= " ,percentage)
data=student_data()
total_percentage=percentage(data)
if 90<=total_percentage>=100:
    print("grade: A+")
elif 80<=total_percentage<90:
    print("grade: A")
elif 70<=total_percentage>80:
    print("grade: B+")
elif 60<=total_percentage>70:
    print("grade: B")   
elif 50<=total_percentage>60:
    print("grade: C")
elif 40<=total_percentage>50:
    print("grade: D")
else:
    print("grade: F(fail)")