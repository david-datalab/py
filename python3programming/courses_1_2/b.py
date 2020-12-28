words = ["adopt", "bake", "beam", "confide", "grill", "plant", "time", "wave", "wish"]
e = "e"
ed = "ed"
past_tense = list()
for i in words:
		#print(i[-1:])
		if i[-1:] == "e":
			pt = i + "d"
			past_tense.append(pt)
		elif i[-1:] != "e":
			pt = i + ed
			past_tense.append(pt)
		else:
			print("error")
print(past_tense)