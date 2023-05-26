import sys

"""
word: 比較対象単語
solution: 正答単語
比較単語と正答単語を入力し, 文字ごとに判別を行う. 

yellowの判定部分にバグあり
"""

def self_wordle(word, solution):
    word = list(word)
    res = []
    green_list = []
    if len(word) != len(solution):
        print("@@@ ERROR! @@@", word, solution)
        sys.exit()

    for i in range(len(word)):
        if word[i] == solution[i]:
            res.append((word[i], "green", i))
            green_list.append(word[i])
        elif word[i] in solution and not(word[i] in green_list):
            res.append((word[i], "yellow", i))
        else:
            res.append((word[i], "gray", i))

    return res