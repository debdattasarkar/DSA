**“5-line pseudo-code template”**, PLUS a **super-easy mnemonic** and a **60-second recall script** you can rehearse before going into an interview.

This matches the **correct Second MST algorithm** (the version YOU validated).

---

# ✅ **5-Line Pseudo-Code Template (Perfect for Interviews)**

```
1. Build MST using Kruskal → mark MST edges, compute MST_weight.
2. Build adjacency list of MST (tree).
3. For each non-MST edge (u, v, w):
4.     Get all edges on MST-path(u, v).
5.     For each path-edge f with weight wf:
6.         candidate = MST_weight + w − wf
7. Return minimum candidate > MST_weight (or -1)
```

This is literally the entire algorithm in **7 lines**.
You can rewrite it in **any language in under 30 seconds**.

---

# 🎯 **Ultra-Easy Mnemonic**

Remember this phrase:

## **“Add edge → get cycle → try removing EVERY edge on the cycle.”**

Breakdown:

* “Add edge” → the non-MST edge
* “Cycle” → appears because MST is a tree
* “Every edge” → not just the max!
  (This is the KEY trick that many candidates miss)
* Compute:

  ```
  MST + extra_edge_weight − removed_edge_weight
  ```
* Minimum weight **strictly greater** than MST = second MST.

---

# 🧠 **The 60-Second Interview Recall Script**

Say this to yourself before the interview:

> “First, I build the MST using Kruskal.
> The MST is a tree, so adding any non-MST edge forms exactly one cycle.
> The next-best spanning tree must be formed by adding that extra edge and removing **one** of the edges on the cycle.
> To find candidates, I compute the path between the edge’s endpoints in the MST and collect all edges along it.
> For each edge f on that path, I compute
> candidate = MST_weight + w(extra) − w(f).
> I keep the smallest candidate strictly greater than the MST weight.
> This guarantees correctness because I evaluate **every possible cycle edge removal**, not just the maximum weight edge.
> Time complexity is O(E log E + E·V), fine for V ≤ 100.”

This is polished, fast, and sounds extremely strong to interviewers.

---

# ⚡ Extra Quick Memory Markers

### 1. **3 objects**

* MST
* Extra edge
* MST-path between endpoints = cycle edges

### 2. **One formula**

```
candidate = MST + w(extra) − w(path_edge)
```

### 3. **One condition**

```
candidate > MST
```

### 4. **One answer**

→ minimum such candidate

---
