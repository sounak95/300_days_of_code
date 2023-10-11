
def print_digits(num):
    if num==0:
        return
    digit=num%10
    num=num//10
    print_digits(num)
    print(digit)

print_digits(42156)

def print_digits1(num, arr):
    if num==0:
        return
    digit=num%10
    num=num//10
    print_digits1(num, arr)
    # print(digit)
    arr.append(digit)

arr=[]
print_digits1(42156, arr)
print(arr)