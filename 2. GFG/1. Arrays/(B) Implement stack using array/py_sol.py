class MyStack:
    
    def __init__(self):
        self.arr=[]
    
    #Function to push an integer into the stack.
    def push(self,data):
        #add code here
        self.arr.append(data)  # Add element to end
    
    #Function to remove an item from top of the stack.
    def pop(self):
        #add code here
        if not self.arr:
            return -1  # Stack is empty
        return self.arr.pop()  # Removes and returns top element
        
        