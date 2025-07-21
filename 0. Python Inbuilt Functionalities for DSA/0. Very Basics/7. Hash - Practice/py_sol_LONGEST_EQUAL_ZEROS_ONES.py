def longest_equal_zeros_ones(arr):
    mp = {0: -1}
    max_len = 0
    count = 0
    
    for i in range(len(arr)):
        count += -1 if arr[i] == 0 else 1
        if count in mp:
            max_len = max(max_len, i - mp[count])
        else:
            mp[count] = i
    return max_len

print(longest_equal_zeros_ones([0, 1, 0, 1, 0, 1]))  # Output: 6
print(longest_equal_zeros_ones([0, 1, 0, 1, 1, 0]))  # Output: 4