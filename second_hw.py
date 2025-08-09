student1=str(input('enter name: '))
grade1=int(input('enter number: '))
grade2=int(input('enter number: '))
grade3=int(input('enter number: '))
grades1=[grade1,grade2,grade3]
student2=str(input('enter name: '))
grade_1=int(input('enter number: '))
grade_2=int(input('enter number: '))
grade_3=int(input('enter number: '))
grades2=[grade_1,grade_2,grade_3]
print()
print()
my_dict={student1:grades1,
         student2:grades2}
print()
student=input('enter name : ')
if student in my_dict.keys() :
    student_grades=my_dict.get(student)
    print(f'{student} grades : {student_grades}')
    print()
    max_grade=max(my_dict.get(student))
    print(f'max grade : {max_grade}')
    print()
    min_grade = min(my_dict.get(student))
    print(f'min grade : {min_grade}')
    print()
    average_grades=sum(my_dict.get(student))/len(my_dict.get(student))
    print(f'average grades : {average_grades}')

else :
    print(f'error')