def main():
    path = "word.txt"
    with open(path, "r", encoding="utf-8") as f:
        data = f.readline()

    data = data.replace('"', "")[1:-1]
    data = data.replace(",", "\n") + "\n"
    
    with open("./wordle_words.txt", "w", encoding="utf-8") as f:
        f.write(data)


if __name__ == "__main__":
    main()