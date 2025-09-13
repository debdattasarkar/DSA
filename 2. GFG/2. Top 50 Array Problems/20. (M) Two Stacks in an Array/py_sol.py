class TwoStacks:
    def __init__(self):
        """
        One array, two stacks growing from opposite ends.

        top1: index of top in stack1 (starts at -1, grows right)
        top2: index of top in stack2 (starts at cap, grows left)

        Time per operation: O(1)
        Space: O(cap)
        """
        self.cap = 100              # default capacity per constraints
        self.arr = [None] * self.cap
        self.top1 = -1
        self.top2 = self.cap

    # Function to push an integer into stack 1
    def push1(self, x):
        # O(1): check free space
        if self.top1 + 1 == self.top2:
            # Overflow — no room left
            return
        self.top1 += 1              # move top1 right
        self.arr[self.top1] = x     # place item

    # Function to push an integer into stack 2
    def push2(self, x):
        # O(1): check free space
        if self.top1 + 1 == self.top2:
            # Overflow — no room left
            return
        self.top2 -= 1              # move top2 left
        self.arr[self.top2] = x     # place item

    # Function to remove an element from top of stack 1
    def pop1(self):
        # O(1): underflow if empty
        if self.top1 == -1:
            return -1
        val = self.arr[self.top1]
        self.top1 -= 1              # shrink stack1
        return val

    # Function to remove an element from top of stack 2
    def pop2(self):
        # O(1): underflow if empty
        if self.top2 == self.cap:
            return -1
        val = self.arr[self.top2]
        self.top2 += 1              # shrink stack2
        return val
        