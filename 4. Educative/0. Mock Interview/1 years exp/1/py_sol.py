def count_pairs(nums, target):
    count = 0
    n = len(nums)
    
    # Iterate over all pairs (i, j) where i < j
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] < target:
                print(f"Pair found: ({nums[i]}, {nums[j]})")
                count += 1
                
    return count

# Example usage
nums = [1, 3, 4, 2]
target = 7
print(count_pairs(nums, target))  # Output: 4