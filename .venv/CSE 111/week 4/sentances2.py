#######################################################
# Tuesday January 28th, 2025
# Simple sentance generator with prepositional phrases
# Programmed by Colby Wilson
#######################################################


# importing the random library
import random

# picks a determiner/article
def get_article():
    # list of articles
    articles = ['A', 'One', 'The', 'Some', 'Many']
    return random.choice(articles)

# picks a noun
def get_noun():
    # a collection of nouns
    nouns = ['cat', 'dog', 'man', 'woman', 'bird', 'girl', 'boy', 'animal', 'car', 'rabbit', 'child', 'children', 'dogs', 'cats']
    return random.choice(nouns)

# picks a verb
def get_verb():
    # a collection of verbs
    verbs = ['laughs', 'laughed', 'ate', 'drank', 'flew', 'ran', 'wrote', 'eats', 'drinks', 'flies', 'runs', 'writes', 'thinks', 'looks', 'talks', 'will laugh', 'will run', 'will eat', 'will drink']
    return random.choice(verbs)

# picks a preposition
def get_prepo():
    # a collection of prepositions
    prepositions = ['on', 'above', 'below', 'under', 'beside', 'with', 'about', 'for', 'at', 'off', 'in', 'by']
    return random.choice(prepositions)

# creates the prepositional phrase
def get_prepo_phrase():
    # calls previous functions
    preposition = get_prepo()
    determiner = get_article().lower() # makes the article lowercase
    noun = get_noun()
    return f"{preposition} {determiner} {noun}"

# completes the sentance
def make_sentance():
    # calls get article, noun, verb, and prepo phrase
    determiner = get_article()
    noun = get_noun()
    verb = get_verb()
    prepo_phrase = get_prepo_phrase()
    return f"{determiner} {noun} {verb} {prepo_phrase}."

# main
def main():
    # generations six random sentances and prints them out
    for _ in range(6):
        print(make_sentance())

main()