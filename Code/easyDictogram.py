# from __future__ import division, print_function  # Python 2 and 3 compatibility
from random import randint
# import re #for changing lines to words list

class EasyDictogram(dict):
    """Dictogram is a histogram implemented as a subclass of the dict type."""

    def __init__(self, word_list):
        '''Initializes the dictogram properties'''

        self.word_list = word_list
       
        self.dictionary_histogram = self.build_dictogram()

        self.tokens = sum(self.dictionary_histogram.values())
        self.types = self.unique_words()

    def build_dictogram(self): #REQUIRED
        '''Creates a histogram dictionary using the word_list property and returns it'''
        dictionary_histogram = {}
        for word in self.word_list:
            word_count = dictionary_histogram.get(word, 0)
            if word_count > 0:
                dictionary_histogram[word] += 1
            else: #if new word
                dictionary_histogram[word] = 1
        # print("Returning... ", dictionary_histogram)
        return dictionary_histogram

    def frequency(self, word): #REQUIRED
        '''returns the frequency or count of the given word in the dictionary histogram'''
        #TODO: use your frequency function as a starting point to complete this method
        word_count = self.dictionary_histogram.get(word, 0)
        return word_count

    def unique_words(self): #REQUIRED
        '''returns the number of unique words in the dictionary histogram'''
        #TODO: use your unique words function as a starting point to complete this method
        # print("Unique words = ", len(self.dictionary_histogram))
        return len(self.dictionary_histogram)

    def sample(self):  #REQUIRED
        '''Randomly samples from the dictionary histogram based on the frequency, returns a word'''
        #TODO: use your sample function as a starting point to complete this method 
        sum_of_values = sum(self.dictionary_histogram.values()) #word_counts.values() returns a list of word_count's values. sum() will sum a the values in a list and returns an int
        random_num = randint(0, sum_of_values - 1) #get a random num from 0-sum_of_values -1 
        random_weighted_word = ""
        for w in self.dictionary_histogram.items():
            if random_num == 0:
                random_weighted_word = w[0]
                break
            if random_num > 0: #if rand_num is greater than 0, then decrement it
                random_num -= w[1]
            if random_num < 0:
                random_weighted_word = w[0]
                break
        # random_num = randint(0, sum_of_values - 1) # reset the random number
        return random_weighted_word

def print_dictogram(word_list):
    '''Creates a dictionary based histogram (dictogram) and then prints out its properties and samples from it'''

    print()
    print('Easy Dictionary Histogram:')
    print('word list: {}'.format(word_list))
    # Create a dictogram and display its contents
    dictogram = EasyDictogram(word_list)
    print('dictogram: {}'.format(dictogram.dictionary_histogram))
    print('{} tokens, {} types'.format(dictogram.tokens, dictogram.types))
    for word in word_list[-2:]:
        freq = dictogram.frequency(word)
        print('{!r} occurs {} times'.format(word, freq))
    print()
    print_dictogram_samples(dictogram)

def print_dictogram_samples(dictogram):
    '''Compares sampled frequency to observed frequency'''

    print('Easy Dictionary Histogram samples:')
    # Sample the histogram 10,000 times and count frequency of results
    samples_list = [dictogram.sample() for _ in range(10000)]
    samples_hist = EasyDictogram(samples_list)
    print('samples: {}'.format(samples_hist.dictionary_histogram))
    print()
    print('Sampled frequency and error from observed frequency:')
    header = '| word type | observed freq | sampled freq  |  error  |'
    divider = '-' * len(header)
    print(divider)
    print(header)
    print(divider)
    # Colors for error
    green = '\033[32m'
    yellow = '\033[33m'
    red = '\033[31m'
    reset = '\033[m'
    # Check each word in original histogram
    for word, count in dictogram.dictionary_histogram.items():
        # Calculate word's observed frequency
        observed_freq = count / dictogram.tokens
        # Calculate word's sampled frequency
        samples = samples_hist.frequency(word)
        sampled_freq = samples / samples_hist.tokens
        # Calculate error between word's sampled and observed frequency
        error = (sampled_freq - observed_freq) / observed_freq
        color = green if abs(error) < 0.05 else yellow if abs(error) < 0.1 else red
        print('| {!r:<9} '.format(word)
            + '| {:>4} = {:>6.2%} '.format(count, observed_freq)
            + '| {:>4} = {:>6.2%} '.format(samples, sampled_freq)
            + '| {}{:>+7.2%}{} |'.format(color, error, reset))
    print(divider)
    print()

print_dictogram(['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish'])