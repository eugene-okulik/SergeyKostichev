from bouquet import Bouquet
from flowers import Daisy, Rose, Anduwanchik


if __name__ == "__main__":
    daisy1 = Daisy("white", 10, 50, 1, True)
    daisy2 = Daisy("blue", 8, 45, 0.8, False)
    # print(daisy1)
    # print(daisy2)

    rose1 = Rose("red", 45, 14, 4.5, True)
    rose2 = Rose("white", 43, 12, 4.2, True)
    # print(rose1)
    # print(rose2)

    dand1 = Anduwanchik("yellow", 10, 8, 0.4, False)
    dand2 = Anduwanchik("white", 10, 3, 0.9, True)
    # print(dand1)
    # print(dand2)

    bouquet1 = Bouquet(dand1, rose1, daisy2)
    print(bouquet1)

    bouquet1.sort_by_price()
    print(bouquet1)
    bouquet1.sort_by_length()
    print(bouquet1)
    bouquet1.sort_by_color()
    print(bouquet1)
    bouquet1.sort_by_fresh()
    print(bouquet1)

    bouquet1.find_by_color("yellow")
    bouquet1.find_by_color("red")

    bouquet1.find_by_price(3)
    bouquet1.find_by_price(0.1)
