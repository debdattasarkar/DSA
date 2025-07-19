
---

# Min and Max in Array

**Difficulty:** Basic
**Accuracy:** 68.55%
**Submissions:** 358K+
**Points:** 1
**Average Time:** 10m

---

## 🧾 Problem Statement

Given an array `arr`, your task is to find the **minimum** and **maximum** elements in the array.

> **Note:** Return a pair that contains two elements — the first one will be the minimum element and the second will be the maximum.

---

## 📘 Examples

### Example 1:

```
Input: arr[] = [3, 2, 1, 56, 10000, 167]
Output: 1 10000
Explanation: Minimum and maximum elements of array are 1 and 10000.
```

### Example 2:

```
Input: arr[] = [1, 345, 234, 21, 56789]
Output: 1 56789
Explanation: Minimum and maximum elements of array are 1 and 56789.
```

### Example 3:

```
Input: arr[] = [56789]
Output: 56789 56789
Explanation: Since the array contains only one element, both min & max are the same.
```

---

## 📌 Constraints

* `1 <= arr.size() <= 10^5`
* `1 <= arr[i] <= 10^9`

---

## ✅ Expected Complexities

* **Time Complexity:** O(n)
* **Auxiliary Space:** O(1)

---

## 🏷️ Topic Tags

* Arrays
* Data Structures

---

## 📚 Related Articles

* Cpp Program To Find The Minimum And Maximum Element Of An Array
* Maximum And Minimum In An Array
* Min And Max In A List In Java

---

---

Sure! Below is the complete explanation and step-by-step dry run, followed by two Python implementations (brute force and optimized) using the format you requested.

---

## 🔍 2. Explanation and Step-by-Step Dry Run

### ✅ Goal

Find the **minimum** and **maximum** values in an integer array.

---

### 🔁 Naive Idea (Brute Force)

Loop twice:

* First loop to find the **min**
* Second loop to find the **max**

**Time Complexity:** O(2n) = O(n)
**Space Complexity:** O(1)

---

### ⚡ Optimized Idea

Traverse the array once:

* Initialize both `min_val` and `max_val` to the first element.
* For each element:

  * If it's less than `min_val`, update `min_val`.
  * If it's greater than `max_val`, update `max_val`.

**Time Complexity:** O(n)
**Space Complexity:** O(1)

---

### 🔁 Dry Run Example

```python
arr = [3, 2, 1, 56, 10000, 167]

Start:
  min_val = max_val = 3

i=1 → arr[1]=2:  min_val = 2 (since 2 < 3), max_val stays 3  
i=2 → arr[2]=1:  min_val = 1 (since 1 < 2), max_val stays 3  
i=3 → arr[3]=56: max_val = 56 (since 56 > 3), min_val stays 1  
i=4 → arr[4]=10000: max_val = 10000  
i=5 → arr[5]=167: no change

Final result: (1, 10000)
```

---

## 🧠 3. Python Code (Interview Format)

### ✅ Optimized Code

```python
class Solution:
    def get_min_max(self, arr):
        # Handle edge case: if array is empty
        if not arr:
            return None, None

        # Initialize min and max to the first element
        min_val = max_val = arr[0]

        # Traverse the array
        for num in arr[1:]:
            if num < min_val:
                min_val = num
            elif num > max_val:
                max_val = num

        return min_val, max_val
```

### 🧪 Test the function

```python
if __name__ == "__main__":
    sol = Solution()
    arr = [3, 2, 1, 56, 10000, 167]
    print("Input:", arr)
    min_val, max_val = sol.get_min_max(arr)
    print("Output:", min_val, max_val)
```

---

### 🐌 Brute Force Version

```python
class Solution:
    def get_min_max(self, arr):
        if not arr:
            return None, None

        min_val = min(arr)  # O(n)
        max_val = max(arr)  # O(n)

        return min_val, max_val
```

> This version uses Python built-ins, still O(n) time, but may be less favored in interviews due to lack of explicit logic.

---

## 💬 4. Expected Interview Q\&A

### Q1. Can you solve it without using Python built-ins?

**A:** Yes, by manually iterating and tracking `min_val` and `max_val`.

---

### Q2. What is the time and space complexity?

**A:**

* Time: O(n), as we visit each element once.
* Space: O(1), using only constant extra variables.

---

### Q3. Can you optimize the number of comparisons?

**A:** Yes, using **Tournament Method**, we can reduce comparisons from `2n` to about `3n/2`, but it’s more complex and usually not required unless mentioned.

---

### Q4. What happens if the array is empty?

**A:** We should return `(None, None)` or raise an exception depending on problem constraints.

---

---

### ✅ Full Python Program – Min and Max in Array

This implementation finds the minimum and maximum values in a given array using a single pass (O(n) time). It includes inline explanations for logic, time complexity, and space complexity, plus timing the execution.

---

### ✅ Code (with Time and Space Complexity Comments)

```python
import timeit

class Solution:
    def get_min_max(self, arr):
        # Time Complexity: O(n), where n is the number of elements in arr
        # Space Complexity: O(1), constant extra space used

        # Handle edge case: empty array
        if not arr:
            return None, None

        # Initialize both min and max with the first element
        min_val = max_val = arr[0]

        # Traverse the array from second element onward
        for num in arr[1:]:
            if num < min_val:
                min_val = num  # Update min if smaller value found
            elif num > max_val:
                max_val = num  # Update max if larger value found

        return min_val, max_val


# Test the implementation
def main():
    arr = [3, 2, 1, 56, 10000, 167]
    sol = Solution()
    result = sol.get_min_max(arr)
    print("Input:", arr)
    print("Output:", result)  # Expected Output: (1, 10000)

# Time the execution of the full program
execution_time = timeit.timeit(main, number=1)
print(f"\nExecution Time: {execution_time:.10f} seconds")
```

---

### 🧪 Sample Output

```
Input: [3, 2, 1, 56, 10000, 167]
Output: (1, 10000)

Execution Time: 0.0004994490 seconds
```

---

### 🔍 Step-by-Step Dry Run

For input `[3, 2, 1, 56, 10000, 167]`:

1. Start: `min_val = 3`, `max_val = 3`
2. Compare 2 → update `min_val = 2`
3. Compare 1 → update `min_val = 1`
4. Compare 56 → update `max_val = 56`
5. Compare 10000 → update `max_val = 10000`
6. Compare 167 → no change

Final result: `(min_val = 1, max_val = 10000)`

---

---

# 🌍 Real-World Use Cases

Here are a few **important real-world use cases** of finding the **minimum and maximum elements in an array**:

---

### ✅ 1. **Sensor Data Analysis (IoT, Weather, Health)**

* **Use Case**: In time-series data from sensors (e.g., temperature, heartbeat, air quality), you often need to know the **minimum and maximum readings** over a period.
* **Example**: Find the lowest and highest temperature of the week.

---

### ✅ 2. **Financial Analytics**

* **Use Case**: Analyzing **stock prices**, **sales trends**, or **currency fluctuations** where identifying daily/monthly highs and lows is essential.
* **Example**: Maximum price of a stock in the last 30 days to flag peaks.

---

### ✅ 3. **Image Processing**

* **Use Case**: In grayscale image processing, `min` and `max` pixel intensity values help in contrast enhancement and normalization.
* **Example**: Auto-adjusting brightness/contrast using histogram normalization.

---

### ✅ 4. **Database Query Optimization**

* **Use Case**: SQL-like operations (e.g., `SELECT MIN(value), MAX(value) FROM table`) are translated into memory-level array scanning when using in-memory DBs or dataframes (Pandas, NumPy).

---

### ✅ 5. **Machine Learning Preprocessing**

* **Use Case**: **Min-Max normalization** is widely used in feature scaling.
* **Example**: Transforming feature range from `[original_min, original_max]` → `[0, 1]` for better gradient descent performance.

---

