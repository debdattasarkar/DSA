

# ⭐ Number of Ways to Arrive at Destination

(Dijkstra + Counting Shortest Paths)

---

# ✅ **5-Line Pseudo-Code Template (Dijkstra + Ways)**

```
dist[] = INF; ways[] = 0
dist[0] = 0;  ways[0] = 1
minHeap = [(0, 0)]

while heap not empty:
    d, u = pop_min()
    for (v, w) in adj[u]:
        if d + w < dist[v]:      dist[v] = d + w;  ways[v] = ways[u]; push
        else if d + w == dist[v]: ways[v] += ways[u]

return ways[target]
```

This is the **exact skeleton** that works in Python/C++/Java.

---

# 🎯 **Ultra-Easy Mnemonic**

### **“Dijkstra + Copy or Add.”**

Say this aloud in the interview:

* **Copy** ways when you find a **better (shorter)** path.
* **Add** ways when you find an **equally short** path.

That's it. That single sentence gives the entire logic.

---

# 🧠 **Why It Works (10-second explanation)**

* Dijkstra ensures nodes are processed in **increasing shortest distance** order.
* Maintaining `ways[]` lets you track **how many shortest paths** reach each node.
* When improving `dist[v]` → **reset** `ways[v]`
* When matching `dist[v]` → **increment** `ways[v]`
* Finally, `ways[target]` is the count of shortest routes.

---

# ⏱ **60-Second Interview Recall Routine**

### **0–10 sec — Recognize the Pattern**

Weighted undirected graph + count shortest paths →
**Dijkstra with path-counting**.

### **10–20 sec — State the approach**

“I’ll run Dijkstra from node 0 and maintain an array:

* `dist[u]` = shortest time to u
* `ways[u]` = number of shortest paths to u

Relax edges while updating distances & ways.”

### **20–40 sec — Write the core logic**

```
if new < dist[v]: dist[v]=new; ways[v]=ways[u]
elif new == dist[v]: ways[v]+=ways[u]
```

### **40–50 sec — Complexity**

* Time: **O(E log V)**
* Space: **O(V + E)**
* Works because weights are non-negative.

### **50–60 sec — Close with intuition**

“Dijkstra gives shortest times; we just maintain how many times we reach a node *with the same shortest time*.”

---

# 🔥 Bonus 1-Line Memory Hook

### **“Update dist, update ways; better = copy, equal = add.”**
