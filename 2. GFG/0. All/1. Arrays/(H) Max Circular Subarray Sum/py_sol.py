class Solution:
    def maxCircularSum(self, arr):
        # code here
        def kadane(nums):
            max_end = max_so_far = nums[0]
            for x in nums[1:]:
                max_end = max(x, max_end + x)
                max_so_far = max(max_so_far, max_end)
            return max_so_far

        def min_kadane(nums):
            min_end = min_so_far = nums[0]
            for x in nums[1:]:
                min_end = min(x, min_end + x)
                min_so_far = min(min_so_far, min_end)
            return min_so_far

        total_sum = sum(arr)

        max_kadane_sum = kadane(arr)
        min_kadane_sum = min_kadane(arr)

        # If all numbers are negative, return max_kadane
        if max_kadane_sum < 0:
            result = max_kadane_sum
        else:
            circular_max = total_sum - min_kadane_sum
            result = max(max_kadane_sum, circular_max)
            
        return result