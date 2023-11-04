'''
print_permutation("abc", 0)
│
├─ print_permutation("abc", 1)  # Swapped 'a' with 'a'
│  ├─ print_permutation("abc", 2)  # Swapped 'b' with 'b' [abc]
│  └─ print_permutation("acb", 2)  # Swapped 'b' with 'c' [acb]
│
├─ print_permutation("bac", 1)  # Swapped 'a' with 'b'
│  ├─ print_permutation("bac", 2)  # Swapped 'a' with 'a' [bac]
│  └─ print_permutation("bca", 2)  # Swapped 'a' with 'c' [bca]
│
└─ print_permutation("cba", 1)  # Swapped 'a' with 'c'
   ├─ print_permutation("cba", 2)  # Swapped 'b' with 'b' [cba]
   └─ print_permutation("cab", 2)  # Swapped 'b' with 'a' [cab]
'''

def print_permutation(s, index):
    # Base case: If the index has reached the length of the string, a permutation is ready to be printed.
    if index >= len(s):
        print(s, end=' ')
        return

    # Convert the string to a list to allow swapping elements.
    s_list = list(s)

    # Iterate over the remaining elements to be permuted.
    for i in range(index, len(s)):
        # Swap the current element with the element at the current index.
        s_list[index], s_list[i] = s_list[i], s_list[index]

        # Recursively call the function with the next index.
        print_permutation("".join(s_list), index + 1)

        # Backtrack by swapping the elements back to their original position.
        s_list[index], s_list[i] = s_list[i], s_list[index]


if __name__ == "__main__":
    string = "abc"
    # Start the permutation process from the first index.
    print_permutation(string, 0)
