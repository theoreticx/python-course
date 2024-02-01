student_score = {
"Ivan": 5.00,
"Alex": 3.50,
"Maria": 5.50,
"Georgy": 5.00
}

#for student, grade in student_score.items():
#    if grade > 4:
#        print(f'{student} - {grade}')
        
        
#####################################################################################################
        
grades = set(student_score.values())
min_grade = min(grades)
max_grade = max(grades)

for student, grade in student_score.items():
    
    grades = set(student_score.values())
    min_grade = min(grades)
    max_grade = max(grades)
    
    if grade == max_grade:
        print(f'{student} - {max_grade}')
    elif grade == min_grade:
        print(f'{student} - {min_grade}')