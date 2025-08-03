from collections import defaultdict
import time

class Solution:
    def countAtMostK(self, arr, k):
        freq = defaultdict(int)  # Dictionary to store frequency of elements in the current window
        left = 0                 # Left pointer for sliding window
        count = 0                # Result count

        for right in range(len(arr)):
            # Step 1: Add new element to window
            if freq[arr[right]] == 0:
                k -= 1  # New distinct element
            freq[arr[right]] += 1

            # Step 2: Shrink window from the left if we exceed k distinct elements
            while k < 0:
                freq[arr[left]] -= 1
                if freq[arr[left]] == 0:
                    k += 1  # One distinct element removed
                left += 1

            # Step 3: All subarrays ending at 'right' with valid 'left' are counted
            count += (right - left + 1)

        return count
    
if __name__ == "__main__":
    arr = [1, 2, 1, 2, 3]
    k = 2
    solution = Solution()
    
    start_time = time.time()
    result = solution.countAtMostK(arr, k)
    end_time = time.time()
    
    print(f"Number of subarrays with at most {k} distinct integers: {result}")
    print(f"Execution time: {end_time - start_time:.6f} seconds")