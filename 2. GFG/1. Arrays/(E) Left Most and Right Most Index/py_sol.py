#User function Template for python3

class Solution:
    def indexes(self, v, x):
        # Your code goes here
        def findFirst():
            low, high = 0, len(v) - 1
            first = -1
            while low <= high:
                mid = (low + high) // 2
                if v[mid] == x:
                    first = mid
                    high = mid - 1  # search left half
                elif v[mid] < x:
                    low = mid + 1
                else:
                    high = mid - 1
            return first

        def findLast():
            low, high = 0, len(v) - 1
            last = -1
            while low <= high:
                mid = (low + high) // 2
                if v[mid] == x:
                    last = mid
                    low = mid + 1  # search right half
                elif v[mid] < x:
                    low = mid + 1
                else:
                    high = mid - 1
            return last

        first = findFirst()
        last = findLast()
        return [first, last]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())
        obj = Solution()
        ans = obj.indexes(a, k)
        if ans[0]==-1 and ans[1]==-1:
            print(-1)
        else:
            print(ans[0], end=' ')
            print(ans[1])

        T -= 1


        print("~")
if __name__ == "__main__":
    main()


# } Driver Code Ends