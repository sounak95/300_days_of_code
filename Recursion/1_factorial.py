'''
fact(5)
|
+-- 5 * fact(4)
     |
     +-- 4 * fact(3)
          |
          +-- 3 * fact(2)
               |
               +-- 2 * fact(1)
                    |
                    +-- 1 * fact(0)
                         |
                         +-- 1 (base case reached)

Time complexity: o(n)
Space Complexity: o(n)
'''


def fact(n):
     #base case
     if n == 0:
          return 1
     #recursive relation
     recAns = fact(n - 1)

     #processing
     finalAns = n * recAns

     return finalAns


print(fact(5))
