
nums = ['1450', '33', '871', '19', '14378', '32', '1005', '44', '8907', '16']

def last_char(str):
    print(str[-1])
    return str[-1]

nums_sorted = sorted(nums, reverse = True, key = last_char)

