class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)  # O(n) time & space

        max_len = 0

        for num in num_set:
            # Start only if it's the beginning of a sequence
            if num - 1 not in num_set:
                current = num
                streak = 1

                # Expand the streak
                while current + 1 in num_set:
                    current += 1
                    streak += 1

                max_len = max(max_len, streak)

        return max_len