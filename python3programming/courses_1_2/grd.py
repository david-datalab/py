def addit(n):
    n = n + 5
    return n
def mult(x):
    call = addit(x)
    return x * call
print(mult(addit(5)))