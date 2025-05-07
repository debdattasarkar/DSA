
class Solution:
    def swapKth(self, arr, k):
        # Code Here
        n = len(arr)
        # Swap the kth element from the beginning and the kth element from the end
        arr[k - 1], arr[n - k] = arr[n - k], arr[k - 1]

#{ 
 # Driver Code Starts
def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    t = int(data[0])
    index = 1
    while t > 0:
        t -= 1
        k = int(data[index])
        arr = list(map(int, data[index + 1].split()))
        ob = Solution()
        ob.swapKth(arr, k)
        print(' '.join(map(str, arr)))
        index += 2
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends