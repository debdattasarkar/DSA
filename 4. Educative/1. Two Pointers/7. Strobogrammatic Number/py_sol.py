# Function to check if a number is strobogrammatic
def is_strobogrammatic(num):
    # Dictionary to map digits to their corresponding rotations
    dict = {'0': '0', '1': '1', '8': '8', '6': '9', '9': '6'}
    # Initialize pointers for the two ends of the string
    left = 0 
    right = len(num) - 1
    
    # Iterate while the left pointer is less than or equal to the right pointer
    while left <= right:
        # Check if the current digit is valid and matches its corresponding rotated value
        if num[left] not in dict or dict[num[left]] != num[right]:
            return False  # Return False if the number is not strobogrammatic
        # Move pointers towards the center
        left += 1
        right -= 1
    
    return True  # Return True if all digit pairs are valid

# Driver code
def main():
    nums = [
        "609",   
        "88",   
        "962",  
        "101",  
        "123"   
    ]

    i = 0  
    for num in nums:
        print(i + 1, ".\tnum: ", num, sep="")
        print("\n\tIs strobogrammatic: ", is_strobogrammatic(num), sep="")
        print("-" * 100)
        i += 1

if __name__ == "__main__":
    main()