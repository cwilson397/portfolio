#########################################
# Tuesday January 21st, 2025
# Simple sentance generator
# Programmed by Colby Wilson
#########################################

# importing the random library
import random

# picss a determiner/article
def get_article():
    
    # list of articles
    articles = ['A', 'One', 'The']
    return random.choice(articles)


# picks a noun
def get_noun():

    # a collection of nouns
    nouns = ['cat', 'dog', 'man', 'woman', 'bird', 'girl', 'boy', 'animal', 'car']
    return random.choice(nouns)

# picks a verb
def get_verb():

    # a collection of verbs
    verbs = ['Laughs', 'Laughed', 'ate', 'drank', 'flew', 'ran', 'wrote', 'eats', 'drinks', 'flies', 'runs', 'writes', 'thinks', 'looks', 'talks']
    return random.choice(verbs)

# makes the sentance
def make_sentence():

    # make a random sentance with above functions
    determiner = get_article()
    noun = get_noun()
    verb = get_verb()
    return f"{determiner} {noun} {verb}"

# main
def main():

    # generates the six random sentances and prints them
    for _ in range(6):
        print(make_sentence())

main()