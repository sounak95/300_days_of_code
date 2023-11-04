'''
find([1,2,3,4,3,5,3], 7, 0, 3)
└── find([1,2,3,4,3,5,3], 7, 1, 3)
    └── find([1,2,3,4,3,5,3], 7, 2, 3) [prints 2]
        └── find([1,2,3,4,3,5,3], 7, 3, 3)
            └── find([1,2,3,4,3,5,3], 7, 4, 3) [prints 4]
                └── find([1,2,3,4,3,5,3], 7, 5, 3)
                    └── find([1,2,3,4,3,5,3], 7, 6, 3) [prints 6]
                        └── find([1,2,3,4,3,5,3], 7, 7, 3) (Base case reached, no further calls)
'''

def find(arr, n, i, target):
    if i==n:
        return

    if arr[i]==target:
        print(i)

    find(arr,n,i+1, target)

arr=[1,2,3,4,3,5,3]

find(arr, len(arr), 0, 3)
