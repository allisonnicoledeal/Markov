#!/usr/bin/env python

import sys
from random import choice


def make_chains(corpus, number):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    text_list = corpus.split()
    d = {}
    num_words = int(number)

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
        # text.append(convert[:]) # append convert to random text
        link = (link[-1],next_link) #reassign link and repeat while loop

    return " ".join(text)

def make_tweet(text):
    tweet = text[-140:]
    cap_it = tweet[0].capitalize()
    return cap_it + tweet[1:]

def main():
    script, filename, num_words = sys.argv
    f = open(filename)
    input_text = f.read()
    f.close() 

    chain_dict = make_chains(input_text, num_words)
    random_text = make_text(chain_dict)
    tweet = make_tweet(random_text)
    print tweet

if __name__ == "__main__":
    main()











