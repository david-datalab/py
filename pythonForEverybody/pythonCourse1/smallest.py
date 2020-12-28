#finding the smallest value in a loop with a condition and a trigger
smallest = None#none value means the abscence of a value or the lack of a value
print('before')
for value in [9, 41, 12, 3, 74, 15]:
    if smallest is None:#the trigger will take the first value in the array to fill the void cuased by using None value
        smallest = value
    elif value < smallest:#here we are comparing if the value in the array is smaller the the value also taken from the array
        smallest = value
    print(smallest, value)
print('after', smallest)
