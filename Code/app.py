from flask import Flask
from histogram import Histogram, create_histogram, get_frequency, get_unique_words, word_contains
from Playground import sample_words, get_lines

app = Flask(__name__)

@app.route('/')
def generate_words():
    lines = get_lines()
    myHistogram = Histogram(lines)
    sentence = ""
    num_words = 10
    for i in range(num_words):
        word = sample_words(myHistogram)
        sentence += " " + word
    print("Sentence is ", sentence)
    return sentence

if __name__ == '__main__':
    app.run()