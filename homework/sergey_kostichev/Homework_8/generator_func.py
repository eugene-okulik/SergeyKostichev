def fibonacci():
    a = 0
    b = 1
    counter = 0
    while counter < 100001:
        counter += 1
        yield a + b
        a, b = b, a + b


if __name__ == "__main__":
    keys = [5, 200, 1000, 100000]
    count = 1
    for number in fibonacci():
        count += 1
        if count in keys:
            print(count, number)
