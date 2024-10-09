def finish_me(func):
    def wrapper(*txt):
        func(*txt)
        print(f"finished")
    return wrapper


@finish_me
def example(text):
    print(text)


example("don't print me")
