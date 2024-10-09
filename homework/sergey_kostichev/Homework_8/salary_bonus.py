import random


salary = int(input("What is your salary? "))
is_bonus = random.choice([False, True])
bonus = 0
if is_bonus:
    bonus = int(random.random() * 100)

print(salary, ",", is_bonus, "- $", salary + bonus)
