import re
fname = '72.txt'
fh = open(fname)
lst = list()
for line in fh:#to extract string numbers valuse and put them in a list
    num = line.strip()
    ln = re.findall("[0-9]+", num)
    for s in ln:#to loop through the strings found in ln
        #if s not in lst:#UPDATE: the headache was here XD #to add the string value in a single list
        lst.append(s)
for i in range(0, len(lst)):#to convert from string to int
    #print(i)
    lst[i] = int(lst[i])
s = sum(lst)
print(lst)
print(s)
#760
#445833
#27486
