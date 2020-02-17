#!python

from __future__ import division, print_function  # Python 2 and 3 compatibility
from random import randint
import re #for changing lines to words list

class Dictogram(dict):
    """Dictogram is a histogram implemented as a subclass of the dict type."""

    def __init__(self, word_list=None):
        """Initialize this histogram as a new dict and count given words."""
        super(Dictogram, self).__init__()  # Initialize this as a new list
        # Add properties to track useful word counts for this histogram
        self.types = 0  #count of unique word #types
        self.tokens = 0  #total count of all words #tokens
        if word_list != None: #if list is not empty, update our properties
            for word in word_list:
                self.add_count(word)
                # words_from_line = re.sub("[^\w]", " ",  line).split() #turns every word in line to a list of words
                # for word in words: #loop through each word and get the histogram
                #     self.add_count(word)

    def add_count(self, word, count=1):
        """Increase frequency count of given word by given count amount."""
        if self.frequency(word) > 0: #if word exist already
            self[word] += count
        else: #if new word
            self[word] = count
            self.types += 1
        self.tokens += count

    def frequency(self, word):
        """Return frequency count of given word, or 0 if word is not found."""
        if not self.__contains__(word):
            return 0
        frequency = self[word]
        return frequency

    def get_count(self, word): #better way with .get()
        word_count = 0
        for word in self:
            word_count = self.get(word, 0) + 1  #if word is in words_histogram's keys, count will increment, else equal 1
            self[word] = word_count

    def __contains__(self, word):
        """Return boolean indicating if given word is in this histogram."""
        for word_history in self:
            if word == word_history:
                return True
        return False

    def sample(self):
        """Return a word from this histogram, randomly sampled by weighting
        each word's probability of being chosen by its observed frequency."""
        # TODO: Randomly choose a word based on its frequency in this histogram
        sum_of_values = sum(self.values()) #word_counts.values() returns a list of word_count's values. sum() will sum a the values in a list and returns an int
        random_num = randint(0, sum_of_values - 1) #get a random num from 0-sum_of_values -1 
        random_weighted_word = ""
        for w in self.items():
            if random_num == 0:
                random_weighted_word = w[0]
                break
            if random_num > 0: #if rand_num is greater than 0, then decrement it
                random_num -= w[1]
            if random_num < 0:
                random_weighted_word = w[0]
                break
        random_num = randint(0, sum_of_values - 1) # reset the random number
        return random_weighted_word

def print_histogram(word_list):
    print()
    print('Histogram:')
    print('word list: {}'.format(word_list))
    # Create a dictogram and display its contents
    histogram = Dictogram(word_list)
    print('dictogram: {}'.format(histogram))
    print('{} tokens, {} types'.format(histogram.tokens, histogram.types))
    for word in word_list[-2:]: #loop from the last 2 word from list
        freq = histogram.frequency(word)
        print('{!r} occurs {} times'.format(word, freq))
    print()
    print_histogram_samples(histogram)

def print_histogram_samples(histogram): #MARK: Find out why the word is always NONE
    print('Histogram samples:')
    # Sample the histogram 10,000 times and count frequency of results
    samples_list = [histogram.sample() for _ in range(10000)]
    samples_hist = Dictogram(samples_list)
    print('samples: {}'.format(samples_hist))
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
    for word, count in histogram.items():
        # Calculate word's observed frequency
        observed_freq = count / histogram.tokens
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


def main():
    import sys
    arguments = sys.argv[1:]  # Exclude script name in first argument
    if len(arguments) >= 1:
        # Test histogram on given arguments
        print_histogram(arguments)
    else:
        # Test histogram on letters in a word
        word = 'abracadabra'
        print_histogram(list(word))
        # Test histogram on words in a classic book title
        fish_text = 'one fish two fish red fish blue fish'
        print_histogram(fish_text.split())
        # Test histogram on words in a long repetitive sentence
        woodchuck_text = ('how much wood would a wood chuck chuck'
                          ' if a wood chuck could chuck wood')
        print_histogram(woodchuck_text.split())


if __name__ == '__main__':
    main()
