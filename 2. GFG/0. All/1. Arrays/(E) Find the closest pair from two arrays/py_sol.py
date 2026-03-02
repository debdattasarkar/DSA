class Solution:
    @staticmethod
    def findClosestPair(arr1, arr2, x):
        # Two pointers (arrays are sorted)
        # Time: O(n + m), Space: O(1)

        i = 0
        j = len(arr2) - 1

        best_pair = [arr1[0], arr2[j]]
        best_diff = abs(arr1[0] + arr2[j] - x)

        while i < len(arr1) and j >= 0:
            current_sum = arr1[i] + arr2[j]
            current_diff = abs(current_sum - x)

            if current_diff < best_diff:
                best_diff = current_diff
                best_pair = [arr1[i], arr2[j]]

            if current_sum == x:
                return [arr1[i], arr2[j]]

            if current_sum > x:
                j -= 1
            else:
                i += 1

        return best_pair