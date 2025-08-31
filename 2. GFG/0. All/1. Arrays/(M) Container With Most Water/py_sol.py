class Solution:
    def maxWater(self, arr):
        # code here
        # Two-pointer greedy
        # Time: O(n), Space: O(1)
        n = len(arr)
        if n < 2:
            return 0
        
        i, j = 0, n - 1
        best = 0
        
        while i < j:
            # Current area using the shorter boundary as height
            h = arr[i] if arr[i] < arr[j] else arr[j]
            area = h * (j - i)
            if area > best:
                best = area
            
            # Move the pointer at the shorter wall to try to find a taller wall
            if arr[i] < arr[j]:
                i += 1
            elif arr[i] > arr[j]:
                j -= 1
            else:
                # Equal heights: moving either is fine; move both to prune width
                i += 1
                j -= 1
        
        return best