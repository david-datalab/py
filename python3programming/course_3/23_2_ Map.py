#The following function produces a new list with each item in the original list doubled. It is an example of a mapping, from the original list to a new list of the same length, where each element is doubled.
def doubleStuff(a_list):
    """ Return a new list in which contains doubles of the elements in a_list. """
    new_list = []
    for value in a_list:
        new_elem = 2 * value
        new_list.append(new_elem)
    return new_list

things = [2, 5, 9]
print(things)
things = doubleStuff(things)
print(things)

#As we did when passing a function as a parameter to the sorted function, we can specify a function to pass to map either by referring to a function by name, or by providing a lambda expression.
def triple(value):
    return 3*value

def tripleStuff(a_list):
    new_seq = map(triple, a_list)
    return list(new_seq)

def quadrupleStuff(a_list):
    new_seq = map(lambda value: 4*value, a_list)
    return list(new_seq)

things = [2, 5, 9]
things3 = tripleStuff(things)
print(things3)
things4 = quadrupleStuff(things)
print(things4)

#Of course, once we get used to using the map function, it’s no longer necessary to define functions like tripleStuff and quadrupleStuff.
things = [2, 5, 9]

things4 = map((lambda value: 4*value), things)
print(list(things4))

# or all on one line
print(list(map((lambda value: 5*value), [1, 2, 3])))


#1. Using map, create a list assigned to the variable greeting_doubled that doubles each element in the list lst.


lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]

greeting_doubled = map(lambda x : x * 2 , lst) 

#2. Below, we have provided a list of strings called abbrevs. Use map to produce a new list called abbrevs_upper that contains all the same strings in upper case.


abbrevs = ["usa", "esp", "chn", "jpn", "mex", "can", "rus", "rsa", "jam"]

abbrevs_upper = map(lambda x : x.upper(), abbrevs)