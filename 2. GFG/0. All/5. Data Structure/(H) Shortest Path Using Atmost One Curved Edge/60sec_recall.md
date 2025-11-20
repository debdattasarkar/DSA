Below is the **cleanest, shortest, interview-friendly 5-line pseudo-code** + **mnemonic** + **60-second recall script** for
**“Shortest Path Using At Most One Curved Edge.”**

This is the *exact mental template* you can memorize and rewrite in **any language in < 30 seconds**.

---

# ✅ **5-Line Pseudo-Code Template (Final & Minimal)**

```
1. Run Dijkstra(a) on straight edges → distA[]
2. Run Dijkstra(b) on straight edges → distB[]
3. ans = distA[b]                 # no curved edge
4. For each (x, y, w1, w2): ans = min(ans,
         distA[x] + w2 + distB[y],
         distA[y] + w2 + distB[x])
5. If ans == INF return -1 else return ans
```

That’s it.
Nothing more is required.

---

# 🎯 **Ultra-Easy Mnemonic: “2D + 1C”**

Memorize:

### **“Two Dijkstras + One Curved Scan”**

or simply

### **“2D + 1C”**

* **2D** → Two Dijkstras on straight edges (from `a` and from `b`)
* **1C** → One pass over the **Curved** edges to evaluate best possible curved usage

This naturally leads to the 5 lines above.

---

# 🧠 **Why this works (interview explanation)**

> “If the path uses a curved edge (x,y), then everything before x and after y must be straight.
> So cost = distA[x] + curved_w + distB[y].
> Thus we compute distA and distB using straight-only Dijkstra, and then scan each curved edge once.”

---

# ⏱️ **60-Second Recall Script (Say Out Loud Before Interview)**

> “This problem allows at most one curved edge, so any valid path is either all straight or exactly one curved edge in the middle.
> I compute straight-only distances from `a` (distA) and straight-only distances from `b` (distB).
> The straight-only candidate is distA[b].
> For each curved edge (x,y,w2), I try: distA[x] + w2 + distB[y] and distA[y] + w2 + distB[x].
> The minimum among all these is the shortest path with ≤1 curved edge.
> Complexity is O((V+E) log V) because of the two Dijkstras.
> Then I return −1 if unreachable.”

Say this verbatim in an interview = **10/10 answer**.

---
