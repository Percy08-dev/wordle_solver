def init_word_list():
    path = "../data/wordle_words.txt"
    with open(path, "r", encoding="utf-8") as f:
        data = f.readlines()
    
    data = [i[:-1] for i in data]

    return data