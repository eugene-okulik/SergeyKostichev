def repeat_me(func):
    def wrapper(txt, count=1): # почему у меня не сработал *args как параметр? txt, count = args
        for t in range(count):
            func(txt)
    return wrapper


@repeat_me
def example(text):
    print(text)


example('print me', count=4)
