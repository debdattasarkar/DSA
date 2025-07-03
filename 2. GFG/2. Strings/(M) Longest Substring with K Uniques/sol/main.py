class Solution:
    def swapKth(self, arr, n, k):
        # 1-based indexing in the problem → convert to 0-based indices
        left_index = k - 1          # Kth element from start
        right_index = n - k         # Kth element from end

        # Edge case: if left_index and right_index are same, do nothing
        if left_index == right_index:
            return arr

        # Step: Swap the elements in-place
        arr[left_index], arr[right_index] = arr[right_index], arr[left_index]  # O(1)

        return arr  # Return is optional depending on interface

if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    arr1 = [1, 2, 3, 4, 5, 6, 7, 8]
    k1 = 3
    print("Original:", arr1)
    print(f"Swap {k1}th from start & end")
    result1 = sol.swapKth(arr1, len(arr1), k1)
    print("Modified:", result1)  # Expected: [1, 2, 6, 4, 5, 3, 7, 8]

    # Test Case 2 (middle element, no-op)
    arr2 = [1, 2, 3, 4, 5]
    k2 = 3
    print("\nOriginal:", arr2)
    print(f"Swap {k2}th from start & end")
    result2 = sol.swapKth(arr2, len(arr2), k2)
    print("Modified:", result2)  # Expected: [1, 2, 3, 4, 5]

    # Test Case 3 (first and last)
    arr3 = [10, 20, 30, 40]
    k3 = 1
    print("\nOriginal:", arr3)
    print(f"Swap {k3}th from start & end")
    result3 = sol.swapKth(arr3, len(arr3), k3)
    print("Modified:", result3)  # Expected: [40, 20, 30, 10]
