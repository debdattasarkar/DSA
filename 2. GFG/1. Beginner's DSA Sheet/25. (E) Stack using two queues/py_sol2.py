'''
    :param x: value to be inserted
    :return: None
'''
from queue import Queue

# Global queues (GFG free-function style)
queue_1 = Queue()  # first queue
queue_2 = Queue()  # second queue

def init():
    """
    Optional: call this once per test case (if your driver allows)
    to avoid leaking state across tests.
    """
    global queue_1, queue_2
    # Re-create queues because queue.Queue has no .clear()
    queue_1 = Queue()
    queue_2 = Queue()

'''
    :param x: value to be inserted
    :return: None
'''
def push(x):
    global queue_1, queue_2

    # Step 1: Push new element into queue_2
    # Time: O(1), Space: O(1)
    queue_2.put(x)

    # Step 2: Move all elements from queue_1 to queue_2
    # Time: O(n), Space: O(1)
    while not queue_1.empty():
        queue_2.put(queue_1.get())

    # Step 3: Swap the queues
    # Time: O(1), Space: O(1)
    queue_1, queue_2 = queue_2, queue_1


def pop():
    global queue_1, queue_2

    # If queue_1 is empty, the stack is empty
    if queue_1.empty():
        return -1

    # The front of queue_1 is the top of the stack
    # Time: O(1), Space: O(1)
    return queue_1.get()
