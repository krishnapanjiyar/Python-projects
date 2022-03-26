import string
from graph import Graph, Vertex

def get_words_from_text(text_path):
    with open(text_path, 'r') as f:
        text = f.read()

        text = ' '.join(text.split()) # this is saying turn whitespaces into just spaces
        text = text.lower() # make everything lowercase to compare stuff
        # now we could be complex and deal with punctuations... but there are cases where
        # you might add a period such as (Mr. Brightside), but that's not really
        # punctuation... so we just remove all the punctuation
        # hello! it's me. --> hello its me
        text = text.translate(str.maketrans('', '', string.punctuation))

    words = text.split()    # split on spaces again
    return words

def make_graph(words):
    g = Graph()

    previous_word = None

    # for each word
    for word in words:
        # check that word is in the graph, and if not then add it
        word_vertex = g.get_vertex(word)
    # if there was a previous word, then add an edge if it does not already exist
    # in the graph, otherwise increment weight by 1
    if previous_word:
        previous_word.increment_egde(word_vertex)

    # set our word to the previous word and iterate!
    previous_word = word_vertex

    # now remember that we want to generate the probability mappings before composing
    # this is a great place to do it before we return the graph object
    g.generate_probability_mappings()

    return g

def main():
    # step 1: get words from text
    # step 2: make a graph using those words
    # step 3: get the next word for x number of words(defined by user)
    # step 4: show the user!
    pass