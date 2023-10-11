

def print_n_to_1(n):
    #base case
    if n==0:
        return n
    #processing
    print(n)

    # recursion call
    print_n_to_1(n-1)

print_n_to_1(5)