Let's break down **Window and Pointer Techniques**—two of the most widely used patterns in **DSA**, especially for array, string, and list-based problems.

---

## 🧰 1. **Sliding Window Technique**

### 📌 Idea:

Instead of recalculating values for every window from scratch, **slide a window** over the data structure and **reuse previous results**.

### 🔄 Use Case:

When you’re asked to find the **maximum/minimum/sum/count** of a subarray, substring, or window of size `k`.

### 🔧 Template (Fixed Window):

```python
def max_sum_subarray(arr, k):
    n = len(arr)
    max_sum = curr_sum = sum(arr[:k])
    
    for i in range(k, n):
        curr_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, curr_sum)
    
    return max_sum
```

### 📦 Common Problems:

* [Leetcode 3](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
* [Leetcode 76](https://leetcode.com/problems/minimum-window-substring/)
* GFG: First negative integer in every window of size k

---

## 🧰 2. **Two Pointer Technique**

### 📌 Idea:

Use **two pointers** (start & end) to scan data from either:

* Same side (to expand/shrink a window)
* Opposite ends (to close in on a condition)

### 🔄 Use Case:

When the problem asks you to:

* Check pairs (`arr[i] + arr[j] == target`)
* Shrink/expand a subrange
* Detect duplicates or partitions

### 🔧 Template (Opposite ends):

```python
def has_pair_with_sum(arr, target):
    arr.sort()
    left, right = 0, len(arr) - 1

    while left < right:
        total = arr[left] + arr[right]
        if total == target:
            return True
        elif total < target:
            left += 1
        else:
            right -= 1
    return False
```

### 🔧 Template (Same side):

```python
def longest_unique_substring(s):
    char_set = set()
    left = max_len = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)
    
    return max_len
```

---

## 🧠 When to Use What

| Scenario                                | Technique      |
| --------------------------------------- | -------------- |
| Substring/array of size k               | Sliding Window |
| Variable window size based on condition | Two Pointers   |
| Checking sum/pairs                      | Two Pointers   |
| Max/Min in moving range                 | Sliding Window |
| Repeating characters, distinct values   | Two Pointers   |

---

## 🧪 Would You Like to Practice:

* Problems based on **fixed-size** or **variable-size** windows?
* Classic problems like:

  * **Longest substring with k distinct characters**
  * **Min window substring**
  * **Container with most water**
  * **Two sum / 3Sum / 4Sum**
* Or Leetcode/GFG style quizzes?

---

---

The **Fast and Slow Pointers** technique (also known as **Tortoise and Hare**) is a powerful pattern commonly used in **linked lists**, **cycle detection**, and sometimes **array traversal**.

---

## 🐢🐇 Fast and Slow Pointers Technique

### 📌 Core Idea:

Use **two pointers** that move at **different speeds**—typically:

* **Slow pointer** moves 1 step
* **Fast pointer** moves 2 steps

By observing their relative positions, you can:

* Detect **cycles**
* Find **middle of list**
* Locate **cycle entry point**
* Compare **linked list halves**

---

## ✅ Common Use Cases

| Problem Type                           | Use Fast & Slow Pointers to...     |
| -------------------------------------- | ---------------------------------- |
| Cycle detection in linked list / graph | Detect if a cycle exists           |
| Find cycle starting point              | Locate where the cycle begins      |
| Find middle node of linked list        | Stop slow when fast reaches end    |
| Check if a linked list is palindrome   | Split in half, reverse, compare    |
| Detect happy number (Leetcode 202)     | Detect cycles in digit square sums |
| Floyd’s Cycle Detection Algorithm      | Classic textbook algorithm         |

---

## 🧑‍💻 Example 1: Detect Cycle in Linked List

```python
def hasCycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
    return False
```

### ✅ Time: `O(n)`

### ✅ Space: `O(1)`

---

## 🧑‍💻 Example 2: Find Start of Cycle (Floyd’s Algorithm)

```python
def detectCycle(head):
    slow = fast = head

    # Step 1: Detect if cycle exists
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None  # No cycle

    # Step 2: Find entry point
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow  # Start of cycle
```

---

## 🧪 Example 3: Find Middle of Linked List

```python
def findMiddle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow  # Middle node
```

---

## 🧠 Why It Works

* If a cycle exists, the fast pointer "laps" the slow pointer.
* If no cycle, fast pointer reaches `None` first.
* Resetting slow and moving both at same speed guarantees they'll meet at cycle start.

---

## 🧩 Interview Problems

| Problem Name                                    | Platform     |
| ----------------------------------------------- | ------------ |
| Linked List Cycle I and II                      | Leetcode     |
| Happy Number                                    | Leetcode 202 |
| Find Middle of Linked List                      | Leetcode 876 |
| Palindrome Linked List                          | Leetcode 234 |
| Detect Cycle in Directed Graph (with recursion) | GFG, custom  |

---

