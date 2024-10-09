template = 'Students {0} study these subjects: {1}'

students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']

students_str = ", ".join(students)
subjects_str = ", ".join(subjects)

print(template.format(students_str, subjects_str))
