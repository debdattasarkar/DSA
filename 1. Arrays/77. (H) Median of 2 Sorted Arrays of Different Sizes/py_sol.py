#User function Template for python3

class Solution:
    def medianOf2(self, a, b):
        #code here
       # Always binary search on the smaller array for efficiency
        if len(a) > len(b):
            a, b = b, a

        n, m = len(a), len(b)
        total = n + m
        half = (total + 1) // 2  # ensures left side has the middle element when total is odd

        l, r = 0, n
        while l <= r:
            i = (l + r) // 2       # Partition in a
            j = half - i           # Partition in b

            # Handle edges using -∞ and ∞
            a_left = a[i - 1] if i > 0 else float('-inf')
            a_right = a[i] if i < n else float('inf')
            b_left = b[j - 1] if j > 0 else float('-inf')
            b_right = b[j] if j < m else float('inf')

            if a_left <= b_right and b_left <= a_right:
                if total % 2 == 0:
                    return (max(a_left, b_left) + min(a_right, b_right)) / 2
                else:
                    return max(a_left, b_left)
            elif a_left > b_right:
                r = i - 1
            else:
                l = i + 1


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    tcs = int(input())

    for _ in range(tcs):
        arr1 = [int(x) for x in input().split()]
        arr2 = [int(x) for x in input().split()]

        ob = Solution()

        if len(arr2) == 1 and arr2[0] == 0:
            arr2 = []
        ans = ob.medianOf2(arr1, arr2)
        if int(ans) == ans:
            print(int(ans))
        else:
            print(ans)
        print("~")

# } Driver Code Ends