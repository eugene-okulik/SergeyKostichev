
if __name__ == "__main__":
    for i in range(1, 101):
        txt = ""
        fuzz, buzz = "Fuzz", "Buzz"

        if i % 3 == 0:
            txt += fuzz
        if i % 5 == 0:
            txt += buzz
        if txt == "":
            txt = str(i)

        print(txt)
