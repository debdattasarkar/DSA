def longest_consecutive(nums):
    num_set = set(nums)
    longest = 0

    for num in nums:
        if num - 1 not in num_set:  # Start of sequence
            length = 1
            while num + length in num_set:
                length += 1
            longest = max(longest, length)
    
    return longest
print(longest_consecutive([100, 4, 200, 1, 3, 2]))  # Output: 4 (1, 2, 3, 4)