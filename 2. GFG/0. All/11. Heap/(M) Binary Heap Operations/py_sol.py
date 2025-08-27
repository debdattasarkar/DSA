'''
heap = [0 for i in range(101)]  # our heap to be used
'''
# We'll use 1-based indexing inside the heap array, so heap[1] is the root.
curr_size = 0  # global size

def _swap(i, j):
    heap[i], heap[j] = heap[j], heap[i]

def _bubble_up(i):
    # Move the node at index i up until the heap property is restored.
    while i > 1:
        p = i // 2
        if heap[i] < heap[p]:
            _swap(i, p)
            i = p
        else:
            break

def _heapify(i):
    # Standard min-heapify down from index i
    while True:
        left = 2 * i
        right = left + 1
        smallest = i

        if left <= curr_size and heap[left] < heap[smallest]:
            smallest = left
        if right <= curr_size and heap[right] < heap[smallest]:
            smallest = right

        if smallest != i:
            _swap(i, smallest)
            i = smallest
        else:
            break
        
#Function to insert a value in Heap.
def insertKey (x):
    global curr_size
    # Assume capacity is enough (101). If needed, guard here.
    curr_size += 1
    heap[curr_size] = x
    _bubble_up(curr_size)  # O(log n)

#Function to delete a key at ith index.
def deleteKey (i):
    global curr_size
    # Convert 0-based to our internal 1-based index
    idx = i + 1
    if idx < 1 or idx > curr_size:
        return  # invalid index, ignore

    # Move last to idx, shrink
    _swap(idx, curr_size)
    curr_size -= 1

    # Fix heap - either it needs to bubble up or heapify down
    # Try bubble up first; if it doesn't move, heapify down.
    _bubble_up(idx)
    _heapify(idx)


#Function to extract minimum value in heap and then to store 
#next minimum value at first index.
# Function to extract minimum value; return -1 if empty.
def extractMin ():
    global curr_size
    if curr_size == 0:
        return -1
    root = heap[1]
    # Move last to root and heapify
    heap[1] = heap[curr_size]
    curr_size -= 1
    if curr_size > 0:
        _heapify(1)  # O(log n)
    return root