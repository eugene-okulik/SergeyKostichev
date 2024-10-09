def fibonacci():
    a = 0
    b = 1
    while True:
        yield a + b
        a, b = b, a + b


keys = [5, 200, 1000, 100000]
count = 1
for number in fibonacci():
    count += 1
    if count in keys:
        print(count, number)
    if count == keys[-1]:
        break
