rawstr = input('enter a number:')
try:
    ival = int(rawstr)
except:
    ival = -1
    print('error : not a number , default value is used.')
if ival > 0 :
    print ('nice work!')
else:
    print ('not a number !')
