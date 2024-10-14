import random

import mysql.connector as mysql
from faker import Faker


db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor()

fake = Faker()

num_students = 5
student_ids = []
students = []
for _ in range(num_students):
    name = fake.first_name()
    second_name = fake.last_name()
    students.append((name, second_name, None))

#1. Добавляю студентов без айди группы
insert_student = "INSERT INTO students (name, second_name, group_id) VALUES (%s, %s, %s)"
for student in students:
    cursor.execute(insert_student, student)
    student_ids.append(cursor.lastrowid)

#2. Добавляю группу и сохраняю айди созданной группы
query = "INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)"
values = ('Autopython Video Course', 'Oct 2024', 'Осt 2124')
cursor.execute(query, values)
current_group_id = cursor.lastrowid

#3. Добавляю всех студентов в эту новую группу, используя сохраненные айди группы и айди студентов
update_student_group = "UPDATE students SET group_id = %s WHERE id = %s"
for student in student_ids:
    cursor.execute(update_student_group, (current_group_id, student))
db.commit()

#4. Назначаю книги студентам по их айди
book_ids = []
for student_id_ in student_ids:
    books = [
        ('C++ Superbook', student_id_),
        ('Java Megabook', student_id_),
        ('Rust Wow-book', student_id_),
        ('Python Just a book', student_id_),
    ]
    insert_book = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
    for book in books:
        cursor.execute(insert_book, book)
        book_ids.append(cursor.lastrowid)

#5. Добавляю предметы
insert_subjet = "INSERT INTO subjets (title) VALUES (%s)"
subjet_ids = []

subjets = ['Mathematics', 'Physics', 'Spanish']
for subject in subjets:
    cursor.execute(insert_subjet, (subject,))
    subjet_ids.append(cursor.lastrowid)

#5. Добавляю уроки
lessons = [
    ('Lesson Basics', subjet_ids[0]),
    ('Lesson Advanced', subjet_ids[0]),
    ('Lesson Optics', subjet_ids[1]),
    ('Lesson Thermodynamics', subjet_ids[1]),
    ('Spanish B1', subjet_ids[2]),
    ('Spanish B2', subjet_ids[2]),
]

#6. Распределяю уроки по предметам
insert_lesson = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
lesson_ids = []
for lesson in lessons:
    cursor.execute(insert_lesson, lesson)
    lesson_ids.append(cursor.lastrowid)

#7. Добавляю оценки используя айди уроков и студентов
marks = []
for student in student_ids:
    for lesson in lesson_ids:
        marks.append((random.randint(1, 10), lesson, student))

insert_mark_query = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
for mark in marks:
    cursor.execute(insert_mark_query, mark)

select_student_and_lessons = """
SELECT *
FROM students s
JOIN lessons l ON s.group_id = l.subject_id
WHERE s.group_id = %s AND l.subject_id = %s
"""
cursor.execute(select_student_and_lessons, (current_group_id, subjet_ids[2]))
students_lessons = cursor.fetchall()
for row in students_lessons:
    print(row)

update_student = "UPDATE students SET name = %s WHERE id = %s"
cursor.execute(update_student, (fake.first_name(), student_ids[0],))

select_marks = "SELECT * FROM marks WHERE student_id = %s"
cursor.execute(select_marks, (student_ids[0],))
marks_result = cursor.fetchall()
for row in marks_result:
    print(row)

select_books = "SELECT * FROM books WHERE taken_by_student_id = %s"
cursor.execute(select_books, (student_ids[0],))
books_result = cursor.fetchall()
for row in books_result:
    print(row)

multiline_selection = """
SELECT *
FROM students s
JOIN marks m ON m.student_id = s.id
JOIN books b ON b.taken_by_student_id = s.id
JOIN `groups` g ON g.id = s.group_id
JOIN lessons l ON m.lesson_id = l.id
JOIN subjets s2 ON l.subject_id = s2.id
WHERE s.id = %s
"""

cursor.execute(multiline_selection, (student_ids[0],))
complex_result = cursor.fetchall()
for row in complex_result:
    print(row)

db.commit()
db.close()
