def count_pairs(nums, target):
    # Sort the array to enable the two-pointer approach
    nums.sort()
    count = 0  # Initialize the count of valid pairs
    low, high = 0, len(nums) - 1  # Initialize two pointers

    # Loop until the two pointers meet
    while low < high:
        # Check if the sum of the current pair is less than the target
        if nums[low] + nums[high] < target:
            # All pairs between low and high are valid
            count += high - low
            # Move the low pointer to explore more pairs
            low += 1
        else:
            # If the sum is not less than the target, move the high pointer
            high -= 1
    
    # Return the total count of pairs
    return count


def main():
    test_cases = [
        ([10, 1, 6, 2, 3, 8], 9),  
        ([1, 3, 5, 7], 8),      
        ([1, 2, 3, 6], 6),      
        ([2, 4, 6, 8, 10], 12), 
        ([5, 1, 9, 2], 10)      
    ]
    
    for i, (nums, target) in enumerate(test_cases):
        print(i+1, "\tnums:", nums)
        print("\ttarget:", target)
        result = count_pairs(nums, target)
        print("\n\tNumber of valid pairs:", result)
        print("-"*100)

if __name__ == "__main__":
    main()