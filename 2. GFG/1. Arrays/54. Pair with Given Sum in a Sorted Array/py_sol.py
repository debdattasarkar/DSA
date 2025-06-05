#User function Template for python3

class Solution:
    def countPairs (self, arr, target) : 
        #Complete the function
        left = 0
        right = len(arr) - 1
        count = 0
    
        while left < right:
            curr_sum = arr[left] + arr[right]
    
            if curr_sum == target:
                # If elements are different
                if arr[left] != arr[right]:
                    # Count duplicates on both ends
                    l_count = 1
                    r_count = 1
                    while left + 1 < right and arr[left] == arr[left + 1]:
                        l_count += 1
                        left += 1
                    while right - 1 > left and arr[right] == arr[right - 1]:
                        r_count += 1
                        right -= 1
                    count += l_count * r_count
                    left += 1
                    right -= 1
                else:
                    # All elements between left and right are the same
                    n = right - left + 1
                    count += (n * (n - 1)) // 2
                    break
            elif curr_sum < target:
                left += 1
            else:
                right -= 1
    
        return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    import sys
    input = sys.stdin.read
    data = input().split('\n')

    t = int(data[0].strip())
    index = 1

    for _ in range(t):
        arr = list(map(int, data[index].strip().split()))
        index += 1
        target = int(data[index].strip())
        index += 1

        res = Solution().countPairs(arr, target)
        print(res)
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends