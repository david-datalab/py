#1
file = open("travel_plans.txt" , "r")
rd = file.read()
num = len(rd)
print(len(rd))

#2
file = open("emotion_words.txt" , "r")
rd = file.readline()
num_words = len(rd[:48])
print(len(rd))
print(rd)

#3
file = open("school_prompt.txt" , "r")
rd = file.readlines()
num_lines = len(rd)
print(len(rd))
print(rd)

#4
file = open("school_prompt.txt" , "r")
rd = file.readlines()
#print(rd)
beginning_chars = rd[0][:30]
print(beginning_chars)

#5
file = open("school_prompt.txt" , "r")
rd = file.readlines()
print(rd)
three = []
for v in rd:
    v = v.split()
    print(v[2])
    three.append(v[2])
#6
file = open("emotion_words.txt" , "r")
rd = file.readlines()
print(rd)
emotions = []
for v in rd:
    v = v.split()
    print(v[0])
    emotions.append(v[0])

#7
file = open("travel_plans.txt" , "r")
rd = file.read()
first_chars = rd[:33]
print(first_chars)

#8
file = open("school_prompt.txt" , "r")
rd = file.readlines()
#print(file)
lst = []
for v in file:
    v = v.strip().split()
    for word in v :
        lst.append(word)
    continue
p_words = []
letters = set('p')
for word in lst:
    if letters & set(word):
        p_words.append(word.rstrip(',').rstrip('.'))
print(p_words)