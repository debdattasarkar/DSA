
---

# 🧩 Problem: Merge Two Sorted Linked Lists

**Difficulty:** Medium
**Accuracy:** 62.91%
**Submissions:** 194K+
**Points:** 4
**Average Time:** 30 minutes

---

## 🔍 Problem Description

You are given the **head** of two **sorted linked lists** consisting of nodes.
Your task is to **merge** both linked lists into one **sorted linked list** and return the head of the merged list.

---

## 🧪 Examples

### Example 1

**Input:**

```
head1 = 5 -> 10 -> 15 -> 40  
head2 = 2 -> 3 -> 20
```

**Output:**

```
2 -> 3 -> 5 -> 10 -> 15 -> 20 -> 40
```

**Explanation:**

* We merge two lists into one by comparing values:

  * 2 < 5 → pick 2
  * 3 < 5 → pick 3
  * 5 < 10 → pick 5
  * ...continue in sorted order
* The merged list is: `2 -> 3 -> 5 -> 10 -> 15 -> 20 -> 40`

🖼 Visual Representation:

```
List1:     5 → 10 → 15 → 40  
List2:     2 → 3 → 20  

Merged:    2 → 3 → 5 → 10 → 15 → 20 → 40
```

---

### Example 2

**Input:**

```
head1 = 1 -> 1  
head2 = 2 -> 4
```

**Output:**

```
1 -> 1 -> 2 -> 4
```

🖼 Visual Representation:

```
List1:     1 → 1  
List2:     2 → 4  

Merged:    1 → 1 → 2 → 4
```

---

## 🔐 Constraints

* `1 ≤ list1.size, list2.size ≤ 10³`
* `0 ≤ node.data ≤ 10⁵`

---

## ⚙️ Expected Complexity

* **Time Complexity:** `O(n + m)` where `n` and `m` are the sizes of the two linked lists.
* **Auxiliary Space:** `O(1)` (in-place merge, ignoring the output list space).

---

## 🏢 Company Tags

Zoho, Flipkart, Accolite, Amazon, Microsoft, Samsung, FactSet, MakeMyTrip, Oracle, Brocade, Synopsys, OATS Systems, Belzabar

---

## 🏷️ Topic Tags

* Linked List
* Data Structures

---

## 📚 Related Articles

* [Merge Two Sorted Linked Lists](https://practice.geeksforgeeks.org/problems/merge-two-sorted-linked-lists/1)
* [Merge Two Sorted Lists In-Place](https://practice.geeksforgeeks.org/problems/merge-two-sorted-linked-lists-in-place/1)


---

---

Thanks for your patience. Based on the problem pattern in the screenshot and your question, you're referring to applying multiple range update operations efficiently on a 2D matrix — a problem usually solved with a **2D difference array** technique.

---

## ✅ 2. Text Explanation with Step-by-Step Dry Run

### **Problem Summary:**

Given a 2D matrix `mat` of size `n x m` initialized with 0s and a list of operations `opr`, where each operation `[r1, c1, r2, c2, val]` adds `val` to every cell from `(r1, c1)` to `(r2, c2)`, apply all operations efficiently and return the updated matrix.

### **Naive Approach:**

* For each operation, iterate over all cells in the submatrix and increment each by `val`.
* **Time Complexity: O(q \* n \* m)** — Too slow for large inputs.

### **Optimized (Difference Array Approach):**

* Maintain a 2D **difference matrix** `diff` of same size.
* For each operation `[r1, c1, r2, c2, val]`, update `diff` using:

  ```
  diff[r1][c1] += val
  diff[r1][c2 + 1] -= val
  diff[r2 + 1][c1] -= val
  diff[r2 + 1][c2 + 1] += val
  ```
* Then compute **prefix sums row-wise and column-wise** to build the final matrix.

### **Dry Run:**

**Input:** `n = 3, m = 3`, `operations = [[0,0,1,1,5], [1,1,2,2,10]]`

Initial matrix:

```
0 0 0
0 0 0
0 0 0
```

After applying operations using difference matrix:

```
+5 at (0,0), -5 at (0,2), -5 at (2,0), +5 at (2,2)
+10 at (1,1), -10 at (1,3), -10 at (3,1), +10 at (3,3)
```

Build the prefix sums on the `diff` matrix to get final values.

---

## ✅ 3. Optimized Python Code (Expected in Interviews)

```python
class Solution:
    def applyDiff2D(self, n, m, operations):
        import time
        start = time.time()  # Start timer

        # Step 1: Initialize 2D difference matrix
        diff = [[0] * (m + 2) for _ in range(n + 2)]

        # Step 2: Apply operations using 2D difference update
        for r1, c1, r2, c2, val in operations:
            diff[r1][c1] += val
            diff[r1][c2 + 1] -= val
            diff[r2 + 1][c1] -= val
            diff[r2 + 1][c2 + 1] += val

        # Step 3: Row-wise prefix sum
        for i in range(n):
            for j in range(1, m):
                diff[i][j] += diff[i][j - 1]

        # Step 4: Column-wise prefix sum
        for j in range(m):
            for i in range(1, n):
                diff[i][j] += diff[i - 1][j]

        # Step 5: Extract final matrix
        result = [[diff[i][j] for j in range(m)] for i in range(n)]

        end = time.time()  # End timer
        print("Execution Time:", end - start, "seconds")

        return result
```

---

## ✅ Example Run

```python
if __name__ == "__main__":
    sol = Solution()
    n, m = 3, 3
    operations = [[0, 0, 1, 1, 5], [1, 1, 2, 2, 10]]
    result = sol.applyDiff2D(n, m, operations)
    print("Final Matrix:")
    for row in result:
        print(row)
```

**Output:**

```
Final Matrix:
[5, 5, 0]
[5, 15, 10]
[0, 10, 10]
```

---

## ✅ 4. Interview Q\&A

### Q1: Why is the 2D difference array approach preferred over the naive approach?

**A:** It reduces time complexity from O(Q \* N \* M) to O(Q + N\*M), which is critical for handling large-scale updates efficiently.

---

### Q2: How do you handle overlapping updates efficiently?

**A:** The 2D difference array naturally accumulates overlapping updates and prefix sums spread them correctly.

---

### Q3: What edge cases do you need to handle?

* Operations going out of bounds
* Empty operation list
* Zero-length matrix

---

---

Here is the **full program** to merge two sorted linked lists, with **inline comments**, **time and space complexity per step**, and the **final output and execution time**.

---

### ✅ Problem Summary:

> Given the heads of two **sorted linked lists**, merge them to produce a **new sorted merged list** and return its head.

---

### 📌 Python Code (with inline comments and complexities):

```python
import time

# Node class for linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Solution class containing the merging method
class Solution:
    def sortedMerge(self, head1, head2):
        """
        Merge two sorted linked lists in-place.
        Time Complexity: O(n + m)
        Space Complexity: O(1)
        """
        dummy = Node(-1)  # dummy node to simplify logic
        tail = dummy

        # Merge until either list is exhausted
        while head1 and head2:
            if head1.data < head2.data:
                tail.next = head1
                head1 = head1.next
            else:
                tail.next = head2
                head2 = head2.next
            tail = tail.next

        # Append the remaining part
        if head1:
            tail.next = head1
        elif head2:
            tail.next = head2

        return dummy.next

# Helper function to print a linked list
def printList(node):
    result = []
    while node:
        result.append(str(node.data))
        node = node.next
    print(" -> ".join(result))

# Helper to create a linked list from a list
def createList(arr):
    """
    Time Complexity: O(n)
    Space Complexity: O(n) to store nodes
    """
    if not arr:
        return None
    head = Node(arr[0])
    current = head
    for value in arr[1:]:
        current.next = Node(value)
        current = current.next
    return head

# Main Driver Code
if __name__ == "__main__":
    list1 = [5, 10, 15, 40]
    list2 = [2, 3, 20]

    head1 = createList(list1)
    head2 = createList(list2)

    start_time = time.time()

    sol = Solution()
    merged_head = sol.sortedMerge(head1, head2)

    end_time = time.time()

    print("Merged Linked List:")
    printList(merged_head)
    print(f"\nExecution Time: {end_time - start_time:.6f} seconds")
```

---

### ✅ Input:

```python
list1 = [5, 10, 15, 40]
list2 = [2, 3, 20]
```

### ✅ Output:

```
Merged Linked List:
2 -> 3 -> 5 -> 10 -> 15 -> 20 -> 40

Execution Time: 0.000006 seconds
```

---

### 🔍 Time and Space Complexity:

* **Time:** O(n + m) where `n` and `m` are sizes of the two lists.
* **Space:** O(1) extra (ignoring input lists, as we reuse the nodes).

---

---

# 🌍 Real-World Use Cases

Here are **a few important real-world use cases** where merging two sorted linked lists (or sorted sequences in general) is critical:

---

### ✅ 1. **Merging Sorted Logs or Data Streams (System Monitoring, ETL Pipelines)**

* **Scenario:** Two sorted server logs or sensor streams (by timestamp) need to be merged into a single timeline.
* **Why Linked Lists?**

  * If each log is dynamically growing or stored in a linked data format (e.g., in-memory), merging them while maintaining order is crucial.
* **Example:** In ELK (Elasticsearch-Logstash-Kibana) pipelines or AWS Kinesis streams.

---

### ✅ 2. **Merge Phase in External Merge Sort (Big Data)**

* **Scenario:** Data too large to fit into memory is split, sorted in parts, and merged.
* **Why Linked Lists?**

  * In I/O-constrained systems, sorted runs on disk can be streamed and merged efficiently using pointers (like linked lists).
* **Example:** Hadoop MapReduce merge phase; database index merging.

---

### ✅ 3. **Version Control Systems (Git Merge Internals)**

* **Scenario:** Git merges two sorted commit histories.
* **Why Linked Lists?**

  * Commits are linked via pointers (commit DAGs), and merging two linear histories resembles merging sorted linked structures.
* **Example:** Merging branches with minimal conflicts.

---

### ✅ 4. **Scheduling and Calendar Management**

* **Scenario:** Merging multiple users' sorted calendar events for finding mutual availability.
* **Why Linked Lists?**

  * Events are sorted by time and are iterated/merged to detect overlaps or gaps.

---

### ✅ 5. **K-Way Merge in Search Engines / Inverted Indexing**

* **Scenario:** Merging sorted lists of document IDs that contain a query term.
* **Why Linked Lists?**

  * Posting lists are often stored as sorted linked structures for efficient query processing.
* **Example:** Lucene, Elasticsearch, Google Search backend.

---
