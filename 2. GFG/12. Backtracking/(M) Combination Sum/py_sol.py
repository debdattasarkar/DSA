#User function Template for python3

class Solution:
    
    # Function to find all combinations of elements
    # in array arr that sum to target.
    def combinationSum(self, arr, target):
        # code here
        res = []
        arr.sort()  # sort to help with pruning and consistency

        def backtrack(index, path, remaining):
            if remaining == 0:
                res.append(path[:])
                return
            if remaining < 0 or index == len(arr):
                return

            # include arr[index]
            path.append(arr[index])
            backtrack(index, path, remaining - arr[index])
            path.pop()

            # exclude arr[index] and move forward
            backtrack(index + 1, path, remaining)

        backtrack(0, [], target)
        return res