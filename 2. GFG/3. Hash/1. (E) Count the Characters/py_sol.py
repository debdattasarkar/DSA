#User function Template for python3

class Solution:
    def getCount (self,S, N):
        # your code here
        # Step 1: Collapse consecutive characters to count as one
        collapsed = []
        for ch in S:
            if not collapsed or collapsed[-1] != ch:
                collapsed.append(ch)
        
        # Step 2: Count frequencies
        freq = {}
        for ch in collapsed:
            freq[ch] = freq.get(ch, 0) + 1

        # Step 3: Count how many characters occurred exactly N times
        count = sum(1 for v in freq.values() if v == N)
        return count

#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    s, n = input().split()
    s = str(s)
    n = int(n)
    ob = Solution()
    print (ob.getCount (s, n))

    print("~")
# Contributed By: Pranay Bansal

# } Driver Code Ends