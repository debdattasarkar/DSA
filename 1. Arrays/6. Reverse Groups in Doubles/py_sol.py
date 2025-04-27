def reverseInDblsGroups(arr):
    n = len(arr)
    k = 1
    i = 0
    while i < n:
        left = i
        right = min(i + k - 1, n - 1)

        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

        i += k  # move to the next group
        k *= 2  # double the group size
    return arr

# Test
print(reverseInDblsGroups([1, 2, 3, 4, 5, 6, 7, 8, 9]))
# Output: [1, 3, 2, 7, 6, 5, 4, 9, 8]
