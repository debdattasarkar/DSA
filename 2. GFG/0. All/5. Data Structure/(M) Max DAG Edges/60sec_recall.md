**“Max DAG Edges”** ultra-short **5-line pseudo-code**, mnemonic, and **60-second recall routine** to keep in your head for interviews.

---

## 🧠 5-Line Pseudo-code Template (universal form)

```
E = number of edges
max_possible = V*(V-1)/2
extra_edges = max_possible - E
return extra_edges
```

Yes — it’s that simple.
One line of logic wrapped in three setup lines. 🔥

---

## 🧩 Mnemonic — **“V-PAIR Minus E”**

Breakdown:

* **V-PAIR** → think of **all possible ordered vertex pairs (i, j)** where `i < j`, i.e. the forward edges in a topological order.
  Count = `V*(V-1)/2`.
* **Minus E** → subtract the edges you already have.

🧩 Mnemonic phrase:

> “**Every DAG is a staircase — all forward pairs allowed, remove existing ones.**”

That visual helps you recall that:

* Topological order = ascending staircase.
* Each step upward is a safe edge (forward edge).
* You can add all the “missing steps” forward — never backward.

---

## ⚙️ 60-second Recall Routine (before the interview)

🕐 **0–15s: Recognize the type**

> “DAG + max edges + no cycle” → must be **topological-order reasoning**.

🕐 **15–30s: Recall the invariant**

> Max edges in DAG = all forward pairs `(i < j)` = `V*(V-1)/2`.

🕐 **30–45s: State the formula**

> Answer = total forward pairs – existing edges
> `= V*(V-1)/2 - E`

🕐 **45–60s: Explain reasoning aloud**

> “In a DAG, any edge added in topological order (earlier → later) is safe.
> There are `V*(V-1)/2` such pairs possible, and E are already used.
> So remaining = `V*(V-1)/2 - E`.”
> Complexity → **O(1)** time, **O(1)** space.

---

## 🎯 15-second Interview Summary

> “A DAG can have at most `V*(V-1)/2` edges — all possible forward pairs in some topological order.
> Subtract the current E to find how many can still be added.
> It’s O(1) time and O(1) space.”

