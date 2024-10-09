def print_results(txt):
    index = txt.index(": ")
    txt = txt[index + 2:]
    result = int(txt) + 10

    print(result)


example1 = "результат операции: 42"
example2 = "результат операции: 514"
example3 = "результат операции: 9"

examples = [example1, example2, example3]
for example in examples:
    print_results(example)
