class Solution:
    def findDuplicates(self, arr):
        # code here
        n = len(arr)
        result = []

        for i in range(n):
            idx = abs(arr[i])
            if arr[idx % n] >= n * 2:
                continue  # Already recorded
            elif arr[idx % n] >= n:
                result.append(idx % n)  # Duplicate found
                arr[idx % n] += n       # Mark as fully recorded
            else:
                arr[idx % n] += n        # Mark as seen once

        return sorted(result)