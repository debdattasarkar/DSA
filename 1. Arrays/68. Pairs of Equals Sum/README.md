Great — here's the enhanced version of your working Python code with detailed **inline comments**, and then equivalent implementations in **C++** and **JavaScript**, all preserving the same logic.

---

### ✅ Python Code with Inline Comments

```python
class Solution:
    def findPairs(self, arr): 
        # Dictionary to store frequency of pair sums
        sum_occurence = {}

        for i in range(len(arr)):
            # Remove the first element for this iteration
            val = arr.pop(0)

            # Iterate over the remaining elements
            for j in arr:
                pair_sum = val + j

                # Count the number of times this sum has occurred
                sum_occurence[pair_sum] = sum_occurence.get(pair_sum, 0) + 1

                # If any sum occurs more than once, it means two pairs exist with same sum
                if sum_occurence[pair_sum] == 2:
                    return True

        # If no matching pair sum found
        return False
```

---

### ✅ C++ Version with Comments

```cpp
class Solution {
  public:
    bool findPairs(vector<int>& arr) {
        unordered_map<int, int> sum_count;

        // Outer loop removes one element at a time
        while (!arr.empty()) {
            int val = arr.front();
            arr.erase(arr.begin());  // pop from front

            // Check with all other elements
            for (int num : arr) {
                int s = val + num;

                // Count the number of times this sum has occurred
                sum_count[s]++;

                // If sum already occurred once before, return true
                if (sum_count[s] == 2)
                    return true;
            }
        }
        return false;
    }
};
```

---

### ✅ JavaScript Version with Comments

```javascript
class Solution {
    findPairs(arr) {
        let sumMap = new Map();

        while (arr.length > 0) {
            // Remove the first element from array
            let val = arr.shift();

            // Check with all remaining elements
            for (let j = 0; j < arr.length; j++) {
                let sum = val + arr[j];

                // Count how many times the sum occurs
                sumMap.set(sum, (sumMap.get(sum) || 0) + 1);

                // If sum occurs second time, return true
                if (sumMap.get(sum) === 2) {
                    return true;
                }
            }
        }

        return false;
    }
}
```

---

