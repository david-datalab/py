
ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']

def second_let(str):
    print(str[1])
    return str[1]
    
#print(second_let(ex_lst))
sorted_by_second_let = sorted(ex_lst , key = second_let)

        
