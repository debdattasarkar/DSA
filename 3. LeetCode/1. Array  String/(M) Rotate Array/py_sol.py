class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n  # Normalize k

        # Helper function to reverse elements in-place
        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        # Step 1: Reverse entire array
        reverse(0, n - 1)
        # Step 2: Reverse first k elements
        reverse(0, k - 1)
        # Step 3: Reverse the rest
        reverse(k, n - 1)