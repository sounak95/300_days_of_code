

def fact(n):
    #base case
    if n==0:
        return 1
    #recursive relation
    recAns = fact(n-1)

    #processing
    finalAns =  n*recAns

    return finalAns


print(fact(5))