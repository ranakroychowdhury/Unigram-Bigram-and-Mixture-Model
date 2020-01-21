# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 10:54:13 2019

@author: Ranak Roy Chowdhury
"""


class LanguageModel:
    
    def Unigram(self, unigramCount):
        total = sum(unigramCount)
        P_w = [item/total for item in unigramCount]
        return P_w
    
    def Bigram(self, bigramCount, vocab_size):
        P_w1_w2 = []
        words = []
        for i in range(vocab_size):
            sublist = [item[2] for item in bigramCount if item[0] == i + 1]
            word = [item[1]-1 for item in bigramCount if item[0] == i + 1]
            total = sum(sublist)
            sublist = [item/total for item in sublist]
            P_w1_w2.append(sublist)
            words.append(word)
        return P_w1_w2, words
    
    
        
            
        