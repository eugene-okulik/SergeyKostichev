import random


if __name__ == "__main__":
    salary = int(input("What is your salary? "))
    is_bonus = bool(random.randint(0, 1))
    bonus = 0
    if is_bonus:
        bonus = int(random.random() * 100)

    print(salary, ",", is_bonus, "- $", salary + bonus)
