class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            curr_sum = numbers[left] + numbers[right]

            if curr_sum == target:
                # Return 1-based indices
                return [left + 1, right + 1]
            elif curr_sum < target:
                left += 1  # Need a bigger sum
            else:
                right -= 1  # Need a smaller sum

        return []  # Won't be reached as per constraints