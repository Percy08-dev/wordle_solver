# 入力単語選択領域
# 単語から文字間共起を求めて, 共起関係の文字の和をxとして, xの値が大きいものを選択？
# 文字の出現数から求める方法は限界な気がする.

# 出現頻度上位の文字を多く含む単語を選出
import re


def get_next_word_mono_gram(word_list):
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
        # print(chars[:5])

        return chars[:5]


    # 出現頻度上位の単語を含む個数をスコア化
    def ranking(word_list, char_list):
        chars = set([i[0] for i in char_list])

        res = [(word, len(chars & set(word))) for word in word_list]
        
        res.sort(key = lambda x:x[1], reverse=True)

        return res

    
    chars = char_cnt(word_list)
    chars = list(chars)[:5]

    for i in reversed(range(5)):
        rate = ranking(word_list=word_list, char_list = chars[:i+1])
        if rate[0][1] == i + 1:
            return rate[0]


# 文字bi-gramで決定
# -> mono-gramの方が成績が良い
def get_next_word_bi_gram(word_list):
    # cut bi gram
    def bi_gram_cnt(word_list):
        bi_grams = dict()
        for word in word_list:
            for i in range(0, 4):
                bg = word[i:i+2]
                if bg in bi_grams:
                    bi_grams[bg] += 1
                else:
                    bi_grams[bg] = 1
        
        bi_grams = list(bi_grams.items())
        bi_grams.sort(key=lambda x:x[1], reverse=True)

        return [i[0] for i in bi_grams[:5]]
    
    def get_bi_gram(word):
        res = [word[i:i+2] for i in range(len(word)-1)]
        return res

    def ranking(word_list, bi_gram):
        bi_gram = set(bi_gram)

        res = [(i, len(bi_gram & set(get_bi_gram(i)))) for i in word_list]
        res.sort(key=lambda x:x[1], reverse=True)

        return res

    bi_gram = bi_gram_cnt(word_list)

    for i in reversed(range(5)):
        rate = ranking(word_list, bi_gram[:i+1])
        
        if rate[0][1] == i+1:
            return rate[0]



# 使用可能な文字種を最初に削減する
def reduse_char(word_list, using,  req):
    def char_cnt(word_list):
        chars = dict()
        for i in word_list:
            c = set(i)
            for j in c:
                if j in chars:
                    chars[j] += 1
                else:
                    chars[j] = 1

        return chars


    def score(word, chars):
        res = 0

        for i in word:
            res += chars[i]

        return res


    def ranking(word_list, using, req, chars):
        # usingの更新
        for i in req:
            if i[1] != "gray":
                using.add(i[0])

        res = [(word, score(word, chars)) for word in word_list if len(set(word) & using) == 0]
        
        res.sort(key = lambda x:x[1], reverse=True)

        return res

    chars = char_cnt(word_list)
    rate = ranking(word_list, using, req, chars)
    
    if len(rate) == 0:
        return
    else:
        return rate[0]