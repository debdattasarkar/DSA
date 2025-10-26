#User function Template for python3

class Solution:
        
    def minSwap (self,arr, k) : 
        """
        Minimum swaps to group all elements <= k into a contiguous subarray.
        Idea: Let 'good' be count of elements <= k.
              Slide a window of length 'good'; in each window count how many 'bad' (>k).
              The minimum 'bad' over all windows equals the minimum swaps required.
        Time  : O(n)
        Space : O(1)
        """
        n = len(arr)
        # 1) Count how many elements are <= k (these should end up together)
        good = sum(1 for x in arr if x <= k)
        if good <= 1:
            return 0  # nothing to group or single item

        # 2) Count bad (>k) in the first window of size 'good'
        bad = sum(1 for i in range(good) if arr[i] > k)
        min_swaps = bad

        # 3) Slide the window across the array; update 'bad' in O(1)
        left = 0
        for right in range(good, n):
            # include new element at 'right'
            if arr[right] > k:
                bad += 1
            # exclude old element at 'left'
            if arr[left] > k:
                bad -= 1
            left += 1
            # track the minimum bad seen
            if bad < min_swaps:
                min_swaps = bad

        return min_swaps