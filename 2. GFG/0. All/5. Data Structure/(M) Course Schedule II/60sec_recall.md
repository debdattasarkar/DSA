Perfect 👏 — this is how you build a **memory muscle version** of **Course Schedule II (Topological Sort)** for interviews.
Here’s your **5-line pseudo-code**, **mnemonic**, and a **60-second recall routine** you can practice right before an interview.

---

## 🧠 5-Line Pseudo-code Template (Kahn’s BFS version – most expected)

```
build adj + indegree[]
queue = all nodes with indegree 0
while queue not empty:
    node = pop(); add to order
    for nei in adj[node]: indegree[nei] -= 1; if indegree[nei]==0: push
if len(order)==n: return order else return []
```

That’s the whole **Kahn’s Algorithm** in five lines — the heart of Course Schedule II.

---

## 🧩 Mnemonic: **“BID–Q–FIVE”**

To recall **Topological Sort (BFS/Kahn)** steps in the right order:

| Letter   | Meaning                              | Memory Trigger                           |
| -------- | ------------------------------------ | ---------------------------------------- |
| **B**    | **Build** adjacency list + indegree  | Build the roadmap first                  |
| **I**    | **Initialize** queue with indegree 0 | Start with independent courses           |
| **D**    | **Dequeue & record** course          | Take courses when prerequisites are done |
| **Q**    | **Queue neighbors** after indegree–1 | Unlock next available courses            |
| **FIVE** | **Final check**: len(order)==n ?     | (F)inish validation for cycles           |

🧩 **Mnemonic Phrase:**

> “**Build**, **Init**, **Dequeue**, **Queue**, then **Finish**.”

Or simpler:

> “**BID–Q–FIVE → Build, Init, Dequeue, Queue, Finish.**”

---

## ⚙️ 60-Second Recall Routine

### 🕐 0–15 seconds → Recognize the pattern

> Problem says “find ordering of tasks/courses with prerequisites.”
> → That’s **Topological Sort**.

### 🕐 15–30 seconds → Visualize Kahn’s flow

> * Make indegree for all nodes
> * Push 0-indegree to queue
> * Pop one → append to result
> * Reduce indegree of its neighbors
> * Push new 0s
> * End when queue empty
> * If result < n → cycle.

### 🕐 30–45 seconds → Recite pseudo aloud

```
for each edge y->x: indeg[x]++
queue = all 0 indeg
while q: u=pop(); order+=u; for v in adj[u]: indeg[v]-=1; if indeg[v]==0: q+=v
if len(order)==n: return order else []
```

### 🕐 45–60 seconds → Summarize complexity

> Time: O(n + m), each node/edge processed once.
> Space: O(n + m) for graph + queue + output.
> BFS avoids recursion limits; DFS works too (reverse postorder).

---

## 🎯 20-Second Interview Elevator Answer

> “I build an adjacency list and count indegrees for each node.
> Then I repeatedly take nodes with zero indegree (no prerequisites), append them to the order, and decrement their neighbors’ indegrees.
> If I process all `n`, that’s a valid schedule; otherwise, a cycle exists.
> It’s O(V + E) time and O(V + E) space.”
