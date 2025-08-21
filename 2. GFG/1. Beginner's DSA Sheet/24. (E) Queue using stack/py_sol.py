class Queue:
    def __init__(self):
        # Two stacks implemented by Python lists
        # Time/Space note per field creation: O(1)
        self._in = []   # pushes on enqueue
        self._out = []  # pops on dequeue

    def enqueue(self, X):
        # Push to in-stack: O(1) time, O(1) extra space
        self._in.append(X)

    def _shift(self):
        """Move items from in -> out only when out is empty.
        Each element is moved at most once overall.
        Amortized total cost per element: O(1)."""
        if not self._out:
            while self._in:                 # Each pop/push is O(1)
                self._out.append(self._in.pop())

    def dequeue(self):
        # Amortized O(1) time; O(1) extra space
        self._shift()
        if not self._out:
            return -1                       # queue is empty
        return self._out.pop()