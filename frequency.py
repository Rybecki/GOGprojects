from collections import Counter

def word_count(fname):
        with open(fname) as f:
                return Counter(f.read().split())

print("Frequency of words in the file: ", word_count("testfile.txt"))

from guesslang import Guess

name = Guess().language_name("testo.py")
print(name)