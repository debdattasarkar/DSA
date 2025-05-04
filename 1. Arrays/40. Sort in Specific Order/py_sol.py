#User function Template for python3

class Solution:
    def sortIt(self, arr):
        #code here.
        # Separate odd and even numbers
        odd = [x for x in arr if x % 2 != 0]
        even = [x for x in arr if x % 2 == 0]
    
        # Sort odd numbers in descending order
        odd.sort(reverse=True)
        # Sort even numbers in ascending order
        even.sort()
        # Combine both parts
        arr[:] = odd + even



#{ 
 # Driver Code Starts
# Initial Template for Python 3


def main():
    T = int(input())
    while T > 0:
        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        ob.sortIt(arr)
        print(*arr)
        print("~")
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends