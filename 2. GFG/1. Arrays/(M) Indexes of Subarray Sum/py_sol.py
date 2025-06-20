def findSubarrayWithSum(arr, target):
    start = 0
    current_sum = 0

    for end in range(len(arr)):
        current_sum += arr[end]

        # Shrink the window as long as current_sum > target
        while current_sum > target and start <= end:
            current_sum -= arr[start]
            start += 1

        # Check if we found the target sum
        if current_sum == target:
            return [start + 1, end + 1]  # Convert to 1-based indexing

    return [-1]

arr = [1, 2, 3, 7, 5]
target = 12
print(findSubarrayWithSum(arr, target))  # Output: [2, 4]