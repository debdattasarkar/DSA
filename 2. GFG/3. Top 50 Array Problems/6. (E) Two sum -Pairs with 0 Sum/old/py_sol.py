#User function Template for python3

class Solution:
    def getPairs(self, arr):
        # code here
        seen = set()
        result = set()

        for num in arr:
            if -num in seen:
                result.add(tuple(sorted((num, -num))))
            seen.add(num)
        
        return sorted([list(pair) for pair in result])