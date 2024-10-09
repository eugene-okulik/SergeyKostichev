def print_results(txt):
    print("Result: ", int(txt[txt.index(": ") + 2:]) + 10)


if __name__ == "__main__":
    examples = ["результат операции: 42",
                "результат операции: 54",
                "результат работы программы: 209"]

    for example in examples:
        print_results(example)
