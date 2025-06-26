def three_sum(nums):
    nums.sort()
    result = []
    n = len(nums)

    for i in range(n - 2):
        if nums[i] > 0:
            break
        
        if i == 0 or nums[i] != nums[i - 1]:
            low, high = i + 1, n - 1
            
            while low < high:
                sum = nums[i] + nums[low] + nums[high]
                
                if sum < 0:
                    low += 1
                elif sum > 0:
                    high -= 1
                else:
                    result.append([nums[i], nums[low], nums[high]])
                    
                    low += 1
                    high -= 1
                    while low < high and nums[low] == nums[low - 1]:
                        low += 1
                    while low < high and nums[high] == nums[high + 1]:
                        high -= 1
    
    return result

# Driver code
def main():
    nums_arrs = [
        [-1, 0, 1, 2, -1, -4],
        [1, 2, 3, 4, 5],
        [0, 0, 0, 0],
        [-4, -1, -1, 0, 1, 2, 2],
        [-10, -7, -3, -1, 0, 3, 7, 10],
        [-3, -5, -7, -9]
    ]

    for i, nums in enumerate(nums_arrs):
        print(f"{i + 1}.\tnums: [{', '.join(map(str, nums))}]\n")
        print(f"\tTriplets: {three_sum(nums)}")
        print('-' * 100)

if __name__ == "__main__":
    main()