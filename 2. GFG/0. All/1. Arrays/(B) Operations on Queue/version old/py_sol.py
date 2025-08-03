#User function Template for python3
from collections import deque
class Solution:
    '''
    Function Arguments :
    		@param  : q (given list on which queue is implemented)
    		@param  : x (value to be used accordingly)
    		@return : None
    '''
    
    # Function to push an element in queue.
    def enqueue(self, q, x):
        q.append(x)  # O(1) append to rear

    # Function to remove front element from queue.
    def dequeue(self, q):
        return q.pop(0) if q else -1  # O(1) pop from front

    # Function to find the front element of queue.
    def front(self, q):
        return q[0] if q else -1  # O(1) peek front

    # Function to find an element in the queue.
    def find(self, q, x):
        return x in q  # O(n) linear search