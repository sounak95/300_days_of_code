# https://practice.geeksforgeeks.org/problems/implement-queue-using-array/1


class MyQueue:

    def __init__(self):
        self.queue = [0] * 100000
        self.rear = -1
        self.front = -1

    # Function to push an element x in a queue.
    def push(self, x):
        # check full
        if self.rear == len(self.queue) - 1:
            return "-1"
        # check empty case
        elif self.front == -1 and self.rear == -1:
            self.front += 1
            self.rear += 1
            self.queue[self.rear] = x
        else:
            # normal case
            self.rear += 1
            self.queue[self.rear] = x

    # add code here

    # Function to pop an element from queue and return that element.
    def pop(self):
        # empty case
        if self.front == -1:
            return "-1"
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


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = MyQueue()
        q = int(input())
        q1 = list(map(int, input().split()))
        i = 0
        while (i < len(q1)):
            if (q1[i] == 1):
                s.push(q1[i + 1])
                i = i + 2
            elif (q1[i] == 2):
                print(s.pop(), end=" ")
                i = i + 1
            elif (s.isEmpty()):
                print(-1)
                i = i + 1
        print()

        # } Driver Code Ends