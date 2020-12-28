Junior = {'SI 206':4, 'SI 310':4, 'BL 300':3, 'TO 313':3, 'BCOM 350':1, 'MO 300':3}

credits = 0
for course in Junior:
    credits = credits + Junior[course]




str1 = "peter piper picked a peck of pickled peppers"

freq = {}

for c in str1:
    if c not in freq:
        freq[c] = 0
    freq[c] = freq[c] + 1

keys = list(freq.keys())
min_value = keys[0]

for key in keys:
    if freq[key] > freq[min_value]:
        min_value = key






s1 = "hello"

counts = {} # start with an empty dictionary
for c in s1:
    if c not in counts:
        # we have not seen this character before, so initialize a counter for it
        counts[c] = 0

    #whether we've seen it before or not, increment its counter
    counts[c] = counts[c] + 1

for c in counts.keys():
    print(c + ": " + str(counts[c]) + " occurrences")






str1 = "I wish I wish with all my heart to fly with dragons in a land apart"

freq_words = {}
words = str1.split()
#word_counts = {}
for word in words:
    if word not in freq_words:
        freq_words[word] = 0
    freq_words[word] = freq_words[word] + 1
print(freq_words)






sent = "Singing in the rain and playing in the rain are two entirely different situations but both can be good"

wrd_d = {}
words = sent.split()
#word_counts = {}
for word in words:
    if word not in wrd_d:
        wrd_d[word] = 0
    wrd_d[word] = wrd_d[word] + 1
print(wrd_d)





sally = "sally sells sea shells by the sea shore"


characters = {}

for c in sally:
    if c not in characters:
        characters[c] = 0
    characters[c] = characters[c] + 1

keys = list(characters.keys())
best_char = keys[0]
for key in keys:
    if characters[key] > characters[best_char]:
        best_char = key









sally = "sally sells sea shells by the sea shore and by the road"

characters = {}

for c in sally:
    if c not in characters:
        characters[c] = 0
    characters[c] = characters[c] + 1

keys = list(characters.keys())
worst_char = keys[0]
for key in keys:
    if characters[key] < characters[worst_char]:
        worst_char = key






string1 = "There is a tide in the affairs of men, Which taken at the flood, leads on to fortune. Omitted, all the voyage of their life is bound in shallows and in miseries. On such a full sea are we now afloat. And we must take the current when it serves, or lose our ventures."
txt = string1.lower()

letter_counts = {} # start with an empty dictionary
for c in txt:
    if c not in letter_counts:
        # we have not seen this character before, so initialize a counter for it
        letter_counts[c] = 0

    #whether we've seen it before or not, increment its counter
    letter_counts[c] = letter_counts[c] + 1

for c in letter_counts.keys():
    print(c + ": " + str(letter_counts[c]) + " occurrences")



p = "Summer is a great time to go outside. You have to be careful of the sun though because of the heat."


#string1 = "There is a tide in the affairs of men, Which taken at the flood, leads on to fortune. Omitted, all the voyage of their life is bound in shallows and in miseries. On such a full sea are we now afloat. And we must take the current when it serves, or lose our ventures."
txt = p.lower()

low_d = {} # start with an empty dictionary
for c in txt:
    if c not in low_d:
        # we have not seen this character before, so initialize a counter for it
        low_d[c] = 0

    #whether we've seen it before or not, increment its counter
    low_d[c] = low_d[c] + 1

for c in low_d.keys():
    print(c + ": " + str(low_d[c]) + " occurrences")
