
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# list of positive words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

def strip_punctuation(string):
    for char in punctuation_chars:
        if char in punctuation_chars:
            string = string.replace(char,"")
    return string

def got_pos(s):
    

