fname = 'romeo.txt'
fh = open(fname)
lst = list()
for line in fh :
  x = line.rstrip().split()
  for word in x :
      lst.append(word)
      continue
lst.sort()
print(lst)
