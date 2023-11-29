# https://leetcode.com/problems/design-circular-deque/


class MyCircularDeque(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.queue=[-1] * k
        self.front = -1
        self.rear = -1
        self.size = k


    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        elif self.isEmpty():
            self.front=0
            self.rear=0
        else:
            self.front=(self.front-1)% self.size
        self.queue[self.front]= value
        return True


    def insertLast(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        elif self.isEmpty():
            self.front=self.rear=0
        else:
            self.rear=(self.rear+1)% self.size
        self.queue[self.rear] = value
        return True

    def deleteFront(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        # single element
        elif self.front==self.rear:
            data = self.queue[self.front]
            self.queue[self.front] = -1
            self.front=-1
            self.rear=-1
        else:
            self.queue[self.front]=-1
            self.front=(self.front+1)%self.size
        return True


    def deleteLast(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        elif self.front==self.rear:
            self.queue[self.rear]=-1
            self.rear=-1
            self.front=-1
        else:
            self.queue[self.rear]=-1
            self.rear=(self.rear-1)% self.size
        return True

    def getFront(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.queue[self.front]



    def getRear(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.queue[self.rear]


    def isEmpty(self):
        """
        :rtype: bool
        """
        if self.front==-1 and self.rear==-1:
            return True
        return False


    def isFull(self):
        """
        :rtype: bool
        """
        if (self.rear + 1)% self.size==self.front:
            return True
        return False



# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()