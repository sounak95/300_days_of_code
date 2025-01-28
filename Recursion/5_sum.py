'''
        sum(3)
          |
       3 + sum(2)
             |
          2 + sum(1)
                |
               1  (base case, return 1)

               Time Complexity: O(n)
               Space Complexity: O(n)

'''


def sum(n):
    if n == 1:
        return 1

    return n + sum(n - 1)


print(sum(3))
