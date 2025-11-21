Here is the **cleanest 5-line pseudo-code** + **mnemonic** + **60-second recall script** that will lock this problem into your memory for interviews.

---

# ✅ **5-Line Pseudo-Code Template (perfect for interviews)**

```
1. components = V, redundant = 0
2. For each edge (u,v):
       if union(u,v) merged: components -= 1
       else: redundant += 1
3. required = components - 1
4. If redundant >= required: return required
5. Else return -1
```

That’s it — this entire problem collapses to the above **5 lines**.

You can rewrite this in **any language** in <30 seconds.

---

# 🎯 **Ultra-Easy Mnemonic → “C-R Formula”**

Memorize this phrase:

### **“Components minus 1, paid for by Redundant edges.”**

Where:

* **Components** = number of disconnected groups
* **Redundant edges** = edges connecting nodes *already* in the same group (cycle edges)
* To connect all components:

  * You need **components − 1** edges
* You can only use **redundant** edges to pay for those

So the final check is:

### **If redundant ≥ components − 1 → possible

Else impossible**

---

# 🧠 **60-Second Recall Script (say this before entering the interview)**

> *“I treat the problem as counting how many disconnected components exist using DSU.
> Every time an edge connects two already-connected nodes, it is redundant — this is a ‘spare wire’ I can reuse.
> To connect C components, I need exactly C−1 operations.
> If I have at least C−1 redundant edges, I can rewire them to connect all components.
> Otherwise it’s impossible.
> DSU gives nearly O(1) per edge, so total time is O(V + E).”*

This is the **perfect** 1-minute explanation interviewers love.

---
