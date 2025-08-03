class Solution:
    def findMajority(self, arr):
        # code here
        n = len(arr)
        
        # Step 1: Boyer-Moore Voting for two majority candidates
        candidate1 = candidate2 = None
        count1 = count2 = 0

        for num in arr:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1
        
        # Step 2: Verify actual counts
        result = []
        for c in [candidate1, candidate2]:
            if arr.count(c) > n // 3:
                result.append(c)
        
        return sorted(result)