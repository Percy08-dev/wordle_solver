def cnt(word:str):
    aiueo = ['a', 'i', 'u', 'e', 'o']
    cnt = 0
    
    for i in aiueo:
        if i in word:
            cnt += 1
    
    return (word, cnt)


def main():
    path = "./data/wordle_words.txt"
    

    with open(path, "r", encoding="utf-8") as f:
        data = f.readlines()
    
    res = [cnt(i) for i in data]
    res.sort(key=lambda x:x[1], reverse=True)

    [print(i) for i in res[:10]]

if __name__ == "__main__":
    main()