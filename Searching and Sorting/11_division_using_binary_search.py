

def get_quotient(divisor, dividend):
    s=0
    e= dividend

    mid = s+(e-s)//2
    ans=-1
    while(s<=e):
        if mid*divisor==dividend:
            return mid
        elif mid*divisor<dividend:
            ans= mid
            s=mid+1
        else:
            e=mid-1
        mid=s+(e-s)//2

    return ans

divisor=-1
dividend=35
ans = get_quotient(abs(divisor),abs(dividend))

if (divisor>0 and dividend<0) or (divisor<0 and dividend>0):
    ans = 0-ans

print(ans)



