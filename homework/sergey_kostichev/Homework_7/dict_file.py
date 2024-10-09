
if __name__ == "__main__":
    words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}

    for word, value in words.items():
        word *= value
        print(word)
