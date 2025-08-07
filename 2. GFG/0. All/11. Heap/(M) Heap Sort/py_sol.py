class Solution:
    def heapify(self, arr, n, i):
        # Maintain max heap property for subtree rooted at index i
        largest = i       # Initialize largest as root
        left = 2 * i + 1  # left child
        right = 2 * i + 2 # right child

        # If left child is larger than root
        if left < n and arr[left] > arr[largest]:
            largest = left

        # If right child is larger than largest so far
        if right < n and arr[right] > arr[largest]:
            largest = right

        # If largest is not root
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # swap
            self.heapify(arr, n, largest)  # Recursively heapify the affected subtree

    def heapSort(self, arr):
        n = len(arr)

        # Step 1: Build a maxheap
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)

        # Step 2: One by one extract elements
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]  # Swap
            self.heapify(arr, i, 0)         # Heapify the reduced heap