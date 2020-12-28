
def checkingIfIn(s ,direction = True , d = {'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}):
	if direction == True:
		print('t')
		if s in d:
			print('in')
			return True		
		if s not in d:
			print('not in')
			return False
	elif direction == False:
		print('f')
		if s in d:
			print('in')
			return False		
		if s not in d:
			print('not in')
			return True
	else:
		return False
checkingIfIn('mango',False)
