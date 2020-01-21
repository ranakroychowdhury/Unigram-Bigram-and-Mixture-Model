# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 17:37:47 2019

@author: Ranak Roy Chowdhury
"""
import math
from matplotlib import pyplot
from matplotlib.pyplot import figure


# calculate log-likelihood under unigram
def log_likelihood_unigram(word_list, P_w, vocab):
    # find the indices of all the words in word_list in the vocabulary
    indices = [vocab.index(element) for element in word_list]
    result = 1
    for index in indices:
        result *= P_w[index]

    return result


# calculate log-likelihood under bigram
def log_likelihood_bigram(word_list, P_w1_w2, words, vocab):
    
    result = 1
    for i in range(len(word_list) - 1):
        # find the index of the word and the next word in the vocab list
        index_actual_word = vocab.index(word_list[i])
        index_next_word = vocab.index(word_list[i+1])
        
        # find the index of the next word in the words list
        if(index_next_word in words[index_actual_word]):
            index_next_word_wordslist = words[index_actual_word].index(index_next_word)
            result *= P_w1_w2[index_actual_word][index_next_word_wordslist]
        # if the word pair doesn't exist, replace the next word with <UNK>
        else:
            print(word_list[i] + ' ' + word_list[i+1])
            result = 0    
    return result


# calculate log_likelihood under mixture model
def log_likelihood_mixture_model(word_list, P_w, P_w1_w2, words, vocab, alpha):
    
    result = 1
    for i in range(len(word_list)-1):
        res_uni = log_likelihood_unigram(list(word_list[i+1].split(" ")), P_w, vocab)
        res_bi = log_likelihood_bigram(word_list[i:i+2], P_w1_w2, words, vocab)
        answer = alpha * res_uni + (1 - alpha) * res_bi
        result *= answer
    return result
    

# plot figure    
def plot_figure(alpha, result):
    fig = pyplot.gcf()
    fig.set_size_inches(20, 15)
    ax1 = fig.add_subplot(211)
    
    ax1.set_ylabel('L_m')
    ax1.set_xlabel('Values of Lambda')
    
    pyplot.plot(alpha, result)
    pyplot.show()
    
    
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
    
    sentence = 'The sixteen officials sold fire insurance'
    word_list = sentence.upper().split()
    
    
    # calculate log-likelihood under unigram
    result_unigram = log_likelihood_unigram(word_list, P_w, vocab)
    print("Log-likelihood under unigram model is " + str(math.log(result_unigram)))
    
    # calculate log-likelihood under bigram
    word_list.insert(0, '<s>')
    result_bigram = log_likelihood_bigram(word_list, P_w1_w2, words, vocab)
    if(result_bigram != 0):
        print("Log-likelihood under bigram model is " + str(math.log(result_bigram)))
    else:
        print("Log-likelihood under bigram model is negative infinity")
    
    
    # calculate log_likelihood under mixture model
    alpha = list(range(1,100))
    alpha = [i * 0.01 for i in alpha]
    result = []
    for i in alpha:
        ans = log_likelihood_mixture_model(word_list, P_w, P_w1_w2, words, vocab, i)
        result.append(math.log(ans))
    plot_figure(alpha, result)
    max_value = max(result)
    max_index = result.index(max_value)
    opt_alpha = alpha[max_index]
    
    print('Maximum value of log-likelihood is ' + str(max_value))
    print('Optimal value of lambda is ' + str(opt_alpha))
    