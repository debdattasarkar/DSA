
from typing import List


class Solution:
    def zigZag(self,arr : List[int]) -> None:
        # code here
        flag = True  # True means "<" relation expected
        for i in range(len(arr) - 1):
            if flag:
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
            else:
                if arr[i] < arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
            flag = not flag  # Toggle expectation
        
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

    def isZigzag(n: int, arr: List[int]) -> bool:
        f = 1

        for i in range(1, n):
            if f:
                if arr[i - 1] > arr[i]:
                    return False
            else:
                if arr[i - 1] < arr[i]:
                    return False
            f = f ^ 1

        return True

    t = int(input())
    for _ in range(t):

        arr = list(map(int, input().split()))
        n = len(arr)

        obj = Solution()
        obj.zigZag(arr)
        check = True
        check = isZigzag(n, arr)

        flag = False
        for i in range(n):
            if arr[i] == i % 2:
                flag = False
            else:
                flag = True
                break

        if not flag:
            print("false")
        else:
            if check:
                print("true")
            else:
                print("false")

        print("~")

# } Driver Code Ends