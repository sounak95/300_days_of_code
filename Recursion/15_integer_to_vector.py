'''
print_digits(42156)
└── print_digits(4215)
    └── print_digits(421)
        └── print_digits(42)
            └── print_digits(4)
                └── print_digits(0)  [Base case: returns and does nothing]
            [4 printed after returning from the base case]
        [2 printed after returning from the recursive call]
    [1 printed after returning from the recursive call]
[5 printed after returning from the recursive call]
[6 printed after returning from the recursive call]

Time Complexity: O(log n) base 10
Space Complexity: O(log n) base 10

'''


def print_digits(num):
    if num == 0:
        return  # Base case: when num is 0, recursion stops
    digit = num % 10  # Extract the last digit of the number
    num = num // 10  # Remove the last digit from the number
    print_digits(num)  # Recursive call with the truncated number
    print(digit)  # After the recursive call, print the last digit


# Calling the function to print digits of a number
print_digits(42156)
'''
print_digits1(42156, arr)
└── print_digits1(4215, arr)
    └── print_digits1(421, arr)
        └── print_digits1(42, arr)
            └── print_digits1(4, arr)
                └── print_digits1(0, arr)  [Base case: returns and does nothing]
            [4 appended to arr after returning from the base case]
        [2 appended to arr after returning from the recursive call]
    [1 appended to arr after returning from the recursive call]
[5 appended to arr after returning from the recursive call]
[6 appended to arr after returning from the recursive call]

Time Complexity: O(log n) base 10
Space Complexity: O(log n) base 10

'''


def print_digits1(num, arr):
    if num == 0:
        return  # Base case: when num is 0, recursion stops
    digit = num % 10  # Extract the last digit of the number
    num = num // 10  # Remove the last digit from the number
    print_digits1(num, arr)  # Recursive call with the truncated number
    arr.append(
        digit)  # After the recursive call, append the last digit to the array


# Array to store digits
arr = []
# Calling the function to store digits of a number in an array
print_digits1(42156, arr)
print(arr)  # Prints the array containing digits
