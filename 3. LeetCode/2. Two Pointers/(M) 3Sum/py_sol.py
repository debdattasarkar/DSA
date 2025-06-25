class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort to apply two-pointer technique
        res = []
        n = len(nums)

        for i in range(n):
            # Skip duplicate elements for the first position
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = -nums[i]
            left, right = i + 1, n - 1

            while left < right:
                two_sum = nums[left] + nums[right]
                if two_sum < target:
                    left += 1
                elif two_sum > target:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # Skip duplicates for second and third elements
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        return res