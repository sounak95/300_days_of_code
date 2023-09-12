
l1=[[1,2,3],[4,5,6], [7,8,9]]

rows = len(l1)
cols = len(l1[0])
for i in range(cols):
    for j in range(rows):
        print(l1[j][i], end=' ')
    print()