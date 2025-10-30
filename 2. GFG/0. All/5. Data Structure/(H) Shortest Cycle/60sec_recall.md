**5-line pseudo-code template** for *Shortest Cycle in an Undirected Graph*, along with a mnemonic and a **60-second recall** cheat that you can use to rebuild it instantly during an interview.

---

## 🧠 5-Line Pseudo-code Template

```
for each node s in graph:
    set all dist[] = -1, parent[] = -1
    BFS from s:
        for each neighbor v of u:
            if v not visited: set dist[v]=dist[u]+1, parent[v]=u
            elif parent[u] != v: ans = min(ans, dist[u] + dist[v] + 1)
return ans if found else -1
```

That’s it — **5 lines** covers the entire shortest cycle logic.
Each BFS finds the smallest loop that includes `s`.

---

## 🧩 Mnemonic — **“BFS + Parent Check = Cycle Length”**

| Step  | Keyword                            | Meaning                               |
| ----- | ---------------------------------- | ------------------------------------- |
| **B** | **BFS per source**                 | Start from every vertex `s`           |
| **P** | **Parent tracking**                | Keep parent to avoid false tree edges |
| **C** | **Check non-parent edge**          | Detects a real cycle                  |
| **L** | **Length = dist[u] + dist[v] + 1** | Calculate the exact cycle length      |
| **M** | **Minimize**                       | Keep smallest seen so far             |

🧩 **Mnemonic phrase:**

> **“B–P–C–L–M → BFS, Parent, Check, Length, Minimize.”**

Repeat it once before the interview, and your brain will reconstruct the BFS pattern instantly.

---

## ⚙️ 60-Second Recall Routine

🕐 **0–15s:**
Recognize the pattern — “unweighted, undirected → shortest = BFS.”

🕐 **15–30s:**
Say the logic aloud:

> “Run BFS from each node; if I find an already visited neighbor that isn’t my parent, it closes a cycle of length `dist[u] + dist[v] + 1`.”

🕐 **30–45s:**
Sketch minimal pseudo:

```
for each s:
  BFS
    if parent[u]!=v and visited[v]:
       ans=min(ans,dist[u]+dist[v]+1)
```

🕐 **45–60s:**
Close with complexity summary (a must in interviews):

> “Each BFS = O(V+E); run for all vertices → O(V*(V+E)); Space O(V).
> BFS ensures shortest unweighted cycle since first cross-edge gives minimum path.”

---

## 💡 Interview Quick Recap Quote

If asked “Explain your idea in 20 seconds,” say this:

> “I run BFS from every node, tracking parents.
> Whenever I find an already visited neighbor that’s not my parent, I’ve found a cycle.
> Its length is `dist[u]+dist[v]+1`.
> I keep the smallest over all BFS runs.”

That’s your perfect elevator answer — short, confident, and complete.

---
