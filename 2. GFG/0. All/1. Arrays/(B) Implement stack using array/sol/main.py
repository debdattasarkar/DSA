class MyStack:

    def __init__(self):
        # Stack is implemented using a list
        self.arr = []

    # Function to push an integer into the stack
    def push(self, data):
        self.arr.append(data)  # O(1) time — append to end of list

    # Function to remove and return the top element from the stack
    def pop(self):
        if not self.arr:
            return -1  # Special case: empty stack
        return self.arr.pop()  # O(1) time — removes last element
    
if __name__ == "__main__":
    stack = MyStack()

    # Push elements
    print("Pushing 10")
    stack.push(10)
    print("Pushing 20")
    stack.push(20)
    print("Pushing 30")
    stack.push(30)

    # Pop elements
    print("Popped:", stack.pop())  # Expected: 30
    print("Popped:", stack.pop())  # Expected: 20
    print("Popped:", stack.pop())  # Expected: 10
    print("Popped:", stack.pop())  # Expected: -1 (empty stack)