# https://leetcode.com/problems/design-circular-queue/


class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.size = k
        self.queue=[-1] * k
        self.rear=-1
        self.front=-1

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        # check full
        if self.isFull():
            return False
        # check empty
        elif self.isEmpty():
            self.rear+=1
            self.front+=1
            self.queue[self.rear] = value
            return True
        else:
            # check normal case
            self.rear = (self.rear+1)% self.size
            self.queue[self.rear] = value
            return True

    def deQueue(self):
        """
        :rtype: bool
        """
        # check empty
        if self.isEmpty():
            return False
        # check single element
        elif (self.front==self.rear):
            self.queue[self.front]=-1
            # reset queue
            self.front=-1
            self.rear=-1
            return True
        else:
            # normal case
            data = self.queue[self.front]
            self.queue[self.front]=-1
            self.front = (self.front+1)% self.size
            return True


    def Front(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def Rear(self):
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
        if self.front == -1 and self.rear == -1:
            return True

    def isFull(self):
        """
        :rtype: bool
        """
        if (self.rear+1)%self.size==self.front:
            return True

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()