words = ["water", "chair", "pen", "basket", "hi", "car"]
num_words = 0
for i in words:
	if len(i) > 3:
		num_words = num_words + 1
        
print(num_words)