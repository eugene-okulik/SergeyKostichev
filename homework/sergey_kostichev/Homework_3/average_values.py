
if __name__ == "__main__":
    a = int(input("Enter value for a: "))
    b = int(input("Enter value for b: "))

    ar_average = (a + b)/2
    geo_average = (a * b)**(1/2)

    print("The arithmetic average value of", a, "and", b, "is", ar_average)
    print("The geometric average value of", a, "and", b, "is", geo_average)