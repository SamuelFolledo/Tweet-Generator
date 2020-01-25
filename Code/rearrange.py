import random
import sys

quotes = ("It's just a flesh wound.",
          "He's not the Messiah. He's a very naughty boy!",
          "THIS IS AN EX-PARROT!!")

def random_python_quote():
    rand_index = random.randint(0, len(quotes) - 1)
    return quotes[rand_index]

if __name__ == '__main__':
    params = sys.argv[1:] #this is how you get command line inputs. Exclude python3 and fileName.py #$ python rearrange.py how now brown cow
    random.shuffle(params) #random.shuffle() takes an array and shuffles it
    print(params)
