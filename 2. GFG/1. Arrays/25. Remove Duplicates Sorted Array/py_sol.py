#User function template for Python

class Solution:
    def removeDuplicates(self, arr):
        #Code Here
        # Edge case: if array is empty, return 0
        if not arr:
            return 0
    
        # i points to the last position of a unique element
        i = 0
        for j in range(1, len(arr)):
            # Compare current element with the last unique
            if arr[j] != arr[i]:
                i += 1              # Move to next unique position
                arr[i] = arr[j]     # Overwrite duplicate with unique
    
        # Return total number of unique elements (index + 1)
        return i + 1


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')

    t = int(data[0])
    line = 1

    solution = Solution()

    for _ in range(t):
        if line < len(data):
            arr = list(map(int, data[line].split()))
            line += 1
            ans = solution.removeDuplicates(arr)
            for i in range(ans):
                print(arr[i], end=" ")
            print()
        print("~")

# } Driver Code Ends