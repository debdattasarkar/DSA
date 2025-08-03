class Solution:
    def splitArray(self, arr, k):
        # code here
        def isValid(mid):
            count = 1
            curr_sum = 0
            for num in arr:
                if curr_sum + num > mid:
                    count += 1
                    curr_sum = num
                else:
                    curr_sum += num
            return count <= k

        low = max(arr)
        high = sum(arr)
        while low < high:
            mid = (low + high) // 2
            if isValid(mid):
                high = mid
            else:
                low = mid + 1
        return low