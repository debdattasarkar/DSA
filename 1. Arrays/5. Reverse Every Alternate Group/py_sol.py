def reverseInAltGroups(arr, k):
    n = len(arr)
    flag = 1
    for i in range(0, n, k):
        left = i
        right = min(i + k - 1, n - 1)
        if flag % 2 != 0:
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
        flag += 1
    return arr

print(reverseInAltGroups([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)) # Output: [3, 2, 1, 4, 5, 6, 9, 8, 7]

