#User function Template for python3
from collections import Counter

class Solution:
    def allPairs(self, x, A, B):
        # Your code goes here 
        b_count = Counter(B)  # Count frequency of elements in B
        res = []

        for a in A:
            target = x - a
            if target in b_count:
                for _ in range(b_count[target]):
                    res.append((a, target))  # Add all matching pairs

        res.sort()  # Sort based on first element
        return res



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while (T > 0):
        x = int(input())
        arr1 = [int(x) for x in input().strip().split()]
        arr2 = [int(x) for x in input().strip().split()]
        ob = Solution()
        answer = ob.allPairs(x, arr1, arr2)
        sz = len(answer)

        if sz == 0:
            print(-1)

        else:

            for i in range(sz):
                if i == sz - 1:
                    print(*answer[i])
                else:
                    print(*answer[i], end=', ')

        T -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends