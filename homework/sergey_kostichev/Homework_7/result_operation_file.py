import random


def guess_number(number: int):
    template = "{0} is {1} the right answer"

    while True:
        result = ""
        user_answer = int(input("Guess number in range 1, 100: "))
        if user_answer < number:
            result = "less than"
        elif user_answer > number:
            result = "more than"
        else:
            break
        print(template.format(user_answer, result))


if __name__ == "__main__":
    min_number, max_number = 1, 100
    rand_number = random.randint(min_number, max_number)

    guess_number(rand_number)
    print("Congratulations! You have guessed the number!")
