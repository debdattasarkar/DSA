from queue import Queue

queue_1 = Queue() # first queue
queue_2 = Queue() # second queue

def push(x):

    global queue_1
    global queue_2
    # code here
    
    # Step 1: Push new element into queue_2
    queue_2.put(x)  # Time: O(1), Space: O(1)

    # Step 2: Move all elements from queue_1 to queue_2
    while not queue_1.empty():
        queue_2.put(queue_1.get())  # Time: O(n), Space: O(1)

    # Step 3: Swap the queues
    queue_1, queue_2 = queue_2, queue_1  # Time: O(1), Space: O(1)

def pop():

    global queue_1
    global queue_2

    # code here
        # If queue_1 is empty, the stack is empty
    if queue_1.empty():
        return -1

    # The front of queue_1 is the top of the stack
    return queue_1.get()  # Time: O(1), Space: O(1)