Here is the **perfect 5-line pseudo-code template** + an **ultra-easy mnemonic** for this problem.
This is the version you can memorize and rebuild in **under 30 seconds** in any language.

---

# ✅ **5-Line Pseudo-Code (All-Pairs + Per-Index Merge)**

```
1. Build 26×26 dist[][], init INF except dist[u][u] = 0
2. For each transform x→y: dist[x][y] = min(dist[x][y], cost)
3. Run Floyd–Warshall on dist to get all-pairs shortest paths
4. For each index i: find best c = min(dist[s[i]][c] + dist[t[i]][c])
5. If any i impossible return -1 else sum the best costs
```

That is the **entire algorithm**, compressed into 5 lines.

No matter the language, these 5 lines always turn into the real solution.

---

# 🧠 **Super-Easy Mnemonic: "Build → FW → Merge"**

Memorize the mantra:

### **Build → FW → Merge**

Where:

* **Build** = build the 26×26 cost matrix
* **FW** = Floyd–Warshall (all-pairs shortest paths)
* **Merge** = for each index, merge both letters into the best meeting letter

That’s it.

You can say it confidently at the start of the interview:

> “This is a letter-graph problem. I Build the cost graph, run Floyd-Warshall for all-pairs shortest paths, then Merge characters position-wise by choosing the cheapest common target letter.”

Interviewer will instantly understand you know the pattern.

---

# ⏱ **60-Second Recall Script**

(Practice this before entering the interview)

> “We must convert s and t into the same final string.
> Letters form a 26-node directed graph with transformation costs.
> We need cheapest x→y conversion for every pair, so we use Floyd–Warshall (26³ is constant).
> For each index, I pick the best letter c that both s[i] and t[i] can reach and add their costs.
> If any index can’t reach the same c, return –1.
> Total is O(n), since per index we check 26 letters.”

If you say this confidently, interviewer immediately knows:
**You see the graph, the dynamic programming, and the all-pairs structure.**

---
