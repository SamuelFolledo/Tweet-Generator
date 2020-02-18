from easyDictogram import EasyDictogram
from random import choice

class MarkovChain:

    def __init__(self, word_list):

        #The Markov chain will be a dictionary of dictionaries
        #Example: for "one fish two fish red fish blue fish"
        #{"one": {fish:1}, "fish": {"two":1, "red":1, "blue":1}, "two": {"fish":1}, "red": {"fish":1}, "blue": {"fish:1"}}
         self.markov_chain = self.build_markov(word_list)
         self.first_word = list(self.markov_chain.keys())[0]

    def build_markov(self, word_list):
        markov_chain = {}

        for i in range(len(word_list) - 1): #loop through each word, and dont include
            #get the current word and the word after
            current_word = word_list[i]
            next_word = word_list[i+1]
            if current_word in markov_chain.keys(): #already there
                #get the histogram for that word in the chain
                histogram = markov_chain[current_word]
                #add to count
                histogram.dictionary_histogram[next_word] = histogram.dictionary_histogram.get(next_word, 0) + 1
            else: #first entry
                markov_chain[current_word] = EasyDictogram([next_word])

        return markov_chain

    def get_random_word(self): #choose a random for from markov chain's keys, which are unique
        random_word = choice(list(self.markov_chain.keys())) #must convert these dic.keys() to list
        return random_word

    def walk(self, num_words):
        #TODO: generate a sentence num_words long using the markov chain
        sentence = ""
        first_word = self.get_random_word() #get a random word for first word
        # first_word = "fish" #for testing
        print("FIRST WORD IS", first_word)
        sentence += first_word + " "
        index = 0
        while index < num_words: #while number of words appended to the sentence is not equal to num_words...
            current_word = first_word
            for word, histogram in self.markov_chain.items(): #word is key, histogram's histogram.dictionary_histogram is value
                # print("EYOOOO", word, histogram.dictionary_histogram)
                if current_word == word: #look for our current word in our markov chain
                    current_word_dictogram = histogram.dictionary_histogram
                    print("From word =", word, "DICTOGRAM I AM SAMPLING IS", current_word_dictogram)
                    random_weighted_word = histogram.sample() #get the random_weighted_word
                    print("Sample returned is", random_weighted_word)
                    current_word = random_weighted_word #assign random_word as the current_word
                    if index == num_words - 1: #if this is the last word, add "."
                        sentence += current_word + "."
                    else: #if not last word, add a space in the end
                        sentence += current_word + " "
                    break
                else:
                    continue
            index += 1
        print("SENTENCE =", sentence)

        # histogram = self.markov_chain[first_word]
        # histogram = self.markov_chain.items()
        # print("RESULT IS", histogram)

        # while index < num_words:
        #     # word = self.markov_chain[first_word]
        #     print("Word is", word, "=== ", word.dictionary_histogram)
            # index += 1
        

    def print_chain(self):
        for word, histogram in self.markov_chain.items(): #word is key, histogram's histogram.dictionary_histogram is value
            print(word, histogram.dictionary_histogram)



# markov_chain = MarkovChain(["one", "fish", "two", "fish", "red", "fish", "blue", "fish", "blue", "fish"])
# markov_chain.print_chain()
# print(markov_chain.walk(10))

sample_line = "bottles kookaburra glide addislade guy envision jinx tow altitude success magazine stroke cramp attadale trombone spirits bitzer nike yolk zippy tingly twins directly drift genders clip gemini malachi unaudited rephrase helium lens little route spray cotta shergar finnegan chirp sadly guapo cyclase zygomatic office obstinacy bullfrog jackrabbit stamford certain spoke"
sample_line2 = 'one fish two fish red fish blue fish blue fish'

markov_chain = MarkovChain(sample_line2.split())
markov_chain.print_chain()
print(markov_chain.walk(10))