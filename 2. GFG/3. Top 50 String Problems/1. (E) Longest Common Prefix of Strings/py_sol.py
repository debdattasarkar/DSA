#User function Template for python3
class Solution:
    def longestCommonPrefix(self, arr):
        # Edge cases
        if not arr:
            return ""
        if len(arr) == 1:
            return arr[0]
        
        # 1) Take the first string as the current prefix
        prefix = arr[0]
        
        # 2) Reduce prefix until it prefixes each next string
        for s in arr[1:]:
            # While s doesn't start with prefix, chop off last char
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:  # early exit: no common prefix
                    return ""
        
        return prefix