class Solution:

    def segregateEvenOdd(self, arr):
        n = len(arr)

        # Step 1: Partition all even numbers to the front
        i = 0
        for j in range(n):
            if arr[j] % 2 == 0:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        # At this point:
        # arr[0:i] → all even numbers (unordered)
        # arr[i:n] → all odd numbers (unordered)

        # Step 2: Sort both parts in-place
        arr[:i] = sorted(arr[:i])   # sort even numbers
        arr[i:] = sorted(arr[i:])   # sort odd numbers

if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    arr1 = [12, 34, 45, 9, 8, 90, 3]
    print("Original:", arr1)
    sol.segregateEvenOdd(arr1)
    print("Modified:", arr1)  # Expected: [8, 12, 34, 90, 3, 9, 45]

    # Test case 2
    arr2 = [0, 1, 2, 3, 4]
    print("\nOriginal:", arr2)
    sol.segregateEvenOdd(arr2)
    print("Modified:", arr2)  # Expected: [0, 2, 4, 1, 3]

    # Test case 3
    arr3 = [10, 22, 4, 6]
    print("\nOriginal:", arr3)
    sol.segregateEvenOdd(arr3)
    print("Modified:", arr3)  # Expected: [4, 6, 10, 22]