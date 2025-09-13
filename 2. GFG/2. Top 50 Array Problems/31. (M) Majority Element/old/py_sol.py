class Solution:
    def majorityElement(self, arr):
        #code here
        count = 0
        candidate = None

        # Step 1: Find a candidate using Boyer-Moore
        for num in arr:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1

        # Step 2: Verify the candidate
        if arr.count(candidate) > len(arr) // 2:
            return candidate
        return -1