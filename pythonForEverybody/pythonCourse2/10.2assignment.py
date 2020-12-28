name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"

handle = open(name)
counts = dict()
hoursCount = list()

for line in handle :
    if 'From ' in line :
        words = line.split()
        hours = words[5]
        hour = hours.split(':')
        time = hour[0]
        hoursCount.append(time)

for word in hoursCount :
    counts[word] = counts.get(word,0) + 1

bigcount = None
bigword = None

for word,count in sorted(counts.items()) :
    bigword = word
    bigcount = count
    print(bigword,bigcount)
