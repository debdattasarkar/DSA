class Solution(object):
    def kthSmallest(self, m, n, k):
        #code here
        def countLessEqual(x):
            count = 0
            for i in range(1, m + 1):
                count += min(x // i, n)
            return count

        left, right = 1, m * n
        while left < right:
            mid = (left + right) // 2
            if countLessEqual(mid) < k:
                left = mid + 1
            else:
                right = mid
        return left
