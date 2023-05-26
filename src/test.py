# ソルバー関係
from init import init_word_list 
from update_wordlist import update_word_list
from choise import get_next_word_mono_gram, get_next_word_bi_gram, reduse_char

# ローカルでのシミュレータ
from wordle_simulator import self_wordle

# 手動で入力するテスト
def self_execution():
    word_list = init_word_list()

    for _ in range(6):
        print(get_next_word_mono_gram(word_list))
        req = [input().split() for _ in range(5)]
        req = [(j[0], j[1], index) for index, j in enumerate(req)]
        print(req)

        word_list = update_word_list(word_list=word_list, request=req)
        print(len(word_list))
        # print(word_list)


# 全パターンテスト
def all_test():
    pops = init_word_list()
    cnt = 0

    while len(pops) > 0:
        sol = pops.pop()
        word_list = init_word_list()
        using = set()
        req = []
        for i in range(6):
            if i < 4:
                word = reduse_char(word_list, using, req)
                if word == None :
                    word = get_next_word_mono_gram(word_list)
            else:
                word = get_next_word_mono_gram(word_list)
            
            
            req = self_wordle(word[0], sol)
            if sum([1 for i in req if i[1] == "green"]) == 5:
                cnt += 1
                break

            word_list = update_word_list(word_list=word_list, request=req)
        else:
            print("残り単語数:{}, 対象単語:{}".format(len(word_list), sol))
            cnt += 1


if __name__ == "__main__":
    self_execution()
    # all_test()