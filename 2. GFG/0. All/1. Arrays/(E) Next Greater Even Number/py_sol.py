#User function Template for python3

class Solution:
    def getNextEven(self, x: str) -> int:
        # Your code goes here
        from itertools import permutations
        
        digits = list(x)
        n = len(digits)
        
        def next_permutation(arr):
            i = n - 2
            while i >= 0 and arr[i] >= arr[i + 1]:
                i -= 1
            if i == -1:
                return False
            j = n - 1
            while arr[j] <= arr[i]:
                j -= 1
            arr[i], arr[j] = arr[j], arr[i]
            arr[i + 1:] = reversed(arr[i + 1:])
            return True

        arr = list(digits)
        orig = int(x)

        while next_permutation(arr):
            num = int("".join(arr))
            if num > orig and int(arr[-1]) % 2 == 0:
                return num
        return -1