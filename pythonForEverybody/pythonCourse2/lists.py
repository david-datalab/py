friends = ['glenn', 'joseph', 'sally']
for friend in friends :
    print(friend)
print(range(len(friends)))
print(friends[1])


for i in range(len(friends)) :
    friend = friends[1]
print("happy new year:", friend)




numlist = list()
while True:
    inp = input("Enter a number:")
    if inp == 'done': break
    value = float(inp)
    numlist.append(value)
average = sum(numlist) / len(numlist)
print(average)



#cpu 350
#ram 260
#gpu 879
#cooler 263
#thermal paste 30
#hdmi to vga active adapter 30
#total 1812TL
