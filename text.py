from random import choice, randint


def make_chains(corpus, num_words):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    text_list = corpus.split()
    d = {}

    for w in range(len(text_list)):
        if w <= (len(text_list) - (num_words +1)): # stops iteration before
        # error is thrown (len:30, want w to stop at 27 if num_words == 2)
            tuple_key = tuple(text_list[w:w+num_words])
            if d.get(tuple_key) == None: # if dict key doesn't exist
                d[tuple_key] = [text_list[w+num_words]] # creates key w/
                # list of num_words as a value
            else:
                d[tuple_key].append(text_list[w+num_words]) # else appends
                # w+num_words-th item in text_list to value list
    return d

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""

    link = choice(chains.keys())
    next_link = 'the'
    text = list(link)

    while link in chains or (next_link[-1] not in ('!','.','?')):
        next_link = choice(chains[link])
        text.append(next_link)
        link = (link[len(link)],next_link) #reassign link and repeat while loop

    return " ".join(text)

new_text = """
    I am lost.
    I have gone to find myself.
    If I should return, before I get back,
    please ask me to wait."""

test_chains = make_chains(new_text, 2)
make_text(test_chains)