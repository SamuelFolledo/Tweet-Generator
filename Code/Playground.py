from __future__ import division, print_function
from random import randint, choice, seed
# seed(1) #for different random nums
import re #for changing lines to words list

def play_with_dictionary():
    myDic = {1:["kobe", "mj"], 3:["wade", "lebron"]}
    print(myDic[1])
    values = myDic.keys()
    print(values)
    for count in values: #loop through each values in dic
        players = myDic[count]
        for player in players:
            if player == "wade":
                print(f"{player} has {count} count")
    # myDic.pop(2)
    print(f"my dic is {myDic}")

    newDic = {"kobe": 24, "mj":23}
    # print(newDic)
    number = -1
    # if "kobe" in newDic:
    number = newDic.get("kk",0)
    # else:
    #     number = 0
    # print(number)
    # for word in words:
    #     word_count = words_histogram.get(word, 0) + 1  #if word is in words_histogram's keys, count will increment, else equal 1
    #     words_histogram[word] = word_count

def sample_words(histogram):
    sum_of_values = sum(histogram.values()) #word_counts.values() returns a list of word_count's values. sum() will sum a the values in a list and returns an int
    random_num = randint(0, sum_of_values - 1) #get a random num from 0-sum_of_values -1 
    random_weighted_word = ""
    for i in range(20): #test by doing it 10x
        # print(f"Test #{i+1}: {random_num} =", end = " ") #end to not create a new line
        for w in histogram.items():
            if random_num == 0:
                # print(f"{w[0]}\n")
                random_weighted_word = w[0]
                break
            if random_num > 0: #if rand_num is greater than 0, then decrement it
                random_num -= w[1]
            if random_num < 0: #0=one, 1-4=fish, 5=two, 6=red, 7 = blue
                # print(f"{w[0]}\n")
                random_weighted_word = w[0]
                break
        random_num = randint(0, sum_of_values - 1) # reset the random number
    return random_weighted_word

# histogram = {"one": 1, "fish":4, "two": 1, "red": 1, "blue":1} 
# sample_words(histogram)

def get_lines():
    my_file = open("./words.txt", "r")
    lines = my_file.readlines()
    my_file.close()
    return lines

def listogram(lines): #lines = list of lines, meaning a list of strings
    listogram = []
    for line in lines:
        words_list_from_line = re.sub("[^\w]", " ",  line).split() #turns every word in line to a list of words
        for word in words_list_from_line:
            index = get_index(word, listogram)
            if index == -1:
                listogram.append([word, 1])
            else:
                # listogram[index][1] += 1
                print(listogram)

def get_index(word, listogram):
    index = 0
    print("word is=", word, "---listogram is", listogram)
    for (word, index) in listogram: #word is a list ["word", count]
        if word[0] == word:
            print(f"Found {word} at index: {index}")
            return index
        index += 1
    print("never found it")
    return -1

def markov_guy(word_list):
    chain = {}
    for i in range(len(word_list)):
        print(i)
        if i == len(word_list):
            break
        if word_list[i] in chain: #if key(word_list[i]) is in dic...
            print(f"We got {word_list[i]} already")
            list_of_words_with_count = chain[word_list[i]] #values([['word1', 1], [word2, 1], ...]) of chain[word_list[i]]
            for word_and_count in chain[word_list[i]]: #for each word_and_count list in our dic of words...
                # print(f"list is {chain[word_list[i]]}")
                # print(word_and_count[0])
                if i + 1 >= len(word_list):
                    continue
                print(f"i+1 = {word_list[i+1]}")
                if word_and_count[0] == word_list[i+1]: #word_and_count[0] is word and word_and_count[1] is the count...
                    print(f"We have {word_list[i+1]} already")
                    # current_count = word_and_count[1]
                    print(f"KAKAKAK {chain[word_list[i]]}")
                    # chain[word_list[i+1]] = []
                    # chain[word_list[i]].append([word_list[i+1], 1])
            #         print(f"FOUND {word_list[i]}")
                    break
                else:
                    chain[word_list[i]].append([word_list[i+1], 1])
                    print(f"NOPE {word_list[i+1]} is new")
            #         chain[word_list[i]] = word_list[i]
                    print(f"LALALA {chain[word_list[i]]}")
                    continue
                
        else: #word is not in dic yet
            chain[word_list[i]] = [[word_list[i+1],1]] #word = [[next_word, 1]]

        # result = chain.get(word_list[i], [[word_list[i+1]]) #[[word1: 1], [word2: 1],...]
        # print(result)

    print(f"CHAIN IS {chain}")


    
if __name__ == '__main__':
    # lines = get_lines()
    # print(lines)
    # listogram(lines)

    fish_text = 'one fish two fish red fish blue fish blue fish'
    markov_guy(fish_text.split())
