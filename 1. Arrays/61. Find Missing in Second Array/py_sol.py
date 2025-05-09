#User function Template for python3
class Solution:
    def findMissing(self,a,b):
        # code here
        b_set = set(b)  # Use set for fast lookup
        result = []
        for num in a:
            if num not in b_set:
                result.append(num)
        return result

#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ob = Solution()
    ans = ob.findMissing(a, b)
    for each in ans:
        print(each, end=' ')
    print()
    print("~")

# } Driver Code Ends