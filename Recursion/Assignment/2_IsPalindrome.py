

def helper(str1, s, e):
    if s>e:
        return True

    if str1[s]!=str1[e]:
        return False

    return helper(str1, s+1, e-1)

def isPalin():
    str1= "madam"
    print( helper(str1, 0, len(str1)-1))
    str1 = "adam"
    print( helper(str1, 0, len(str1) - 1))

isPalin()