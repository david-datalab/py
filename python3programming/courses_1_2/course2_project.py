
#We have provided some synthetic (fake, semi-randomly generated) twitter data in a csv file named project_twitter_data.csv which has the text #of a tweet, the number of retweets of that tweet, and the number of replies to that tweet. We have also words that express positive sentiment #and negative sentiment, in the files positive_words.txt and negative_words.txt.
#
#Your task is to build a sentiment classifier, which will detect how positive or negative each tweet is. You will create a csv file, which #contains columns for the Number of Retweets, Number of Replies, Positive Score (which is how many happy words are in the tweet), Negative Score #(which is how many angry words are in the tweet), and the Net Score for each tweet. At the end, you upload the csv file to Excel or Google #Sheets, and produce a graph of the Net Score vs Number of Retweets.
#
#To start, define a function called strip_punctuation which takes one parameter, a string which represents a word, and removes characters #considered punctuation from everywhere in the word. (Hint: remember the .replace() method for strings.)

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
def strip_punctuation(string):
    for char in punctuation_chars:
        if char in punctuation_chars:
            string = string.replace(char,"")
    return string


#Next, copy in your strip_punctuation function and define a function called get_pos which takes one parameter, a string which represents one or more sentences, and calculates how many words in the string are considered positive words. Use the list, positive_words to determine what words will count as positive. The function should return a positive integer - how many occurrences there are of positive words in the text. Note that all of the words in positive_words are lower cased, so you’ll need to convert all the words in the input string to lower case as well.


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

def get_pos(strSentences):
    strSentences = strip_punctuation(strSentences)
    listStrSentences = strSentences.split()

    c = 0
    for word in listStrSentences:
        for positiveWord in positive_words:
            if worf == positiveWord:
                c += 1
    return c