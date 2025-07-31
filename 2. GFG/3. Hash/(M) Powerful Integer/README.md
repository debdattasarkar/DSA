
---

# Powerful Integer

**Difficulty**: Medium
**Accuracy**: 51.91%
**Submissions**: 27K+
**Points**: 4

---

## 🧠 Problem Statement

You are given a 2D integer array `intervals[][]` of length `n`, where each `intervals[i] = [start, end]` represents a closed interval (i.e., all integers from `start` to `end`, inclusive). You are also given an integer `k`.

An integer is called **Powerful** if it appears in at least `k` intervals.

Return the **maximum Powerful Integer**.

### ❗Note:

If **no integer** occurs at least `k` times, return `-1`.

---

## 🧪 Examples

### Example 1

```
Input: 
n = 3 
intervals[][] = [[1, 3], [4, 6], [3, 4]] 
k = 2

Output: 
4

Explanation: 
Integers 3 and 4 appear in 2 intervals. The maximum is 4.
```

---

### Example 2

```
Input: 
n = 4 
intervals[][] = [[1, 4], [12, 45], [3, 8], [10, 12]] 
k = 3

Output: 
-1

Explanation: 
No integer appears in at least 3 intervals.
```

---

### Example 3

```
Input: 
n = 5 
intervals[][] = [[16, 21], [5, 8], [12, 17], [17, 29], [9, 24]] 
k = 3

Output: 
21

Explanation: 
Integers 16, 17, 18, 19, 20, and 21 appear in at least 3 intervals. The maximum is 21.
```

---

## 🔒 Constraints

* $1 \leq n \leq 10^5$
* $1 \leq \text{intervals}[i][0] \leq \text{intervals}[i][1] \leq 10^9$
* $1 \leq k \leq 10^5$

---

## 💡 Expected Time and Space Complexities

| Metric          | Value      |
| --------------- | ---------- |
| Time Complexity | O(n log n) |
| Auxiliary Space | O(n)       |

---

## 🏷️ Tags

* Hash
* Sorting
* Map
* Data Structures
* Algorithms

---

## 📚 Related Articles

* [Powerful Integers](https://www.geeksforgeeks.org/problems/powerful-integers/1)

---

---

Here is a comprehensive response based on the correct sweep-line based solution for the **Powerful Integer** problem.

---

## ✅ Problem Statement

You are given a 2D integer array `intervals[][]` of size `n`, where each `intervals[i] = [start, end]` represents a closed interval (inclusive).
You are also given an integer `k`.
An integer is called **Powerful** if it appears in **at least `k` intervals**.

Return the **maximum Powerful Integer**.

📌 If **no integer appears** in at least `k` intervals, return `-1`.

---

## ✅ Step-by-Step Explanation with Dry Run

### Example:

```python
intervals = [[16, 21], [5, 8], [12, 17], [17, 29], [9, 24]]
k = 3
```

We apply a **sweep line algorithm**:

### Step 1: Mark start and end of intervals:

We use a map `event_map` where:

* `event_map[start] += 1` (interval starts)
* `event_map[end + 1] -= 1` (interval ends after end)

👉 After processing:

```python
event_map = {
    5: +1,
    9: +1,
    12: +1,
    16: +1,
    17: +1,
    18: -1,   # 17+1
    21: +0,
    22: -1,   # 21+1
    25: -1,   # 24+1
    30: -1    # 29+1
}
```

### Step 2: Sort keys:

```python
points = sorted(event_map.keys())  
# → [5, 9, 12, 16, 17, 18, 22, 25, 30]
```

### Step 3: Traverse with running prefix sum:

We maintain a `count` of how many intervals are active at any point.

```python
Initialize: count = 0, answer = -1

Iterate i from 0 to len(points)-2:
    point = points[i]
    next_point = points[i+1]
    count += event_map[point]

    if count >= k:
        # all integers in range [point, next_point-1] are valid
        answer = max(answer, next_point - 1)
```

### Iteration View:

| Interval | Count | Valid Range    | Max Valid |
| -------- | ----- | -------------- | --------- |
| \[17,18) | 3     | 17             | 17        |
| \[18,22) | 3     | 18, 19, 20, 21 | 21 ✅      |

✅ Final Answer = `21`

---

## ✅ Python Code with Inline Comments

```python
from collections import defaultdict

class Solution:
    def powerfulInteger(self, intervals, k):
        events = defaultdict(int)

        # Marking +1 at start and -1 at end+1
        for start, end in intervals:
            events[start] += 1
            events[end + 1] -= 1

        # Sort the event points
        points = sorted(events.keys())
        count = 0
        ans = -1

        # Traverse each interval between points
        for i in range(len(points) - 1):
            point = points[i]
            next_point = points[i + 1]
            count += events[point]

            # If count ≥ k, entire range [point, next_point-1] is valid
            if count >= k:
                ans = max(ans, next_point - 1)

        return ans
```

### ✅ Time and Space Complexity

| Metric           | Complexity |
| ---------------- | ---------- |
| Time Complexity  | O(n log n) |
| Space Complexity | O(n)       |

---

## ✅ Expected Interview Questions and Answers

### Q1. Why do we use `end + 1` for marking end events?

**A:** Because we use the sweep line approach, where we apply changes between two points. `end + 1` helps us exclude the end from the active interval.

---

### Q2. Why is this more efficient than brute force?

**A:** Brute force checks each number in every interval (`O(N * range)`), which is slow. This algorithm reduces it to `O(n log n)` by only handling event boundaries.

---

### Q3. What data structure is used here?

**A:** We use a `defaultdict` to store event deltas and a sorted list of keys to simulate prefix sum of overlapping intervals.

---

### Q4. What if intervals are large (up to 10⁹)?

**A:** This method doesn’t iterate over every number in the interval. Instead, it only processes start and end events—making it scalable even for huge values.

---

## ✅ Real-World Use Cases (Why This Matters)

1. **Network Traffic Monitoring**: Find the peak time during which at least `k` devices are active simultaneously.
2. **Event Scheduling**: Determine the latest time when at least `k` events are happening concurrently.
3. **Sensor Coverage**: Identify the farthest location covered by at least `k` sensors.

---
