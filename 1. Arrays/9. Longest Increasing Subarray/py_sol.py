#User function Template for python3

class Solution:
    def lenOfLongIncSubArr(self, arr):
        #Code here
        n = len(arr)
        max_len = 1
        curr_len = 1
    
        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                curr_len += 1
                max_len = max(max_len, curr_len)
            else:
                curr_len = 1
    
        return max_len

#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')

    t = int(data[0])
    results = []

    for i in range(1, t + 1):
        arr = list(map(int, data[i].split()))
        solution = Solution()
        ans = solution.lenOfLongIncSubArr(arr)
        results.append(ans)

    for result in results:
        print(result)
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends