def circular_array_loop(nums):
    size = len(nums)
    # Iterate through each index of the array 'nums'.
    for i in range(size):
        # Set slow and fast pointer at current index value.
        slow = fast = i
      
        # Set true in 'forward' if element is positive, set false otherwise.
        forward = nums[i] > 0
      
        while True:
            # Move slow pointer to one step.
            slow = next_step(slow, nums[slow], size) 
            # If cycle is not possible, break the loop and start from next element.
            if is_not_cycle(nums, forward, slow):
                break
        
            # First move of fast pointer.
            fast = next_step(fast, nums[fast], size)
            # If cycle is not possible, break the loop and start from next element.
            if is_not_cycle(nums, forward, fast):
                break
            
            # Second move of fast pointer.
            fast = next_step(fast, nums[fast], size)
            # If cycle is not possible, break the loop and start from next element.
            if is_not_cycle(nums, forward, fast):
                break
        
            # At any point, if fast and slow pointers meet each other,
            # it indicate that loop has been found, return True.
            if slow == fast:
                return True
                
    return False

# A function to calculate the next step
def next_step(pointer, value, size):
    return (pointer + value) % size


# A function to detect a cycle doesn't exist
def is_not_cycle(nums, prev_direction, pointer):
    # Set current direction to True if current element is positive, set False otherwise.
    curr_direction = nums[pointer] >= 0
    
    # If current direction and previous direction is different or moving a pointer takes back to the same value,
    # then the cycle is not possible, we return True, otherwise return False.
    if (prev_direction != curr_direction) or (nums[pointer] % len(nums) == 0):
        return True
    else:
        return False

# Driver code
def main():

    input = (
            [-2, -3, -9],
            [-5, -4, -3, -2, -1],
            [-1, -2, -3, -4, -5],
            [2, 1, -1, -2],
            [-1, -2, -3, -4, -5, 6],
            [1, 2, -3, 3, 4, 7, 1],
            [2, 2, 2, 7, 2, -1, 2, -1, -1]
            )
    num = 1

    for i in input:
        print(f"{num}.\tCircular array = {i}")
        print(f"\n\tFound loop = {circular_array_loop(i)}")
        print("-"*100, "\n")
        num += 1


if __name__ == "__main__":
    main()