def main():
    path = "./english-words/words.txt"
    with open(path, "r" , encoding="utf-8") as f:
        words = f.readlines()

    res = [i.lower() for i in words if len(i) == 6 and i[:-1].isalpha()]

    with open("./data/wordle_words.txt", "w", encoding="utf-8") as f:
        f.writelines(res)

if __name__ == "__main__":
    main()