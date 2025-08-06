class Solution:
    def insertionSort(self, arr):
        # code here
        n = len(arr)
        for i in range(1, n):
            key = arr[i]  # Current element to place correctly
            j = i - 1
            # Move elements greater than key to one position ahead
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            # Place key after the last smaller element
            arr[j + 1] = key