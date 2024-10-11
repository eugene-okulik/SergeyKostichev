import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor()

query = "INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)"
values = ('Autopython Video Course', 'October 2024', 'October 2124')
cursor.execute(query, values)
current_group_id = cursor.lastrowid

students = [
    ('Sasha', 'Lisunova', current_group_id),
    ('Masha', 'Borodinova', current_group_id),
    ('Dasha', 'Prjevalskaya', current_group_id),
    ('Glasha', 'Miroslavskaya', current_group_id),
    ('Cheburasha', 'Mandarinova', current_group_id),
]

insert_student = "INSERT INTO students (name, second_name, group_id) VALUES (%s, %s, %s)"
student_ids = []

for student in students:
    cursor.execute(insert_student, student)
    student_ids.append(cursor.lastrowid)

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

insert_subject = "INSERT INTO subjets (title) VALUES (%s)"
subjet_ids = []

subjets = ['Mathematics', 'Physics', 'Spanish']
for subject in subjets:
    cursor.execute(insert_subject, (subject,))
    subjet_ids.append(cursor.lastrowid)

lessons = [
    ('Lesson Basics', subjet_ids[0]),
    ('Lesson Advanced', subjet_ids[0]),
    ('Lesson Optics', subjet_ids[1]),
    ('Lesson Thermodynamics', subjet_ids[1]),
    ('Spanish B1', subjet_ids[2]),
    ('Spanish B2', subjet_ids[2]),
]

insert_lesson = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
lesson_ids = []

for lesson in lessons:
    cursor.execute(insert_lesson, lesson)
    lesson_ids.append(cursor.lastrowid)

print("Inserted lesson IDs:", lesson_ids)

marks = [
    (8, lesson_ids[0], student_ids[0]),
    (9.9, lesson_ids[0], student_ids[0]),
    (8, lesson_ids[1], student_ids[1]),
]

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

update_student = "UPDATE students SET name = 'Sergey' WHERE id = %s"
cursor.execute(update_student, (student_ids[0],))

# Удаляю всех добавленных студентов, но только теоретически. Можно выбрать пару из добавленных, если указать диапазон
'''for student_id_ in student_ids:
        delete_student = "DELETE FROM students WHERE id = %s"
        cursor.execute(delete_student, (student_id_,))'''

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
