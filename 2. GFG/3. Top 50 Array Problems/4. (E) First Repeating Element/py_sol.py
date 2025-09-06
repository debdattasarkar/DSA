class Solution:
    def firstRepeated(self,arr):
        # code here 
        """
        Reverse-scan trick: the last index we set while moving left is
        the smallest index of a repeating value.
        Time:  O(n)
        Space: O(n)
        """
        seen = set()
        ans = -1
        for i in range(len(arr) - 1, -1, -1):  # right -> left
            if arr[i] in seen:
                ans = i + 1                    # 1-based
            else:
                seen.add(arr[i])
        return ans