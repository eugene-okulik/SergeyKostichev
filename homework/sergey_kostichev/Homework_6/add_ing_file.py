
if __name__ == "__main__":
    text = ("Etiam tincidunt neque erat, quis molestie enim imperdiet vel. "
            "Integer urna nisl, facilisis vitae semper at, dignissim vitae libero")
    ing = "ing"
    transformed_text = []

    for word in text.split():
        if "," in word or "." in word:
            word = word.replace(",", ing + ",")
            word = word.replace(".", ing + ".")
        else:
            word += ing
        transformed_text.append(word)

    print(" ".join(transformed_text))
