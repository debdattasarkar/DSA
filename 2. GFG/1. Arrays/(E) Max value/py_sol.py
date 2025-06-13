#User function Template for python3

class Solution:
    def maxVal(self, arr):
        # Code Here
        max_diff = float('-inf')
        min_diff = float('inf')
    
        for i in range(len(arr)):
            val = arr[i] - i
            max_diff = max(max_diff, val)
            min_diff = min(min_diff, val)
    
        return max_diff - min_diff
            


#{ 
 # Driver Code Starts
def main():
    t = int(input().strip())

    while t > 0:
        line = input().strip()
        nums = list(map(int, line.split()))
        ob = Solution()
        print(ob.maxVal(nums))
        t -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends