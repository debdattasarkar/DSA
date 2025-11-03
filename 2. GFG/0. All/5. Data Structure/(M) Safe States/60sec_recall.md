**5-line pseudo-code template** + a **mnemonic** so you can recall the Safe States logic in 60 seconds before your interview.

---

## 🧠 5-Line Pseudo-Code Template (Universal)

**Goal:** find all nodes that *cannot reach a cycle* (a.k.a. “eventually safe”).

```
1. Build graph + reverse_graph + outdegree[]  
2. Push all nodes with outdegree == 0 into queue  
3. While queue not empty:
       pop node → mark safe
       for each pred in reverse_graph[node]:
            if (--outdegree[pred] == 0): queue.push(pred)
4. Return all safe nodes (sorted)
```

---

## ⚡ Mnemonic: **"B-R-O-Q-S" → BROQS**

👉 say it like “brocks” — super fast to recall logic flow.
Each letter = the step in your topological-safe peeling algorithm:

| Letter | Step                | Meaning                     | Quick recall             |
| :----- | :------------------ | :-------------------------- | :----------------------- |
| **B**  | **Build**           | graph + reverse + outdegree | Build both maps          |
| **R**  | **Reverse**         | process reversed edges      | Flip directions          |
| **O**  | **Outdegree check** | terminal nodes start queue  | Outdegree 0 ⇒ enqueue    |
| **Q**  | **Queue BFS**       | peel nodes backward         | While queue not empty    |
| **S**  | **Safe list**       | collect results             | return sorted safe nodes |

**→ BROQS = Build → Reverse → Outdegree → Queue → Safe**

💡 Just whisper “BROQS” mentally, and the logic flows.

---

## ⚙️ DFS version (alternate 5-line skeleton)

If you prefer recursion:

```
1. Build adjacency list
2. Define dfs(node):
       if visiting → cycle → False
       mark visiting
       if any neighbor unsafe → False
       mark safe → True
3. Run dfs(node) for all
4. Return all safe nodes
```

Mnemonic: **"C-C-V-S" → “Cycle-Check, Visit, Safe”**
→ You remember the loop: check cycle → mark visiting → explore → mark safe.

---

## 🧩 60-second pre-interview recall checklist

Before they hand you the problem:

* “Safe node = cannot reach cycle.”
* Two standard tools:
  🔹 **Reverse + Kahn BFS (BROQS)**
  🔹 **DFS 3-color (Cycle-Check-Visit-Safe)**
* Complexity = O(V + E) time, O(V + E) space.
* Always start from **terminal nodes (outdeg=0)**.
* Return sorted safe nodes (because nodes labeled 0..V-1).

---

✅ **Tip:**
Right before the interview starts, write this on your scratchpad:

```
BROQS → Build Reverse Outdegree Queue Safe
```

That single line is your 5-step “anchor.”
You can reconstruct the entire working code in **under 30 seconds** in Python, C++, or Java.
