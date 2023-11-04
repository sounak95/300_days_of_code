'''
                       fibo(5)
                       /    \
                  fibo(4)    fibo(3)
                  /    \       /    \
            fibo(3)  fibo(2) fibo(2) fibo(1)
            /    \    /    \   /    \
      fibo(2) fibo(1) fibo(1) fibo(0)
      /    \
fibo(1) fibo(0)

'''
'''
0 1 1 2 3 5 8
'''
def fibo(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fibo(n-1)+fibo(n-2)

print(fibo(6))