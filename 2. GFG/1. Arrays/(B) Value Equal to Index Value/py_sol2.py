#User function Template for python3
class Solution:
    # Function to find values in array equal to their indices
    def valueEqualToIndex(self, arr):
        return [arr[i] for i in range(len(arr)) if arr[i]== i+1]