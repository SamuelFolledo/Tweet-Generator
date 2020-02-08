from random import randint, choice, seed
seed(1) #for different random nums
import re #for changing lines to words list

def histogram(source_text): #source_text can either be a filename or contents of the file as string
    '''
    function which takes a source_text argument (can be either a filename or 
    the contents of the file as a string, your choice) and return a 
    histogram data structure that stores each unique word along with the 
    number of times the word appears in the source text.
    '''
    lines = source_text
    words = []
    for line in lines: #loop through each line
        words = re.sub("[^\w]", " ",  line).split() #turns every word in line to an array of words
    # ---------------------------- NOOB WAY ----------------------------
    # for word in words: #create a histogram from a list of words
    #     word_count = words_histogram.get(word, 0) + 1  #if word is in words_histogram's keys, count will increment, else equal 1
    #     words_histogram[word] = word_count
    # ---------------------------- ADVANCE WAY ----------------------------
    words_histogram = {} #type = {count:[word1, word2, word3,...]}
    for word in words:
        # for 
        print(f"WORD = {word}")
    return words_histogram

def unique_words(histogram): #{count: [word1,word2,word3,...]} histogram sample
    '''
    function that takes a histogram argument and returns the 
    total count of unique words in the histogram
    '''


def frequency(word, histogram): #{count: [word1,word2,word3,...]} histogram sample
    '''
    function that takes a word and histogram argument and 
    returns the number of times that word appears in a text
    '''
    frequency = 0



def get_random_words(amount):
    my_file = open("/Users/macbookpro15/Desktop/Tweet-Generator/words.txt", "r")
    lines = my_file.readlines()
    line = lines[0] 
    words = line.split() 
    line_returned = ""
    for i in range(amount):
        word = choice(words)
        if i < amount - 1: 
            line_returned += str(word + " ")
        else: #if we are at the last word
            line_returned += str(word + ".")
    print(f"Line Returned = {line_returned}")
    my_file.close()
    return line_returned

if __name__ == '__main__':
    histogram = histogram("one fish two fish red fish blue fish")
    print(f"HISTOGRAM = {histogram}")