#User function Template for python3

class Solution:
    def rearrange(self,arr):
        # code here
        pos = [x for x in arr if x >= 0]
        neg = [x for x in arr if x < 0]

        result = []
        i = j = 0

        # Alternate starting with positive
        while i < len(pos) and j < len(neg):
            result.append(pos[i])
            i += 1
            result.append(neg[j])
            j += 1

        # Append remaining elements
        result.extend(pos[i:])
        result.extend(neg[j:])
         # In-place update
        arr[:] = result

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.rearrange(arr)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends