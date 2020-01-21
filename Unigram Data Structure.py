# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 10:08:18 2019

@author: Ranak Roy Chowdhury
"""


# compute the probability of a word given 
# that it starts with a specific letter
def starts_with(vocab, P_w, letter):
    # words that start with 'M'
    result = [i for i in vocab if i.startswith(letter)]

    # indices of words that start with M
    index = []
    for element in result:
        index.append(vocab.index(element))
    
    # extract the probabilities of each word that starts with 'M'
    P_w_starts_with_M = [P_w[i] for i in index]
    
    # store the 'M' word and its probability as key-value pair in dictionary
    table = dict()
    i = 0
    for item in result:
        table[item] = P_w_starts_with_M[i]
        i += 1

    print(table)

    
if __name__ == "__main__": 
    # read all required files
    from FileReader import FileReader
    file = FileReader()
    vocab, unigram, bigram = file.readAll()
    
    # compute the probability of each word
    from LanguageModel import LanguageModel
    lm = LanguageModel()
    P_w = lm.Unigram(unigram) 
    
    # compute the probability of a word given 
    # that it starts with a specific letter
    letter = 'M'
    starts_with(vocab, P_w, letter) 
    
    
    