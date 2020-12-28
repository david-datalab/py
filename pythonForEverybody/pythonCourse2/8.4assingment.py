fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh :
  l = line.rstrip().split()

  for word in l :
      if word not in lst:#the trick was here and my mistake was in how to form the if statement and also I used lst variable earlier in the equasion and that lead me to a lot of confusion.
          lst.append(word)
          continue
lst.sort()
print(lst)



#so I need to read the range index and add the list components due to the range index
#also before that I need to create a list in a correct way that it will include each
#word as a single list element and that was my mistake, "reading lines as list elements"









#open
#read line by line
#split each line
#build a list
#check for words
#append new words
#sort and print
