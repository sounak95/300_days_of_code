'''
helper("madam", 0, 4)
├── helper("madam", 1, 3)
│   ├── helper("madam", 2, 2) (At the middle of the string, returns True)
│   └── (No mismatch found, so returns True up the tree)
└── (Start and end characters match, continues to recurse)

helper("adam", 0, 3)
└── (Mismatch between 'a' and 'm', returns False immediately, no further recursion)

'''
# Recursive helper function that checks if a substring is a palindrome
def helper(str1, s, e):
    if s > e:  # If start index is greater than end, we've checked all the characters
        return True  # The substring is a palindrome

    if str1[s] != str1[e]:  # If characters at start and end index don't match
        return False  # The substring is not a palindrome

    # Move towards the middle of the string and recurse
    return helper(str1, s + 1, e - 1)

# Function to check if the whole string is a palindrome
def isPalin():
    str1 = "madam"  # First test string
    print(helper(str1, 0, len(str1) - 1))  # Check if 'madam' is a palindrome

    str1 = "adam"  # Second test string
    print(helper(str1, 0, len(str1) - 1))  # Check if 'adam' is a palindrome

isPalin()  # Call the function to perform the check
