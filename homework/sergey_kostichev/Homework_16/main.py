from sql_connection import SQLConnection
import csv
import os


def read_csv(path, datas):
    with open(path, newline='') as csvfile:
        csv_data = csv.reader(csvfile)
        for row in csv_data:
            datas.append(row)


if __name__ == "__main__":
    file_name = 'data.csv'
    base_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    file_path = os.path.join(base_path, 'eugene_okulik', 'Lesson_16', 'hw_data', file_name)
    datas = []

    read_csv(file_path, datas)
    db = SQLConnection()

    query_template = '''
                    SELECT *
                    FROM students s
                    JOIN `groups` g ON g.id = s.group_id
                    JOIN books b ON b.taken_by_student_id = s.id
                    JOIN marks m ON m.student_id = s.id
                    JOIN lessons l ON l.id = m.lesson_id
                    JOIN subjets s2 ON l.subject_id = s2.id
                    WHERE s.name = %s AND s.second_name = %s
                    AND g.title = %s AND b.title = %s
                    AND s2.title = %s AND l.title = %s
                    AND m.value = %s
                '''

    for index in range(1, len(datas)):
        line = datas[index]
        name = line[0]
        second_name = line[1]
        group_title = line[2]
        book_title = line[3]
        subject_title = line[4]
        lesson_title = line[5]
        mark_value = line[6]

        values = (name, second_name, group_title, book_title,
                  subject_title, lesson_title, mark_value)

        result = db.find_by_query(query_template, values)
        if len(result) == 0:
            print(line)

    db.close_db()
