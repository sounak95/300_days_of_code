


l1=[[1,2,3],[4,5,6], [7,8,9]]

rows = len(l1)
cols = len(l1[0])
for i in range(rows):
    for j in range(i, cols):
        l1[i][j], l1[j][i] = l1[j][i], l1[i][j]

print(l1)