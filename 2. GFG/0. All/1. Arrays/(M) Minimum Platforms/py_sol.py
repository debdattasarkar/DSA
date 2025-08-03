#User function Template for python3

class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,arr,dep):
        # code here
        n = len(arr)
        arr.sort()
        dep.sort()

        platform_needed = 0
        max_platforms = 0
        i = j = 0

        # Process all events in sorted order
        while i < n and j < n:
            if arr[i] <= dep[j]:
                platform_needed += 1
                i += 1
            else:
                platform_needed -= 1
                j += 1
            max_platforms = max(max_platforms, platform_needed)

        return max_platforms