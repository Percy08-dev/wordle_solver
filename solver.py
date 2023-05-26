import sys
from test import self_wordle

# 使用する辞書の作成
def init_word_list():
    path = "./data/wordle_words.txt"
    with open(path, "r", encoding="utf-8") as f:
        data = f.readlines()
    
    data = [i[:-1] for i in data]

    return data

# ===================================================================
# 辞書のアップデートブロック

# 辞書に単語を再保存するかを判別
def select(word, req:list):
    flag = True
    greens = []

    for (char, color, index) in req:
        if color == "green":
            greens.append(char)
        
        flag &= check(word, char, color, index, greens)

    return flag


# 単語の文字がヒントに合致するか判定
def check(word, char, color, index, greens):
    # print(word, char, color, index, greens)
    if char in greens:
        if color == "green":
            res = word[index] == char
        else:   # ここにはgrayのみ
            res = word[index] != char
    else:
        if color == "yellow":
            res = word[index] != char and char in word
        elif color == "gray":
            res = not(char in word)
        else:
            print("input error color!")
            sys.exit()

    return res


# 得られたヒントを元に単語リストを更新
def update_word_list(word_list, request):
    request.sort(key=lambda x:len(x[1]), reverse=True)        # yellow -> green -> grayの順にソート
    # print(request)
    word_list = [i for i in word_list if select(i, request)]

    return word_list


# ==============================================================
# 入力単語選択領域
# 単語から文字間共起を求めて, 共起関係の文字の和をxとして, xの値が大きいものを選択？
# 文字の出現数から求める方法は限界な気がする.

# max frequency char
def char_cnt(word_list):
    chars = dict()
    for i in word_list:
        c = set(i)
        for j in c:
            if j in chars:
                chars[j] += 1
            else:
                chars[j] = 1

    chars = list(chars.items())
    chars.sort(key = lambda x:x[1], reverse=True)
    print(chars[:5])

    return chars[:5]


# 出現頻度上位の単語を含む個数をスコア化
def ranking(word_list, char_list):
    chars = set([i[0] for i in char_list])

    res = [(word, len(chars & set(word))) for word in word_list]
    
    res.sort(key = lambda x:x[1], reverse=True)

    return res


# 出現頻度上位の単語を多く含む単語を選出
def get_next_word(word_list):
    chars = char_cnt(word_list)
    chars = list(chars)[:5]

    for i in reversed(range(5)):
        rate = ranking(word_list=word_list, char_list = chars[:i+1])
        if rate[0][1] == i + 1:
            return rate[0]

# ==========================================================
# テスト関係

# 試験実行
def self_execution():
    word_list = init_word_list()

    for _ in range(6):
        print(get_next_word(word_list))
        req = [input().split() for _ in range(5)]
        req = [(j[0], j[1], index) for index, j in enumerate(req)]
        print(req)

        word_list = update_word_list(word_list=word_list, request=req)
        print(len(word_list))
        print(word_list)


# 全パターンテスト
def all_test():
    pops = init_word_list()
    cnt = 0

    while len(pops) > 0:
        sol = pops.pop()
        word_list = init_word_list()
        for i in range(6):
            word = get_next_word(word_list)
            req = self_wordle(word[0], sol)
            if sum([1 for i in req if i[1] == "green"]) == 5:
                cnt += 1
                break

            word_list = update_word_list(word_list=word_list, request=req)
        else:
            print("残り単語数:{}, 対象単語:{}".format(len(word_list), sol))
            cnt += 1


def self_test():
    sol = input()
    word_list = init_word_list()
    for i in range(6):
        word = get_next_word(word_list)
        req = self_wordle(word[0], sol)
        # print(req)
        print(word[0], len(word_list))
        if sum([1 for i in req if i[1] == "green"]) == 5:
            cnt += 1
            break

        word_list = update_word_list(word_list=word_list, request=req)


def main():
    # self_execution()
    # all_test()
    self_test()

if __name__ == "__main__":
    main()