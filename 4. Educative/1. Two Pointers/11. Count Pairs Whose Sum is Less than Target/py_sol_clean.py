def count_pairs(nums, target):
    nums.sort()
    count = 0
    low, high = 0, len(nums) - 1

    while low < high:
        if nums[low] + nums[high] < target:
            count += high - low
            low += 1
        else:
            high -= 1
    
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