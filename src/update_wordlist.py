import sys

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
