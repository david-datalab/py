stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"
sent = sent.strip().split()
lst = []

for strg in sent:
	if strg not in stopwords:
		lst.append(strg[:2].upper())
acro = ". ".join(lst)
print(acro)


