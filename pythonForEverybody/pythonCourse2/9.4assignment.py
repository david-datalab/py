name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"

handle = open(name)
counts = dict()
mailList = list()

for line in handle :
    if 'From ' in line :
        words = line.split()
        address = words[1]
        mailList.append(address)

for word in mailList :
    counts[word] = counts.get(word,0) + 1

bigcount = None
bigword = None

for word,count in counts.items() :
    if bigcount is None or count > bigcount :
        bigword = word
        bigcount = count

print(bigword,bigcount)
