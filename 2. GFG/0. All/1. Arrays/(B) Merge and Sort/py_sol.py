#User function Template for python3

class Solution:
    def mergeNsort(self, arr, brr):
        # Write your code here
        merged = arr + brr
        merged = list(set(merged))
        merged.sort()
        return merged