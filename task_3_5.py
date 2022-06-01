from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(n):
    jokes_list = []
    for i in range(n):
        random_noun = choice(nouns)
        random_adverb = choice(adverbs)
        random_adjective = choice(adjectives)
        joke = f'{random_noun} {random_adverb} {random_adjective}'
        print(joke)
                      
get_jokes(3)