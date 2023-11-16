# https://www.codingninjas.com/studio/problems/redundant-brackets_975473

def findRedundantBrackets(s):
	# Write your code here.
	# Return boolean True or False.
    st=[]
    for ch in s:
        if ch=='(' or ch=='+'or ch=='-' or ch=='*' or ch=='/':
            st.append(ch)
        elif ch==')':
            op_count=0
            while(len(st)!=0 and st[-1]!='('):
                ele = st[-1]
                if ele=='+' or ele=='-' or ele=='/' or ele=='*':
                    op_count+=1
                st.pop()

            if op_count==0:
                return True

            # reached till '(' in stack
            st.pop()

    return False

print(findRedundantBrackets("(a+b)"))