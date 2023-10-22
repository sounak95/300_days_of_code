def print_permutation(s, index):
    # base case
    if index >= len(s):
        print(s, end=" ")
        return

    s_list = list(s)  # Convert string to list since Python strings are immutable
    for j in range(index, len(s)):
        # Swap characters
        s_list[index], s_list[j] = s_list[j], s_list[index]

        # recursion
        print_permutation("".join(s_list), index + 1)

        # backtracking
        s_list[index], s_list[j] = s_list[j], s_list[index]


if __name__ == "__main__":
    string = input("Enter a string: ")
    print_permutation(string, 0)
