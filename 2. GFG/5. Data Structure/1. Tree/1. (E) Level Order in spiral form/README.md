Here is the full README in Markdown format for the problem **"Level Order in Spiral Form"**, as seen in the uploaded image:

---

# Level Order in Spiral Form

## Introduction

The **Spiral (Zigzag) Level Order Traversal** of a binary tree is a variation of the traditional level-order traversal. The nodes are visited level by level, but the direction alternates at each level: from right-to-left on even levels and from left-to-right on odd levels (starting from level 0 for the root).

---

## Table of Contents

* [Introduction](#introduction)
* [Problem Statement](#problem-statement)
* [Examples](#examples)
* [Constraints](#constraints)
* [Expected Complexity](#expected-complexity)
* [Tags](#tags)

---

## Problem Statement

Given a binary tree, return the spiral (zigzag) order traversal of its nodes' values as a list.

### Spiral Order Traversal Definition:

* Level 0 (root level): right to left
* Level 1: left to right
* Level 2: right to left
* …and so on (alternating directions)

---

## Examples

### Example 1

```
Input: root = [1, 3, 2]

    1
   / \
  3   2

Output: [1, 3, 2]

Explanation:
Level 0 → right to left → [1]  
Level 1 → left to right → [3, 2]
```

---

### Example 2

```
Input: root = [10, 20, 30, 40, 60]

      10
     /  \
   20    30
  /        \
40         60

Output: [10, 20, 30, 60, 40]

Explanation:
Level 0 → right to left → [10]  
Level 1 → left to right → [20, 30]  
Level 2 → right to left → [60, 40]
```

---

### Example 3

```
Input: root = [1, 2, N, 4]

    1
   /
  2
 /
4

Output: [1, 2, 4]
```

---

## Constraints

* `1 ≤ number of nodes ≤ 10^5`
* `0 ≤ node->data ≤ 10^5`

---

## Expected Complexity

* **Time Complexity**: O(n)
* **Auxiliary Space**: O(n)

---

## Tags

### Company Tags

`Flipkart`, `Morgan Stanley`, `Accolite`, `Amazon`, `Microsoft`, `Hike`, `MakeMyTrip`, `Adobe`, `Walmart`, `Payu`, `Ola`, `Housing.com`, `Teradata`

### Topic Tags

`Tree`, `Stack`, `Recursion`, `Data Structures`, `Algorithms`

---

## Related Content

* **Interview Experiences**:

  * Flipkart Interview Experience Set 24
  * Amazon Interview Experience Set 357 | 5 Years Experienced
  * Make My Trip Interview Experience On Campus

* **Article**: [Level Order Traversal in Spiral Form](#)

---

If you’d like code implementations in Python, C++, or JavaScript for this problem using stacks or deque, just let me know!
