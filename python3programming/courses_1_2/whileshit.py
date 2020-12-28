list1 = [8, 3, 4, 5, 6, 7, 9]

def stop_at_four(list1):
	c = -1
	l = []
	while c < len(list1):
		c = c + 1
		if c <= 3:
			l.append(list1[c])
	print(l)
	return l
			
stop_at_four(list1)



list1 = [8, 3, 4, 5, 6, 7, 9]
idx = 0
accum = 0
while idx < len(list1):
    accum = accum + list1[idx]
    idx = idx + 1
    

    
