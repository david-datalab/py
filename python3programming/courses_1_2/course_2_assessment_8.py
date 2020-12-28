#Sort the following string alphabetically, from z to a, and assign it to the variable sorted_letters.
letters = "alwnfiwaksuezlaeiajsdl"
sorted_letters = sorted(letters, reverse=True)
#Sort the list below, animals, into alphabetical order, a-z. Save the new list as animals_sorted.


animals = ['elephant', 'cat', 'moose', 'antelope', 'elk', 'rabbit', 'zebra', 'yak', 'salamander', 'deer', 'otter', 'minx', 'giraffe', 'goat', 'cow', 'tiger', 'bear']
animals_sorted = sorted(animals)


#The dictionary, medals, shows the medal count for six countries during the Rio Olympics. Sort the country names so they appear alphabetically. Save this list to the variable alphabetical.


medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}
alphabetical = sorted(medals)


#Given the same dictionary, medals, now sort by the medal count. Save the three countries with the highest medal count to the list, top_three.
medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}

list=sorted(medals,key=lambda medal:medals[medal],reverse=True)

top_three=list[:3]
#web example
#orders = {
#	'cappuccino': 54,
#	'latte': 56,
#	'espresso': 72,
#	'americano': 48,
#	'cortado': 41
#}
#
#sort_orders = sorted(orders.items(), key=lambda x: x[1], reverse=True)
#
#for i in sort_orders:
#	print(i[0], i[1])



#Create a function called last_four that takes in an ID number and returns the last four digits. For example, the number 17573005 should return 3005. Then, use this function to sort the list of ids stored in the variable, ids, from lowest to highest. Save this sorted list in the variable, sorted_ids. Hint: Remember that only strings can be indexed, so conversions may be needed.


def last_four(x):
    lst = []
    for i in x:
        i = str(i)
        lst.append(i[-4:])
        return lst

ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]
ids = str(ids)
sorted_ids = sorted(ids, key = last_four) 


#Sort the list ids by the last four digits of each id. Do this using lambda and not using a defined function. Save this sorted list in the variable sorted_id.

ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]
sorted_id = sorted(ids, key =lambda x: str(x)[-4:]) 

#Sort the following list by each element’s second letter a to z. Do so by using lambda. Assign the resulting value to the variable lambda_sort.

ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']

lambda_sort = sorted(ex_lst, key = lambda x: x[1]) 
