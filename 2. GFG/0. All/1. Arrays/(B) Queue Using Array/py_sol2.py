from collections import deque
import time

class MyQueue:
    def __init__(self):
        # Initialize deque for efficient O(1) operations
        self.queue = deque()  # Time: O(1), Space: O(1)

    # Function to push an element x into the queue
    def push(self, x):
        self.queue.append(x)  # Enqueue at the rear → O(1)

    # Function to pop an element from the queue
    def pop(self):
        if not self.queue:
            return -1  # Queue is empty → O(1)
        return self.queue.popleft()  # Dequeue from the front → O(1)
    
if __name__ == "__main__":
    q = MyQueue()

    print("Running deque-based queue operations...\n")

    start_time = time.time()  # Start timing

    # Push elements
    q.push(10)
    q.push(20)
    q.push(30)
    q.push(40)

    # Pop elements
    print("Popped:", q.pop())  # Expected: 10
    print("Popped:", q.pop())  # Expected: 20

    # More pushes
    q.push(50)
    q.push(60)

    # Pop remaining
    print("Popped:", q.pop())  # Expected: 30
    print("Popped:", q.pop())  # Expected: 40
    print("Popped:", q.pop())  # Expected: 50
    print("Popped:", q.pop())  # Expected: 60
    print("Popped:", q.pop())  # Expected: -1

    end_time = time.time()  # End timing

    print(f"\nExecution Time: {end_time - start_time:.8f} seconds")