class Solution():
    def maxMinHeight(self, arr, k, w):
        # code here
        def is_possible(min_height):
            n = len(arr)
            water = [0] * (n + 1)
            ops = 0
            curr_add = 0

            for i in range(n):
                curr_add += water[i]
                actual_height = arr[i] + curr_add
                if actual_height < min_height:
                    needed = min_height - actual_height
                    ops += needed
                    if ops > k:
                        return False
                    curr_add += needed
                    if i + w < len(water):  # 🔧 fix to avoid index error
                        water[i + w] -= needed
            return True

        low, high = min(arr), max(arr) + k
        result = low

        while low <= high:
            mid = (low + high) // 2
            if is_possible(mid):
                result = mid
                low = mid + 1
            else:
                high = mid - 1

        return result