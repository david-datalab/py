
largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    try:
        i = int(num)
        if smallest is None:
            smallest = i
        elif i < smallest:#here we are comparing if the value in the array is smaller the the value also taken from the array
            smallest = i

        if largest is None:#the trigger will take the first value in the array to fill the void cuased by using None value
            largest = i
        elif i > largest:#here we are comparing if the value in the array is smaller the the value also taken from the array
            largest = i
    except:
        if num == "done" :
            break
        print("Invalid input")
        continue

print("Maximum is ", largest)
print("Minimum is ", smallest)
#the final solution was to use more if and elif and to use the except for when anything goes wrong, also use try to ignore the mistakes in the code , this is a future message for yourself.


#largest = None
#smallest = None
#while True:
#    num = input("Enter a number: ")
#    try:
#        i = str(int(num))
                #print(i)
#    except:
#        if num == "done" :
#            break
        #print(num)
#        if num != "done":
#            print("Invalid input")
            #i = int(num)
#            continue

#    for i in num:
#        if smallest is None:#the trigger will take the first value in the array to fill the void cuased by using None value
#            smallest = i
#        elif i < smallest:#here we are comparing if the value in the array is smaller the the value also taken from the array
#            smallest = i
#        print(i)
#    print("small",smallest, type(smallest))
#
#    for i in num:
#        if largest is None:#the trigger will take the first value in the array to fill the void cuased by using None value
#            largest = i
#        elif i > largest:#here we are comparing if the value in the array is smaller the the value also taken from the array
#            largest = i
#        print(i)
#    print("large",largest, type(largest))
#print("Maximum is ", largest)
#print("Minimum is ", smallest)
