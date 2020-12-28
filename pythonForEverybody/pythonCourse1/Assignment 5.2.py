

largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    print(num)
    for i in num:
        if smallest is None:#the trigger will take the first value in the array to fill the void cuased by using None value
            smallest = i
        elif i < smallest:#here we are comparing if the value in the array is smaller the the value also taken from the array
            smallest = i
        print(smallest, value)
    print('after', smallest)
    for i in num:
        if largest is None:#the trigger will take the first value in the array to fill the void cuased by using None value
            largest = i
        elif i > largest:#here we are comparing if the value in the array is smaller the the value also taken from the array
            largest = i
        print(largest, value)
    print('after', largest)
print("Maximum", largest)
print("Minimum", smallest)
