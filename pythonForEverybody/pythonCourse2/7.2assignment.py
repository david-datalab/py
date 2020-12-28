# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
counter = 0
fnum = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    counter = counter + 1
    fnum = fnum + float(line[21:].strip())
    #print(counter, fnum)
    average = fnum / counter
print("Average spam confidence:", average)
#try:
#except:

    #if line.startswith("X-DSPAM-Confidence:") : continue
    #counter = counter + 1
    #print(counter)

print("Done")
#counter done
#extract float data done
#average calculation -> done
#strip done
#print the result done
