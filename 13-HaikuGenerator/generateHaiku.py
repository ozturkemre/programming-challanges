from random import randint


def choose(word_list):
    return word_list[randint(-1, len(word_list) - 1)]


words1 = ["sessizlik", "suskunluk", "durgunluk", "sahipsiz", "yalnızlık", "mutluluk", "rengarenk", "mutsuzluk"]
words2 = ["hakim", "nedir", "sensiz", "benlik"]
words3 = ["bir başına", "tek başına", "yapayalnız", "umutsuzca"]
words4 = ["sen ve ben", "burada"]
words5 = ["hayat geçiyor", "gökyüzüm sensin", "yağmur gibisin", "sahibim sensin", "sonsuzluk gibi"]

haiku = choose(words1) + " " + choose(words2) + "\n" + choose(words3) + " " + choose(words4) + "\n" + choose(words5)
print(haiku)
