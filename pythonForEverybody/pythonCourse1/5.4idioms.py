#counter example
zork = 0
print('before', zork)
for thing in [9, 41, 12, 3, 74, 15] :
    zork = zork + 1
    print(zork, thing)
print('after', zork)
#sum example
surk = 0
print('before', surk)
for thing in [9, 41, 12, 3, 74, 15]:
    surk = surk + thing
    print(surk ,thing)
print('after', surk)
#average example
count = 0
sum = 0
print('before', count, sum)
for value in [9, 41, 12, 3, 74, 15]:
    count = count + 1
    sum = sum + value
    print (count, sum, value)
print('after', count, sum, sum / count)

#filtering in a loop
print('before')
for vavue in [9, 41, 12, 3, 74, 15]:
    if vavue > 20 :
        print('large number', vavue)
print('after')

#search using a boolean variable
found = False
print('before', found)
for vague in [9, 41, 12, 3, 74, 15]:
    if vague == 3:
        found = True
    print(found, vague)
print('after', found)
