# Unique Paths in a Grid

## 📝 Problem Statement

You are given a 2D grid `grid[][]` of size `n x m` consisting of values **0** and **1**:

* A value of **0** means the cell is traversable.
* A value of **1** means the cell is blocked (you cannot enter).

You start at the top-left cell `(1, 1)` and need to reach the bottom-right cell `(n, m)`, moving **only right or down** at each step. Your task is to **calculate the total number of unique ways** to reach the target, considering the obstacles.

> Note: The first and last cell can also contain **1**. The result is guaranteed to fit in a **32-bit integer**.

---

## 📥 Input

* A 2D list `grid[][]` of size `n x m` with values `0` (open) and `1` (blocked).

---

## 📤 Output

* An integer representing the number of unique paths from the top-left to the bottom-right cell.

---

## 💡 Examples

### Example 1

**Input:**

```
n = 3, m = 3
grid = [[0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]]
```

**Output:** `2`

**Explanation:**

1. Right → Right → Down → Down
2. Down → Down → Right → Right

---

### Example 2

**Input:**

```
n = 1, m = 3
grid = [[1, 0, 1]]
```

**Output:** `0`

**Explanation:** Start is blocked; no path exists.

---

## ✅ Constraints

* `1 ≤ n * m ≤ 10^6`
* Grid cells: `grid[i][j] ∈ {0, 1}`

---

## ⏱ Expected Time & Space Complexity

* **Time Complexity:** `O(n * m)`
* **Auxiliary Space:** `O(n * m)`

---

## 💼 Company Tags

* Uber

---

## 🧠 Topic Tags

* Dynamic Programming
* Matrix
* Algorithms
* Data Structures

---

## 🔗 Related Links

* [Unique Paths in a Grid with Obstacles – GeeksforGeeks](https://www.geeksforgeeks.org/unique-paths-in-a-grid-with-obstacles/)

---

