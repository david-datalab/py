sentence = "python is a high level general purpose programming language that can be applied to many different classes of problems."
s = sentence.split()
a = 0
e = 0

for i in s:
	
	if "a" in i:
		a = a + 1 
		
	elif "e" in i:
		e = e + 1
num_a_or_e = e + a 
print(num_a_or_e)		