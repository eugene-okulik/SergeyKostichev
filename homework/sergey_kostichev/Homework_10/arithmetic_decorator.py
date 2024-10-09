def operations(func):
    def wrapper(*args):
        f, s = int(args[0]), int(args[1])
        op = ''
        if f == s:
            op = '+'
        elif f > s:
            op = '-'
        elif f < s:
            op = '/'
        if f < 0 or s < 0:
            op = '*'
        return func(*args, op)

    return wrapper


@operations
def calc(first, second, operation):
    return first + operation + second


a, b = input("Type two numbers, like '10 30': ").split()

expression = calc(a, b)
print(expression, "=", eval(expression))
