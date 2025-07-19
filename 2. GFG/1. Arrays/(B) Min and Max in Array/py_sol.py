#User function Template for python3

class Solution:
    def get_min_max(self, arr):
        # Handle edge case: if array is empty
        if not arr:
            return None, None

        # Initialize min and max to the first element
        min_val = max_val = arr[0]

        # Traverse the array
        for num in arr[1:]:
            if num < min_val:
                min_val = num
            elif num > max_val:
                max_val = num

        return min_val, max_val