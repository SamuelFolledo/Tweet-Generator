from random import randint, choice, seed
seed(1) #for different random nums

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
