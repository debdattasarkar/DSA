**Super-short, interview-friendly, easy-to-recall pseudo-code skeleton** you can memorize in under **60 seconds**.
This is specifically for the **Maximum Stone Removal** problem and works for both **DFS** and **DSU** approaches.

---

# ⭐ 5-Line Pseudo-Code Template (DSU Form)

*(The fastest and cleanest for interviews)*

```
1. Create DSU for all rows and columns (map col to col+offset).
2. For each stone (r, c): union(r, c+offset).
3. Count unique parents among all used row/column nodes.
4. Components = number of unique parents.
5. Answer = total_stones - Components.
```

---

# ⭐ 5-Line Pseudo-Code Template (DFS Form)

```
1. Build graph: stones are nodes; connect if share row/column.
2. For each unvisited stone: run DFS → count components.
3. Each component of size k contributes (k-1) removable stones.
4. Total_removal = sum(k-1) = N - components.
5. Return total_removal.
```

---

# ⭐ 30-Second Memory Mnemonic (DSU Approach)

**“Row-Col Join → Count Roots → N minus Roots.”**

Breakdown:

* **Row-Col Join**
  For each `(r, c)` connect `r` and `c+offset`.

* **Count Roots**
  Count distinct DSU roots among rows + columns used.

* **N minus Roots**
  Return `total_stones - number_of_components`.

This is literally the entire solution in one sentence.

---

# ⭐ 10-Second Mnemonic

**“Join all, keep one per group.”**

Meaning:

* If stones are connected (by row/column), they form a **group**.
* Each group must leave **one stone behind** → rest are removable.
* So: Answer = total_stones - groups.

---

# ⭐ How to Rebuild It Under Pressure (mental checklist)

### Think this in order (each step ~5 sec):

1️⃣ **What is the graph?**
Stones connected if same row or column.

2️⃣ **What is the rule?**
A connected component of size k → remove k−1 stones.

3️⃣ **What do we need?**
Number of connected components.

4️⃣ **How to get components fast?**
Treat row i and column j as DSU nodes → Union(row, col).

5️⃣ **Final formula?**
Answer = total_stones − number_of_components.

---

# ⭐ 60-Second Pre-Interview Recall Script

Read this once before entering an interview:

> “This problem is connected components.
> Stones are nodes; same row/column = edge.
> In each component of size k, remove k−1 stones → total = N − components.
> I can count components via DFS (O(n²)) or DSU (faster).
> DSU trick: Treat each row and column as a node.
> Union(row, col+offset) for every stone.
> Count unique DSU parents = components.
> Return N − components.
> Time ~ O(n), space ~ O(n).
> This works because each cluster can only leave one stone.”

This script ensures:

* You sound confident
* You cover full logic
* You show knowledge of **graphs + DSU + optimization**
* You can derive code even without remembering exact lines

---
