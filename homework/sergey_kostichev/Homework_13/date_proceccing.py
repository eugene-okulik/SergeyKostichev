import os
import datetime


file_name = 'data.txt'
base_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
file_path = os.path.join(base_path, 'eugene_okulik', 'hw_13', file_name)


def give_answer(func):
    def wrapper(*args):
        print("Answer: ", end="")
        func(*args)
        print()
    return wrapper


def read_datafile(path):
    with open(path, 'r', encoding='utf-8') as data_file:
        for line in data_file.readlines():
            if '\n' not in line:
                line += '\n'
            print(line)
            yield line


@give_answer
def print_date_week_later(dat):
    new_date = dat + datetime.timedelta(days=7)
    print(new_date)


@give_answer
def print_day_of_week(dat):
    day_of_week = dat.strftime('%A')
    print(day_of_week)


@give_answer
def print_how_many_days_ago(dat):
    days_ago = (datetime.datetime.now() - dat).days
    print(days_ago)


for data_line in read_datafile(file_path):
    data_line = data_line.split()
    date = data_line[1] + " " + data_line[2]
    py_date = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f')
    match data_line[0]:
        case '1.':
            print_date_week_later(py_date)
        case '2.':
            print_day_of_week(py_date)
        case '3.':
            print_how_many_days_ago(py_date)
        case _:
            print('There is no action')
