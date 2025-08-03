#User function Template for python3
class Solution:
    def countElements(self, a, b, n, query, q):
        # code here
        # Step 1: Find the maximum value in both arrays to size our frequency array
        max_val = max(max(a), max(b)) + 1
        
        # Step 2: Create frequency array for array `b`
        freq = [0] * (max_val + 1)
        for num in b:
            freq[num] += 1

        # Step 3: Create prefix sum array so that freq[i] holds count of elements <= i
        for i in range(1, len(freq)):
            freq[i] += freq[i - 1]

        # Step 4: Resolve queries using prefix array
        result = []
        for idx in query:
            value = a[idx]
            result.append(freq[value])

        return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    q = int(input())
    query = []
    ob = Solution()
    for i in range(q):
        query.append(int(input()))
    ans = ob.countElements(a, b, n, query, q)
    for i in range(q):
        print(ans[i])

    print("~")
# } Driver Code Ends