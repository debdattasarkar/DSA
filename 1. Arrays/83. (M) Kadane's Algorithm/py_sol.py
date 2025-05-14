def maxSubarraySum(arr):
    max_sum = curr_sum = arr[0]

    for num in arr[1:]:
        curr_sum = max(num, curr_sum + num)
        max_sum = max(max_sum, curr_sum)

    return max_sum

print(maxSubarraySum([2, 3, -8, 7, -1, 2, 3]))  # Output: 11
print(maxSubarraySum([-2, -4]))                # Output: -2
print(maxSubarraySum([5, 4, 1, 7, 8]))          # Output: 25