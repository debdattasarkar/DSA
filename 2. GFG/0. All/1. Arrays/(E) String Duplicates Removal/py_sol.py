#User function Template for python3
class Solution:
	def removeDuplicates(self, s):
	    # code here
        seen = set()
        result = []
        
        for ch in s:
            if ch not in seen:
                seen.add(ch)
                result.append(ch)
        
        return ''.join(result)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        str = input().strip()
        ob = Solution()
        ans = ob.removeDuplicates(str)
        print(ans)
        tc -= 1

        print("~")

# } Driver Code Ends