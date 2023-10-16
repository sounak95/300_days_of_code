

def find_subsequence(str1, output, index, ans):

    if index==len(str1):
        print(output)
        ans.append(output)
        return

    find_subsequence(str1, output+str1[index],index+1 , ans)

    find_subsequence(str1, output,index+1, ans)

ans=[]
find_subsequence("abc", "", 0, ans)
print(ans)
