
def print_permutation(s, index):
    if index>=len(s):
        print(s, end=' ')
        return

    s_list = list(s)
    for i in range(index, len(s)):
        s_list[index], s_list[i] = s_list[i], s_list[index]
        print_permutation("".join(s_list), index+1)
        s_list[index], s_list[i] = s_list[i], s_list[index]

if __name__ == "__main__":
    string = "abc"
    print_permutation(string, 0)