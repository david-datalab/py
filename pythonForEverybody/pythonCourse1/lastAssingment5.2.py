largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    try:
        i = int(num)
        if smallest is None:
            smallest = i
        elif i < smallest:
            smallest = i

        if largest is None:
            largest = i
        elif i > largest:
            largest = i
    except:
        if num == "done" :
            break
        print("Invalid input")
        continue

print("Maximum is", largest)
print("Minimum is", smallest)
