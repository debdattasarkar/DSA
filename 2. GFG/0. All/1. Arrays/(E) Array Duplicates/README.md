
---

# 🧩 Array Duplicates

**Difficulty**: Easy
**Accuracy**: 18.95%
**Submissions**: 823K+
**Points**: 2
**Average Time**: 20m

---

## 📝 Problem Statement

Given an array `arr` of integers, find all the elements that occur more than once in the array. If no element repeats, return an empty array.

---

## 📥 Examples

### Example 1:

```
Input:  arr[] = [2, 3, 1, 2, 3]
Output: [2, 3]
Explanation: 2 and 3 occur more than once in the given array.
```

### Example 2:

```
Input:  arr[] = [0, 3, 1, 2]
Output: []
Explanation: There is no repeating element in the array, so the output is empty.
```

### Example 3:

```
Input:  arr[] = [2]
Output: []
Explanation: There is single element in the array. Therefore output is empty.
```

---

## 📌 Constraints

* $1 \leq \text{arr.size()} \leq 10^6$
* $0 \leq \text{arr[i]} \leq 10^6$

---

## ⚙️ Expected Complexities

* **Time Complexity**: $O(n)$
* **Auxiliary Space**: $O(n)$

---

## 🏷️ Company Tags

* Paytm
* Zoho
* Flipkart
* Amazon
* D-E Shaw
* Qualcomm

---

## 🧠 Topic Tags

* Arrays
* Data Structures

---

## 💼 Related Interview Experiences

* One97 Interview Experience Set 3 Backend Node JS Developer

---

---

Here's a comprehensive explanation, dry run, and Python code (brute and optimized) for the **Array Duplicates** problem in interview-preferred format.

---

## 📘 Text Explanation

### Problem:

Given an array of integers, find all the elements that **occur more than once**.
If no elements repeat, return an **empty list**.

---

## 🧠 Step-by-Step Dry Run

### Input:

```
arr = [2, 3, 1, 2, 3]
```

### Step-by-Step (Using HashMap):

| Step | Element | Count Map          | Output  |
| ---- | ------- | ------------------ | ------- |
| 1    | 2       | {2: 1}             | \[]     |
| 2    | 3       | {2: 1, 3: 1}       | \[]     |
| 3    | 1       | {2: 1, 3: 1, 1: 1} | \[]     |
| 4    | 2       | {2: 2, 3: 1, 1: 1} | \[2]    |
| 5    | 3       | {2: 2, 3: 2, 1: 1} | \[2, 3] |

---

## ✅ Brute Force Python (Using HashMap)

```python
class Solution:
    def findDuplicates(self, arr):
        count = {}
        result = []

        # Count frequency of each element
        for num in arr:
            count[num] = count.get(num, 0) + 1

        # Collect elements that occur more than once
        for num, freq in count.items():
            if freq > 1:
                result.append(num)

        return sorted(result)
```

**Time Complexity**: `O(n log n)` due to sorting
**Space Complexity**: `O(n)`

---

## 🚀 Optimized Python (In-place for range-limited input)

If values are in the range `0 <= arr[i] < n`, we can mark duplicates using index manipulation.

```python
class Solution:
    def findDuplicates(self, arr):
        n = len(arr)
        result = []

        for i in range(n):
            idx = abs(arr[i])
            if arr[idx % n] >= n * 2:
                continue  # Already recorded
            elif arr[idx % n] >= n:
                result.append(idx % n)  # Duplicate found
                arr[idx % n] += n       # Mark as fully recorded
            else:
                arr[idx % n] += n        # Mark as seen once

        return sorted(result)
```

**Time Complexity**: `O(n)`
**Space Complexity**: `O(1)` (in-place)
**Constraints**: Only works if `arr[i] < len(arr)` for all `i`

---

## ❓ Expected Interview Questions and Answers

### Q1: How did you decide on your approach?

**A**: I first used a frequency map (hash table) to count occurrences. It's the most direct way to track duplicates with linear time and space. If constraints allow, I also considered using index marking for in-place detection.

---

### Q2: Can you do it without extra space?

**A**: Yes, if the array has elements within a known range (like 0 to n-1), we can use index-based tricks by modifying the array in-place to track frequency indirectly.

---

### Q3: How would your solution behave if the input array is sorted?

**A**: A sorted array enables an O(n) scan with a simple comparison between adjacent elements to find duplicates.

```python
class Solution:
    def findDuplicates(self, arr):
        arr.sort()
        result = []
        for i in range(1, len(arr)):
            if arr[i] == arr[i-1] and (not result or result[-1] != arr[i]):
                result.append(arr[i])
        return result
```

---

### Q4: What if the array size is huge (close to 10⁶)? What would you optimize?

**A**: I would avoid sorting due to its `O(n log n)` complexity and prefer the frequency map or index-based solution to stay within `O(n)` time and constant space (if values are constrained).

---

---


```python
def find_duplicate(nums):
    # Initialize the fast and slow pointers and make them point the first
    # element of the array
    fast = slow = nums[0]
    # PART #1
    # Traverse in array until the intersection point is found
    while True:
        # Move the slow pointer using the nums[slow] flow
        slow = nums[slow]
        # Move the fast pointer two times fast as the slow pointer using the 
        # nums[nums[fast]] flow 
        fast = nums[nums[fast]]
        # Break the loop when slow pointer becomes equal to the fast pointer, i.e., 
        # if the intersection is found
        if slow == fast:
            break
    # PART #2
    # Make the slow pointer point the starting position of an array again, i.e.,
    # start the slow pointer from starting position
    slow = nums[0]
    # Traverse in the array until the slow pointer becomes equal to the
    # fast pointer
    while slow != fast:
        # Move the slow pointer using the nums[slow] flow
        slow = nums[slow]
        # Move the fast pointer slower than before, i.e., move the fast pointer
        # using the nums[fast] flow
        fast = nums[fast]
    # Return the fast pointer as it points the duplicate number of the array
    return fast

# Driver code
def main():
    nums = [
        [1, 3, 2, 3, 5, 4], 
        [2, 4, 5, 4, 1, 3], 
        [1, 6, 3, 5, 1, 2, 7, 4], 
        [1, 2, 2, 4, 3], 
        [3, 1, 3, 5, 6, 4, 2]
    ]
    for i in range(len(nums)):
        print(i + 1, ".\tnums = ", nums[i], sep="")
        print("\tDuplicate number = ", find_duplicate(nums[i]), sep="")
        print("-" * 100)


if __name__ == '__main__':
    main()

```

Great question!

The program you posted is an elegant and optimized solution to **"Find the Duplicate Number"** problem using **Floyd’s Tortoise and Hare Cycle Detection Algorithm**. It is **different** from the "Array Duplicates" problem (which finds *all* repeating elements). This version **finds exactly one duplicate**, assuming some specific constraints.

---

## ✅ Problem Type This Solves

> Given an array `nums` containing `n + 1` integers where each integer is in the range `[1, n]` inclusive, prove that at least one duplicate number must exist. Assume **only one duplicate** exists but it may appear multiple times.

---

## 📌 Key Assumptions for Floyd’s Algorithm to Work:

* Array length = `n + 1`
* Values range from `1` to `n`
* There is **exactly one number that repeats**, possibly multiple times
* The input array can be interpreted as a **linked list with a cycle**

---

## 🧠 Why This Works

This approach **models the array as a cycle**:

* Treat each index as a node.
* Value at each index `i` is a pointer to the next node: `i → nums[i]`.
* Since there are more nodes than unique values, there will be a **cycle** (by the pigeonhole principle).
* The **duplicate number is the cycle entrance**.

---

## 🔁 Dry Run Example:

### Input: `[1, 3, 2, 3, 5, 4]`

```
Index:    0  1  2  3  4  5
Value:    1  3  2  3  5  4

Start:
slow = nums[0] = 1
fast = nums[0] = 1

Iterating:
slow = nums[1] = 3
fast = nums[nums[1]] = nums[3] = 3

Intersection found at index 3 (value 3)
Now move slow = nums[0] = 1, fast stays at 3

slow = nums[1] = 3
fast = nums[3] = 3

Found duplicate: 3
```

---

Your implementation is **perfectly valid and clean** for the **“find all duplicates in an array”** problem. It’s interview-friendly, especially for Python-based roles.

Let’s break it down with an analysis.

---

## ✅ Code You Provided (HashMap + Sorted Output)

```python
class Solution:
    def findDuplicates(self, arr):
        freq = {}     # Dictionary to count frequency
        res = []      # Result list

        # Step 1: Count frequency of each number
        for num in arr:
            freq[num] = freq.get(num, 0) + 1

        # Step 2: Collect duplicates in sorted order
        for num in sorted(freq):
            if freq[num] > 1:
                res.append(num)

        return res
```

---

## 🧠 How It Works

1. **Frequency Counting** using dictionary (`O(n)`):

   * Key = number, value = count

2. **Sorting Keys** (`O(k log k)`) where `k = number of unique elements`

3. **Appending Duplicates** to result:

   * Only `freq[num] > 1` entries are included.

---

## ⏱️ Time and Space Complexity

| Aspect         | Complexity                                                    |
| -------------- | ------------------------------------------------------------- |
| Time           | `O(n + k log k)` <br> (`n = len(arr)`, \`k = unique elements) |
| Space          | `O(k)`                                                        |
| Sorted Output? | ✅ Yes                                                         |
| Stable?        | ✅ Yes (Predictable order)                                     |

---

## 📌 Input → Output Example

```python
Input:  [4, 2, 7, 2, 5, 7, 4]
freq:  {4: 2, 2: 2, 7: 2, 5: 1}
sorted(freq): [2, 4, 5, 7]
Duplicates: [2, 4, 7]
```

---

## 🔎 Comparison to Other HashMap Versions

| Version                 | Sorted Output | Space | Performance                             |
| ----------------------- | ------------- | ----- | --------------------------------------- |
| Yours (with `sorted()`) | ✅ Yes         | O(n)  | Slightly more work due to sorting       |
| Basic set/seen method   | ❌ No          | O(n)  | Slightly faster if order doesn’t matter |

---

## ✅ Interview-Friendly Tips

**Pros:**

* Shows clear intent (`freq.get(num, 0) + 1` is Pythonic).
* Uses `sorted()` to make output deterministic.
* Doesn’t mutate input array.

**Improvements (if interviewer asks):**

* If order doesn't matter, you can skip `sorted()` for performance.
* You can use `collections.Counter` for cleaner frequency counting:

  ```python
  from collections import Counter
  freq = Counter(arr)
  ```

---

Let me know if you want to see this rewritten using `Counter`, or want a version where **no sorting is used**, or output is in **input order**.


---

## ✅ Python Code Analysis

```python
def find_duplicate(nums):
    slow = fast = nums[0]

    # Phase 1: Detect the cycle
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    # Phase 2: Find the entrance to the cycle
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return fast
```

---

## ⏱️ Time and Space Complexity

* **Time**: `O(n)`
* **Space**: `O(1)` (no extra memory)

---

## 🚫 When This Approach Fails

This algorithm **doesn't work** for:

* Finding **all duplicates**
* Arrays where elements are **not guaranteed** to be from 1 to n
* Arrays with **more than one distinct duplicate**

For example:

```python
[2, 3, 1, 2, 3]  # Has two duplicates (2 and 3) → Floyd's won't work
```

---

## 🗣️ Interview Q\&A Based on This:

### Q1: How does this approach avoid using extra space?

**A**: It reuses the structure of the array as a virtual linked list and does not store any additional frequency or seen set.

---

### Q2: How is this different from HashMap-based duplicate detection?

**A**: HashMap tracks frequency and uses O(n) space. This uses constant space and is based on cycle detection.

---

### Q3: What if multiple duplicates exist?

**A**: This solution fails if more than one duplicate exists. It's strictly for **one duplicate**.

---

### Q4: Can this be modified to detect all duplicates?

**A**: No, because it only finds one cycle. To find all duplicates, we need counting, sorting, or marking techniques.

---

Would you like a comparison table of all techniques (Floyd’s, HashMap, Sorting, Frequency Array)?

Here’s a detailed **comparison table** of different techniques for detecting duplicates in arrays — including **Floyd's Cycle Detection**, **HashMap**, **Sorting**, and **Frequency Array (Counting)** approaches.

---

## 🔍 Duplicate Detection Approaches Comparison

| Technique                    | Duplicate Type     | Time Complexity | Space Complexity | Modifies Array? | Handles Multiple Duplicates | Assumptions Required                                 |
| ---------------------------- | ------------------ | --------------- | ---------------- | --------------- | --------------------------- | ---------------------------------------------------- |
| **Floyd’s Cycle Detection**  | One duplicate only | O(n)            | O(1)             | No              | ❌ No                        | Array of `n+1` elements with values `1` to `n`       |
| **HashMap / HashSet**        | Any number         | O(n)            | O(n)             | No              | ✅ Yes                       | None                                                 |
| **Sorting**                  | Any number         | O(n log n)      | O(1) or O(n)     | Yes             | ✅ Yes                       | Must allow modification or copy                      |
| **Frequency Array**          | Any number         | O(n)            | O(max(arr\[i]))  | No              | ✅ Yes                       | Values must be in a known, small range (e.g., ≤ 10⁶) |
| **Index Marking (in-place)** | Any number         | O(n)            | O(1)             | ✅ Yes           | ✅ Yes (only once per value) | Values in range `0 to n-1` or `1 to n`               |

---

## 📝 Summary of Usage Scenarios

| Scenario                                   | Best Method                |
| ------------------------------------------ | -------------------------- |
| Only one duplicate in a cycle-based setup  | ✅ Floyd’s Cycle Detection  |
| Multiple duplicates, memory is available   | ✅ HashMap / HashSet        |
| Input must remain sorted / allow reuse     | ✅ Sorting                  |
| Values are small and bounded (like 0–10⁶)  | ✅ Frequency Array          |
| Space constraint, and modification allowed | ✅ Index Marking (in-place) |

---

## 🔧 Example Use Cases

### Use Case 1: `[1, 3, 2, 3, 4]`

* Floyd’s: ❌ Not valid input (more than one duplicate allowed)
* HashMap: ✅ Detects `3`
* Sorting: ✅ Detects `3`
* Frequency Array: ✅ Detects `3`
* Index Marking: ✅ Detects `3`

---

### Use Case 2: `[1, 4, 3, 2, 2]` (values from 1 to n)

* Floyd’s: ✅ Detects `2`
* HashMap: ✅ Detects `2`
* Others: ✅

---

Would you like real code examples side-by-side for these techniques on one input array?

---

Perfect! Let's take a common input array:

```python
arr = [1, 3, 4, 2, 2]
```

In this array, the number **2** is the duplicate.

---

## ✅ 1. Floyd’s Cycle Detection (Only one duplicate, values 1 to n)

```python
class Floyd:
    def findDuplicate(self, nums):
        slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow

print("Floyd’s:", Floyd().findDuplicate([1, 3, 4, 2, 2]))
```

✅ **Output:** `2`

---

## ✅ 2. HashMap (General case, all duplicates)

```python
class UsingHashMap:
    def findDuplicates(self, nums):
        seen = set()
        result = []
        for num in nums:
            if num in seen:
                result.append(num)
            else:
                seen.add(num)
        return list(set(result))

print("HashMap :", UsingHashMap().findDuplicates([1, 3, 4, 2, 2]))
```

✅ **Output:** `[2]`

---

## ✅ 3. Sorting (Modifies array)

```python
class UsingSorting:
    def findDuplicates(self, nums):
        nums.sort()
        result = []
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] and (not result or nums[i] != result[-1]):
                result.append(nums[i])
        return result

print("Sorting :", UsingSorting().findDuplicates([1, 3, 4, 2, 2]))
```

✅ **Output:** `[2]`

---

## ✅ 4. Frequency Array (if max value known, say ≤ 10⁶)

```python
class UsingFreqArray:
    def findDuplicates(self, nums):
        freq = [0] * (max(nums) + 1)
        result = []
        for num in nums:
            freq[num] += 1
            if freq[num] == 2:
                result.append(num)
        return result

print("FreqArr :", UsingFreqArray().findDuplicates([1, 3, 4, 2, 2]))
```

✅ **Output:** `[2]`

---

## ✅ 5. Index Marking (Values must be in range `1 to n`, modifies array)

```python
class IndexMarking:
    def findDuplicates(self, nums):
        result = []
        for num in nums:
            idx = abs(num)
            if nums[idx - 1] < 0:
                result.append(idx)
            else:
                nums[idx - 1] *= -1
        return result

print("Indexing:", IndexMarking().findDuplicates([1, 3, 4, 2, 2]))
```

✅ **Output:** `[2]`

---

## 📊 Output Summary

| Method          | Output |
| --------------- | ------ |
| Floyd’s         | 2      |
| HashMap         | \[2]   |
| Sorting         | \[2]   |
| Frequency Array | \[2]   |
| Index Marking   | \[2]   |

---

Let me know if you want the same comparison for an array with **multiple duplicates**, e.g. `[1, 3, 2, 2, 3, 4]`.

Great! Let's take the array:

```python
arr = [1, 3, 2, 2, 3, 4]
```

In this array:

* **2** and **3** appear more than once.

We'll now run all 5 techniques again and note where each one works or fails.

---

## ✅ 1. Floyd’s Cycle Detection (⚠️ Not for multiple duplicates)

```python
class Floyd:
    def findDuplicate(self, nums):
        slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow

try:
    print("Floyd’s:", Floyd().findDuplicate([1, 3, 2, 2, 3, 4]))
except Exception as e:
    print("Floyd’s: ❌ Invalid input for Floyd's (multiple duplicates)")
```

❌ **Fails or gives partial output** — Floyd's is only for **one duplicate**.

---

## ✅ 2. HashMap (Correct for any number of duplicates)

```python
class UsingHashMap:
    def findDuplicates(self, nums):
        seen = set()
        result = []
        for num in nums:
            if num in seen:
                result.append(num)
            else:
                seen.add(num)
        return list(set(result))

print("HashMap :", UsingHashMap().findDuplicates([1, 3, 2, 2, 3, 4]))
```

✅ **Output:** `[2, 3]`

---

## ✅ 3. Sorting (Works correctly)

```python
class UsingSorting:
    def findDuplicates(self, nums):
        nums.sort()
        result = []
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] and (not result or nums[i] != result[-1]):
                result.append(nums[i])
        return result

print("Sorting :", UsingSorting().findDuplicates([1, 3, 2, 2, 3, 4]))
```

✅ **Output:** `[2, 3]`

---

## ✅ 4. Frequency Array (Works if values are bounded)

```python
class UsingFreqArray:
    def findDuplicates(self, nums):
        freq = [0] * (max(nums) + 1)
        result = []
        for num in nums:
            freq[num] += 1
            if freq[num] == 2:
                result.append(num)
        return result

print("FreqArr :", UsingFreqArray().findDuplicates([1, 3, 2, 2, 3, 4]))
```

✅ **Output:** `[2, 3]`

---

## ✅ 5. Index Marking (In-place and correct)

```python
class IndexMarking:
    def findDuplicates(self, nums):
        result = []
        for num in nums:
            idx = abs(num)
            if nums[idx - 1] < 0:
                result.append(idx)
            else:
                nums[idx - 1] *= -1
        return result

print("Indexing:", IndexMarking().findDuplicates([1, 3, 2, 2, 3, 4]))
```

✅ **Output:** `[2, 3]`

---

## 📊 Output Summary for `[1, 3, 2, 2, 3, 4]`

| Method          | Output     | Notes                         |
| --------------- | ---------- | ----------------------------- |
| Floyd’s         | ❌ (Fails)  | Only works for one duplicate  |
| HashMap         | ✅ `[2, 3]` | Works for all cases           |
| Sorting         | ✅ `[2, 3]` | Works, modifies input         |
| Frequency Array | ✅ `[2, 3]` | Efficient if values are small |
| Index Marking   | ✅ `[2, 3]` | In-place, modifies array      |

---
