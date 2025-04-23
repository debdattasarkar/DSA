def secondLargest(arr):
    if len(arr) < 2:
        return -1

    largest = second = -1

    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num

    return second

print(secondLargest([12, 35, 1, 10, 34, 1]))  # Output: 34
print(secondLargest([10, 5, 10]))            # Output: 5
print(secondLargest([10, 10, 10]))           # Output: -1