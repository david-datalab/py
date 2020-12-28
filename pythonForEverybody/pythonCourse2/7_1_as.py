fname = input("Enter file name: ")
fh = open(fname)
fh = fh.read().upper().rstrip()
print(fh)