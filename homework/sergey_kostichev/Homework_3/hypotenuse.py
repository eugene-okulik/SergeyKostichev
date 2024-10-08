
if __name__ == "__main__":
    a = int(input("Enter value for a: "))
    b = int(input("Enter value for b: "))

    hypotenuse = (a*a + b*b)**(1/2)
    area = (a * b)/2

    print("Hypotenuse of a right triangle with legs", a, "and", b, "is", hypotenuse)
    print("Area of a right triangle with legs", a, "and", b, "is", area)
