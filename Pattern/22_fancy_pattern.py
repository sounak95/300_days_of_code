'''
********1********
*******2*2*******
******3*3*3******
*****4*4*4*4*****
****5*5*5*5*5****
'''
n=5

for i in range(n):
    start_num_index = 8 - i
    num=i+1
    count_num = i + 1
    for j in range(17):

        if (j==start_num_index and count_num>0):
            print(num, end='')
            count_num-=1
            start_num_index+=2
        else:
            print('*', end='')
    print()

