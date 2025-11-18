**5-line pseudo-code template** + **memory trick** you can rehearse in < 60 seconds before an interview.
This is specifically crafted for *minimax graph/grid path problems* like **“Path With Minimum Effort”** (absolute difference, minimize the maximum edge weight).

---

# ✅ **5-Line Pseudo-Code (Dijkstra-Minimax Template)**

```
1. cost[start] = 0, push (0, start) into min-heap
2. while heap not empty:
3.     pop (currCost, node)
4.     for each neighbor:
5.         newCost = max(currCost, edgeWeight); relax & push if smaller
```

That is **literally everything needed**.
From this skeleton, you can rebuild Python, C++, Java, JavaScript, Go, etc. in under a minute.

---

# 🎯 **Mapping It to the Grid Problem**

* `node` → `(r, c)`
* `neighbor` → up, down, left, right if in bounds
* `edgeWeight` → `abs(mat[r][c] - mat[nr][nc])`
* `cost[][]` → 2D array storing minimum max-diff found so far
* `start` → `(0,0)`
* `end` → `(n-1, m-1)`; return cost when popped

---

# 🧠 **Ultra-Easy Mnemonic: “PQ-POP-RELAX-MAX”**

Memorize this acronym:

### **PQ → POP → RELAX → MAX**

Meaning:

1. **PQ** → use a **P**riority **Q**ueue (min-heap)
2. **POP** → pop smallest cost cell
3. **RELAX** → check all neighbors
4. **MAX** → update neighbor using

   ```
   newCost = max(currCost, edgeDiff)
   ```

That’s the entire minimax Dijkstra idea in 4 syllables.

Say it before entering the interview room.

---

# 🧠 Why This Is Easy to Remember

This problem reduces to:

> “Dijkstra but instead of summing weights, take the max.”

So the entire modification is this one line:

```
newCost = max(currentCost, edgeWeight)
```

If you can recall that *one* line, the rest is plain Dijkstra.

---

# ⚡ 60-Second Interview Recall Script

(Practice saying this out loud)

> “This is a minimax path.
> The edge cost is abs difference. The path cost is the maximum edge.
> So I just run Dijkstra, but instead of summing, I do `newCost = max(currCost, diff)`.
> Use a min-heap, pop the smallest cost, relax neighbors, update cost grid.
> First time I pop the bottom-right, that cost is the answer.”

This is a polished, interview-ready explanation.

---

# 🎯 **If you want, I can also give you:**

* **10-second whiteboard version**
* **Reusable template for all minimax problems**
* **One-page cheat sheet** for grid graph shortest path patterns (BFS vs Dijkstra vs 0-1 BFS vs Minimax).
