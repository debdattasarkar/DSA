
---

### ✅ Full Program: Two Sum (Python)

```python
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Step 1: Create a hashmap (dictionary) to store number → index mapping
        index_map = {}  # key: number, value: index

        # Step 2: Iterate through the array
        for i, num in enumerate(nums):
            # Compute the required complement that would sum to the target
            complement = target - num

            # Step 3: Check if this complement was seen earlier in the hashmap
            if complement in index_map:
                # If yes, return the stored index of the complement and current index
                return [index_map[complement], i]

            # Step 4: If not found, store the current number and its index for future reference
            index_map[num] = i

        # Note: Per the problem, exactly one solution exists, so we never reach here
        return []
```

---

### 📌 Input & Output Example

#### Example 1:

```python
nums = [2, 7, 11, 15]
target = 9
# Output: [0, 1]
# Because nums[0] + nums[1] == 2 + 7 = 9
```

#### Example 2:

```python
nums = [3, 2, 4]
target = 6
# Output: [1, 2] → nums[1] + nums[2] = 2 + 4 = 6
```

---

### 🧮 Time & Space Complexity (Per Step)

| Step                                | Time Complexity | Space Complexity |
| ----------------------------------- | --------------- | ---------------- |
| Creating `index_map`                | O(1)            | O(n)             |
| Iterating through `nums`            | O(n)            | O(n)             |
| Hash lookup and insertion (each op) | O(1) average    | —                |
| **Total**                           | ✅ **O(n)**      | ✅ **O(n)**       |

* **n = len(nums)**
* Worst case, we store all numbers before finding the result

---

### ✅ Summary:

* **Approach**: Hash Map for constant-time lookups of complements
* **Best Use Case**: When you need to find pairs summing to a value **in one pass**
* **Guaranteed**: One and only one solution (per constraints)

---
