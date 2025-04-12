grades=[]
number_of_students=int(input('Number of students'))
for i in range(number_of_students):
    grade=int(input('student grade'))
    grades.append(grade)
Avarage=sum(grades)/number_of_students
Minimum= min(grades)
Maximum=max(grades)
print(Avarage)
print(Minimum)
print(Maximum)
for i, grade in enumerate(grades):
    if grade >=50:
        print(f'student number {i+1} is passed with grade {grade}')
    else:
        print(f'student number {i+1} failed with grade {grade}')
