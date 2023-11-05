#!/bin/python3
# https://www.hackerrank.com/challenges/ctci-merge-sort/problem
import math
import os
import random
import re
import sys

#
# Complete the 'countInversions' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def merge(arr,temp, s, mid, e):
    # Calculate the middle index of the current segment of the array
    i= s
    j= mid+1
    k=s

    c=0
    while(i<=mid and j<=e):
        if arr[i]<=arr[j]:
            temp[k] = arr[i]
            i+=1
        else:
            temp[k]= arr[j]
            c+=mid-i+1
            j+=1
        k+=1

    while(i<=mid):
        temp[k]=arr[i]
        i+=1
        k+=1

    while(j<=e):
        temp[k]=arr[j]
        j+=1
        k+=1

    for i in range(s, e+1):
        arr[i] = temp[i]

    return c




    return c

def merge_sort(arr, temp, s, e):
    # Base case: If the segment size is 1 or 0, it's already sorted
    if s >= e:
        return 0

    # Calculate the middle index
    mid = (s + e) // 2
    c=0
    # Recursively apply merge_sort to the left half
    c+=merge_sort(arr, temp, s, mid)

    # Recursively apply merge_sort to the right half
    c+=merge_sort(arr, temp, mid + 1, e)

    # Merge the two sorted halves
    c+=merge(arr, temp, s, mid, e)

    return c

def countInversions(arr):
    # Write your code here
    temp=[0] * len(arr)
    return merge_sort(arr, temp, 0, len(arr)-1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
