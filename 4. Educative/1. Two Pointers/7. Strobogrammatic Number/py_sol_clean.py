# Function to check if a number is strobogrammatic
def is_strobogrammatic(num):
    dict = {'0': '0', '1': '1', '8': '8', '6': '9', '9': '6'}
    left = 0 
    right = len(num) - 1
    
    while left <= right:
        if num[left] not in dict or dict[num[left]] != num[right]:
            return False
        left += 1
        right -= 1
    return True

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