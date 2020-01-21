# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 09:41:13 2019

@author: Ranak Roy Chowdhury
"""

# File Reader Class
class FileReader:
    
    def readVocab(self):
        # Reading hw4_vocab.txt
        filename = "hw4_vocab.txt"
        with open(filename) as f:
            vocab = f.readlines()
            vocab = [x.strip() for x in vocab]
        return vocab
            
    def readUnigram(self):            
        # Reading hw4_unigram.txt
        filename = "hw4_unigram.txt"
        unigram = []
        with open(filename) as f:
            for line in f:
                unigram.append(int(line))
        return unigram
                
    def readBigram(self):
        # Reading hw4_bigram.txt
        filename = "hw4_bigram.txt"
        bigram = []
        with open(filename) as f:
            for line in f:
                line = line.split()
                line = [int(i) for i in line]
                bigram.append(line)
        return bigram
    
    def readAll(self):
        vocab = self.readVocab()
        unigram = self.readUnigram()
        bigram = self.readBigram()
        return vocab, unigram, bigram
                        
                    