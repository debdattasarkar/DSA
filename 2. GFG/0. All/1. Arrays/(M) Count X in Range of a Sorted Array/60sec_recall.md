## 5-Line Pseudo-Code Template (Count X in Range)

```text
for each query (l, r, x):
    left  = first index ≥ x in [l, r]        // lower_bound
    right = first index > x in [l, r]        // upper_bound
    answer = right - left
return all answers
```

That’s the **entire algorithm**.

---

## Ultra-Simple Mnemonic (30–60 second recall)

### 🧠 Phrase to remember

> **“Sorted range → UB minus LB.”**

### Visual recall

* **LB** → where `x` **starts**
* **UB** → where `x` **ends + 1**
* **Count** → `UB - LB`

### Spoken interview version (15 seconds)

> “Array is sorted. All x’s are contiguous.
> For each query, I binary-search inside [l, r].
> Count equals upper_bound minus lower_bound.”

---

## 60-Second Interview Recall Script

1. **Sorted array ⇒ binary search**
2. **Range query ⇒ search only [l, r]**
3. **Find first ≥ x**
4. **Find first > x**
5. **Subtract**

If you remember **“first ≥ x”** and **“first > x”**, the code writes itself in any language.

---

## One-Line Mental Formula

```text
COUNT(x in [l, r]) = UB(x, l..r) − LB(x, l..r)
```

If you want, next I can:

* draw a **sticky-note sketchnote** for this (LB/UB arrows),
* or show the **hashmap + index list** optimization variant.
