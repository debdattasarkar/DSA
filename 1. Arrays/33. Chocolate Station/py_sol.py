#User function Template for python3

class Solution:
    def getChocolateCost(self, arr, price):
        # code here
        total_cost = arr[0]  # Chocolates to reach station 1 initially
        balance = 0  # Geek starts with 0 chocolates

        # Traverse from station 1 to end
        for i in range(len(arr) - 1):
            diff = arr[i] - arr[i + 1]

            if diff < 0:
                need = -diff
                if balance >= need:
                    balance -= need
                else:
                    total_cost += (need - balance)
                    balance = 0
            else:
                balance += diff

        return total_cost * price
    


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    tc = int(input().strip())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        price = int(input().strip())
        ob = Solution()
        print(ob.getChocolateCost(arr, price))
        tc -= 1
        print("~")

# } Driver Code Ends