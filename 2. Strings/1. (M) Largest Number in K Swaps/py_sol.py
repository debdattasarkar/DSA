#User function Template for python3

class Solution:
    
    #Function to find the largest number after k swaps.
    def findMaximumNum(self, s, k):
        #code here
        self.max_num = s

        def helper(s_list, k, idx):
            if k == 0 or idx == len(s_list):
                return

            max_digit = max(s_list[idx:])

            if s_list[idx] != max_digit:
                for j in range(len(s_list)-1, idx-1, -1):
                    if s_list[j] == max_digit:
                        # Swap
                        s_list[idx], s_list[j] = s_list[j], s_list[idx]
                        curr_str = ''.join(s_list)

                        # Update max_num
                        if curr_str > self.max_num:
                            self.max_num = curr_str

                        # Recurse
                        helper(s_list, k - 1, idx + 1)

                        # Backtrack
                        s_list[idx], s_list[j] = s_list[j], s_list[idx]
            else:
                # Move to next index only if current is already max
                helper(s_list, k, idx + 1)

        helper(list(s), k, 0)
        return self.max_num



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        k = int(input())
        s = input()
        ob = Solution()
        print(ob.findMaximumNum(s, k))

        print("~")

# } Driver Code Ends