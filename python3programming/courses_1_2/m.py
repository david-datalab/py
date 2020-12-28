stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
org = "The organization for health, safety, and education"
org = org.strip().split()
lst = []

for strg in org:
	if strg not in stopwords:
		lst.append(strg[0].upper())
acro = "".join(lst)
