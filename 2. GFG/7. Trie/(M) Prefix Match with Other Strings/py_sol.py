#User function Template for python3

class Solution:
    def klengthpref(self,arr,n,k,s):
        # return list of words(str) found in the board
        # If str is shorter than k, no matches possible
        if len(s) < k:
            return 0

        # Extract k-length prefix of str
        prefix = s[:k]
        count = 0

        for word in arr:
            # Check if current word has at least k characters
            if len(word) >= k:
                # Check prefix match
                if word[:k] == prefix:
                    count += 1

        return count