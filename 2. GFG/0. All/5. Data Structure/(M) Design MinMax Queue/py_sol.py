from collections import deque
class SpecialQueue:
    def __init__(self):
        # FIFO queue to store actual elements
        self.q = deque()
        # Monotonic deques:
        # minDQ keeps elements in non-decreasing order; front is the min
        self.minDQ = deque()
        # maxDQ keeps elements in non-increasing order; front is the max
        self.maxDQ = deque()

    def enqueue(self, x):
        # Push to main queue
        self.q.append(x)

        # Maintain minDQ: remove larger elements from the back
        while self.minDQ and self.minDQ[-1] > x:
            self.minDQ.pop()
        self.minDQ.append(x)

        # Maintain maxDQ: remove smaller elements from the back
        while self.maxDQ and self.maxDQ[-1] < x:
            self.maxDQ.pop()
        self.maxDQ.append(x)

    def dequeue(self):
        # Pop from main queue
        val = self.q.popleft()

        # Synchronize with minDQ / maxDQ if the popped value is at their front
        if self.minDQ and val == self.minDQ[0]:
            self.minDQ.popleft()
        if self.maxDQ and val == self.maxDQ[0]:
            self.maxDQ.popleft()

        return val

    def getFront(self):
        # Front of main queue
        return self.q[0]

    def getMin(self):
        # Min is at front of minDQ
        return self.minDQ[0]

    def getMax(self):
        # Max is at front of maxDQ
        return self.maxDQ[0]
