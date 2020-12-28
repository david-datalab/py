# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
fh = fh.read().upper().rstrip()
#reading and converting to upprcase letters and stripping the right whitespaces
#ufh = fh.upper()
print(fh)
