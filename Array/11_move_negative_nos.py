
# 2 pointer technique
l1=[1,-2,3,4,-9,-4]

'''
o/p
[-2, -9, -4, 4, 1, 3]
'''

j=0
for i in range(len(l1)):
    if l1[i]<0:
        l1[j],l1[i]=l1[i],l1[j]
        j+=1
print(l1)


'''
Dry run:
-2,1,3,4,-9,4
-2,-9,3,4,1,-4
-2,-9.-4,4,1,3
'''