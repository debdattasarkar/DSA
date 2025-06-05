def is_sorted(arr):
    for i in range(1, len(arr)):
         if arr[i] < arr[i - 1]:
              return False
    return True
    
print(is_sorted([1, 2, 2, 4, 5]))  # True
print(is_sorted([5, 4, 3]))        # False