class Solution:
    def countSubset(self, arr, k):
        n = len(arr)
        mid = n // 2

        left_part = arr[:mid]
        right_part = arr[mid:]

        # Generate all subset sums for a list, return list of sums
        # Time: O(2^m), Space: O(2^m)
        def generate_sums(nums):
            sums = []

            def dfs(i, running_sum):
                if i == len(nums):
                    sums.append(running_sum)
                    return
                # not take
                dfs(i + 1, running_sum)
                # take
                dfs(i + 1, running_sum + nums[i])

            dfs(0, 0)
            return sums

        left_sums = generate_sums(left_part)     # size up to 2^(n/2)
        right_sums = generate_sums(right_part)   # size up to 2^(n/2)

        # Build frequency map of right sums
        right_count = {}
        for s in right_sums:
            right_count[s] = right_count.get(s, 0) + 1

        # For each left sum, add how many right sums make total k
        total_ways = 0
        for sL in left_sums:
            needed = k - sL
            total_ways += right_count.get(needed, 0)

        return total_ways