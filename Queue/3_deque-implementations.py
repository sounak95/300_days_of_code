# https://www.codingninjas.com/studio/problems/deque_1170059


from os import *
from sys import *
from collections import *
from math import *

class Deque:
    def __init__(self, size):
        # Write your code here
        self.queue=[-1] * size
        self.size = size
        self.front=-1
        self.rear=-1

    # Pushes 'X' in the front of the deque. Returns true if it gets pushed into the deque, and false otherwise.
    def pushFront(self, x):
        # Write your code here
        # check overflow
        if self.front==0:
            return False
        # check empty case
        elif self.front == -1 and self.rear == -1:
            self.front += 1
            self.rear += 1
            self.queue[self.front] = x
            return True
        else:
            # normal case
            self.front -= 1
            self.queue[self.front] = x
            return True

    # Pushes 'X' in the back of the deque. Returns true if it gets pushed into the deque, and false otherwise.
    def pushRear(self, x):
        # Write your code here
        # check full
        if self.rear == self.size - 1:
            return False
        # check empty case
        elif self.front == -1 and self.rear == -1:
            self.front += 1
            self.rear += 1
            self.queue[self.rear] = x
            return True
        else:
            # normal case
            self.rear += 1
            self.queue[self.rear] = x
            return True

    # Pops an element from the front of the deque. Returns -1 if the deque is empty, otherwise returns the popped element.
    def popFront(self):
        # Write your code here
        # empty case
        if self.front == -1:
            return -1
        # single element
        elif self.front == self.rear:
            data = self.queue[self.front]
            self.queue[self.front] = -1
            # reset queue
            self.front = -1
            self.rear = -1
            return data

        else:
            data = self.queue[self.front]
            self.queue[self.front] = -1
            self.front += 1
            return data

    # Pops an element from the back of the deque. Returns -1 if the deque is empty, otherwise returns the popped element.
    def popRear(self):
        # Write your code here
        # empty case
        if self.rear == -1 and self.front==-1:
            return -1
        # single element
        elif self.front == self.rear:
            data = self.queue[self.rear]
            self.queue[self.rear] = -1
            # reset queue
            self.front = -1
            self.rear = -1
            return data

        else:
            data = self.queue[self.rear]
            self.queue[self.rear] = -1
            self.rear -= 1
            return data

    # Returns the first element of the deque. If the deque is empty, it returns -1.
    def getFront(self):
        # Write your code here
        if self.rear == -1 and self.front==-1:
            return -1
        return self.queue[self.front]

    # Returns the last element of the deque. If the deque is empty, it returns -1.
    def getRear(self):
        # Write your code here
        if self.rear == -1 and self.front == -1:
            return -1
        return self.queue[self.rear]

    # Returns true if the deque is empty. Otherwise returns false.
    def isEmpty(self):
        # Write your code here
        if self.rear == -1 and self.front==-1:
            return True
        return False

    # Returns true if the deque is full. Otherwise returns false.
    def isFull(self):
        # Write your code here
        if self.rear == self.size - 1:
            return True
        return False
