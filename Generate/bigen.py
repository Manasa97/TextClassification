#!/usr/bin/env python3
# encoding: utf-8
 
import sys

from pprint import pprint
from random import choice


EOS = ['.', '?', '!']
 
 
def build_dict(words):
    """
    Build a dictionary from the words.
 
    (word1, word2) => [w1, w2, ...]  # key: tuple; value: list
    """
    d = {}
    for i, word in enumerate(words):
        try:
            first, second = words[i], words[i+1]
        except IndexError:
            break
        key = (first)
        if key not in d:
            d[key] = []
        #
        d[key].append(second)
 
    return d
 
 
def generate_sentence(d):
    count=0
    li = [key for key in d.keys() if key[0][0].isupper()]
    key = choice(li)
    li = []
    first= key
    li.append(first)
    #li.append(second)
    while True:
        try:
            second = choice(d[key])
        except KeyError:
            break
        li.append(second)
        if second[-1] in EOS:
            count=count+1
            if (count==5):
                break
        # else
        key = (second)
        first= key
 
    return ' '.join(li)
 
 
def main(fname):
    #fname = sys.argv[1]
    with open(fname, "rt") as f:
        text = f.read()
 
    words = text.split()
    d = build_dict(words)
    #pprint(d)
    print()
    sent = generate_sentence(d)
    print(sent)
    if sent in text:
        print('# existing sentence :(')
 
####################
 
if __name__ == "__main__":
    # filename='corpus.txt'
    f = 'words_0.txt'
    main(f)
