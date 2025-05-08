#User function Template for python3

class Solution:
    def reArrange(self, arr, N):
        # code here 
        even, odd = 0, 1
        while even < N and odd < N:
            if arr[even] % 2 == 0:
                even += 2
            elif arr[odd] % 2 == 1:
                odd += 2
            else:
                # swap if even index has odd and odd index has even
                arr[even], arr[odd] = arr[odd], arr[even]
                even += 2
                odd += 2

#{ 
 # Driver Code Starts
#Initial Template for Python 3


def check(arr, n):
    flag = 1
    c=d=0
    for i in range(n):
        if i%2==0:
            if arr[i]%2:
                flag = 0
                break
            else:
                c+=1
        else:
            if arr[i]%2==0:
                flag = 0
                break
            else:
                d+=1
    if c!=d:
        flag = 0
            
    return flag
        
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        ob.reArrange(arr,N)
        
        print(check(arr,N))

        print("~")
# } Driver Code Ends