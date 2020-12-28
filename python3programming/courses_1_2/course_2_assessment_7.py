#Create a function called mult that has two parameters, the first is required and should be an integer, the second is an optional parameter that can either be a number or a string but whose default is 6. The function should return the first parameter multiplied by the second.
def mult(i,o = 6):
    i = int(i)
    return i * o
mult(2)


#The following function, greeting, does not work. Please fix the code so that it runs without error. This only requires one change in the definition of the function.

def greeting(name, greeting="Hello ", excl="!"):
    return greeting + name + excl

print(greeting("Bob"))
print(greeting(""))
print(greeting("Bob", excl="!!!"))


#Below is a function, sum, that does not work. Change the function definition so the code works. The function should still have a required parameter, intx, and an optional parameter, intz with a defualt value of 5.

def sum(intx, intz=5):
    return intz + intx



#Write a function, test, that takes in three parameters: a required integer, an optional boolean whose default value is True, and an optional dictionary, called dict1, whose default value is {2:3, 4:5, 6:8}. If the boolean parameter is True, the function should test to see if the integer is a key in the dictionary. The value of that key should then be returned. If the boolean parameter is False, return the boolean value “False”.


def test(i ,b = True ,dict1 = {2:3, 4:5, 6:8}):
    if b == True:
        #print('p1')
        if i in dict1:
            #print(dict1[i],'p2')
            return dict1[i]
    else:
            print('n')
            return False
test(4,b=False)

