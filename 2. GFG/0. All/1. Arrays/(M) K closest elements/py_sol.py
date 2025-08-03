class Solution:
    def printKClosest(self, arr, k, x):
        # code here
        candidates = []

        for num in arr:
            if num == x:
                continue
            # First by absolute difference, then by higher value
            candidates.append((abs(num - x), -num, num))

        # Sort using the first two criteria
        candidates.sort()

        # Extract the last value from each tuple (the actual number), first k only
        result = [val for _, _, val in candidates[:k]]
        return result