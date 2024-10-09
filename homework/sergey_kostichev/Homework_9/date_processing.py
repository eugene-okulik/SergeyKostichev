from datetime import datetime


template_date = "Jan 15, 2023 - 12:05:33"
py_date = datetime.strptime(template_date, '%b %d, %Y - %H:%M:%S')
print(py_date.strftime('%B'))
human_date = py_date.strftime('%d.%m.%Y, %H:%M')
print(human_date)
