from __future__ import division, print_function
from random import randint, choice, seed
seed(1) #for different random nums
import re #for changing lines to words list

class Histogram(dict): #create Histogram class from a dictionary
    def __init__(self, lines=None): #line is a string
        """Initialize this histogram as a new list and count given words."""
        super(Histogram, self).__init__()  # Initialize this as a new list
        # Add properties to track useful word counts for this histogram
        self.unique_words_count = 0  #count of unique word #types
        self.words_count = 0  #total count of all words #tokens
        self.words = [] #list of words
        if lines != None: #if list is not empty, update our properties
            words_from_line = re.sub("[^\w]", " ",  lines).split() #turns every word in line to an array of words
            for word in words_from_line: #loop through each word and get the histogram
                self.add_count(word)
    
    def add_count(self, word, count=1):
        """Increase frequency count of given word by given count amount."""
        # word_count = self.histogram.get(word, 0) + count  #if word is in words_histogram's keys, count will increment, else equal 1
        # self.histogram[word] = word_count
        if self.frequency(word) > 0:
            self[word] += count
        else:
            self[word] = count
            self.unique_words_count += 1
        self.words_count += count

    def frequency(self, word):
        """Return frequency count of given word, or 0 if word is not found."""
        if not self.__contains__(word):
            return 0
        frequency = self[word]
        return frequency

    def __contains__(self, word):
        """Return boolean indicating if given word is in this histogram."""
        for word_history in self:
            if word == word_history:
                return True
        return False

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
        print(word)


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
    # histogram = histogram("one fish two fish red fish blue fish")
    # print(f"HISTOGRAM = {histogram}")
    myGram = Histogram("one fish two fish red fish blue fish")
    print(f"Histogram = {myGram}")
    print(f"Unique words count = {myGram.unique_words_count}")
    print(f"Words count = {myGram.words_count}")