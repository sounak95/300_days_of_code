# https://leetcode.com/problems/min-stack/

class MinStack(object):

    def __init__(self):
        self.st=[]

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if len(self.st)==0:
            ele = (val,val)
            self.st.append(ele)
        else:
            purana_min = self.st[-1][1]
            new_min =  min(val, purana_min)
            ele = (val, new_min)
            self.st.append(ele)

    def pop(self):
        """
        :rtype: None
        """
        self.st.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.st[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        return self.st[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()