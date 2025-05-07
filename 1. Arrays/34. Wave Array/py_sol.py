from typing import List


class Solution:
    def convertToWave(self, arr : List[int]) -> None:
        # code here
        n = len(arr)
        # Traverse array in steps of 2
        for i in range(0, n - 1, 2):
            # Swap current element with the next
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
        



#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        arr = list(map(int, input().strip().split()))

        obj = Solution()
        obj.convertToWave(arr)
        IntArray().Print(arr)
        print("~")

# } Driver Code Ends