# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 11:02:32 2019

@author: Ranak Roy Chowdhury
"""
import numpy as np


# def starts_with(vocab, P_w1_w2, words, word, top_k):
def starts_with(vocab, P_w1_w2, words, word, top_k):
    # find the index of the word 'THE'
    idx = vocab.index(word)
    
    # find the indices of the highest k probailities
    highest_prob_indices = np.argsort(P_w1_w2[idx])[-top_k:]
    
    # find the highest probability values and 
    # the corresponding words based on the indices
    highest_prob_values = [P_w1_w2[idx][i] for i in highest_prob_indices]
    highest_prob_words = [vocab[words[idx][i]] for i in highest_prob_indices]
    print(highest_prob_values)
    print(highest_prob_words)
    
    
if __name__ == "__main__": 
    # read all required files
    from FileReader import FileReader
    file = FileReader()
    vocab, unigram, bigram = file.readAll()
    
    # compute the probability of each word
    from LanguageModel import LanguageModel
    lm = LanguageModel()
    P_w = lm.Unigram(unigram)
    vocab_size = len(vocab)

    P_w1_w2, words = lm.Bigram(bigram, vocab_size)
    
    # compute the probability of a word given 
    # that it starts with a specific letter
    word = 'THE'
    top_k = 10
    starts_with(vocab, P_w1_w2, words, word, top_k)
    