class kQueues:
    def __init__(self, n, k):
        # n = total slots in the single array
        # k = number of queues
        self.n = n
        self.k = k

        # data stores actual values
        self.data = [0] * n

        # next_index acts like "next pointer" for each slot
        self.next_index = list(range(1, n)) + [-1]  # 0->1->2->...->n-1->-1

        # front and rear pointers for each of k queues
        self.front = [-1] * k
        self.rear = [-1] * k

        # head of free list (first free slot index)
        self.free_head = 0

    def enqueue(self, x, i):
        # Enqueue element x into queue number i
        # Time: O(1)
        if self.free_head == -1:
            # No free space available (array full)
            return

        # Take a free index from free list
        new_index = self.free_head
        self.free_head = self.next_index[new_index]

        # Store value
        self.data[new_index] = x
        self.next_index[new_index] = -1  # new node will be the tail

        # If queue i is empty, new node becomes front and rear
        if self.front[i] == -1:
            self.front[i] = self.rear[i] = new_index
        else:
            # Link it after current rear
            self.next_index[self.rear[i]] = new_index
            self.rear[i] = new_index

    def dequeue(self, i):
        # Dequeue element from queue number i
        # Time: O(1)
        if self.front[i] == -1:
            return -1  # queue empty

        # Get front index of queue i
        removed_index = self.front[i]
        result = self.data[removed_index]

        # Move front to next node
        self.front[i] = self.next_index[removed_index]

        # If queue becomes empty, update rear too
        if self.front[i] == -1:
            self.rear[i] = -1

        # Add removed index back to free list
        self.next_index[removed_index] = self.free_head
        self.free_head = removed_index

        return result

    def isEmpty(self, i):
        # Check if queue i is empty
        # Time: O(1)
        return self.front[i] == -1

    def isFull(self):
        # Check if array is full
        # Time: O(1)
        return self.free_head == -1
