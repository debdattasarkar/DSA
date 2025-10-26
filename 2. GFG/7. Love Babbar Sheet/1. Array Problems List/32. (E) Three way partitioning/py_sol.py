#User function template for Python

class Solution:
    #Function to partition the array around the range such 
    #that array is divided into three parts.
	def threeWayPartition(self, arr, a, b):
	    """
        In-place 3-way partition around [a, b] using Dutch National Flag pointers.
        Time  : O(n)   -- each index is processed at most once
        Space : O(1)   -- only a few pointers
        Modifies arr in place and returns it (convenient for testing).
        """
        low, mid, high = 0, 0, len(arr) - 1

        while mid <= high:
            if arr[mid] < a:
                # send to left zone
                arr[low], arr[mid] = arr[mid], arr[low]
                low += 1
                mid += 1
            elif a <= arr[mid] <= b:
                # stays in the middle zone
                mid += 1
            else:  # arr[mid] > b
                # send to right zone; do NOT advance mid yet
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1

        return arr  # optional (GFG validates by checking partition property)