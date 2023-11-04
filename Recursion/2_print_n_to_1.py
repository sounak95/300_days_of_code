'''
print_n_to_1(5)
|
+-- Print 5
|
+-- print_n_to_1(4)
|   |
|   +-- Print 4
|
|   +-- print_n_to_1(3)
|       |
|       +-- Print 3
|
|       +-- print_n_to_1(2)
|           |
|           +-- Print 2
|
|           +-- print_n_to_1(1)
|               |
|               +-- Print 1
|
|               +-- print_n_to_1(0)
                    |
                    +-- Print nothing (base case, return without printing)

'''

def print_n_to_1(n):
    #base case
    if n==0:
        return
    #processing
    print(n)

    # recursion call
    print_n_to_1(n-1)   

print_n_to_1(5)