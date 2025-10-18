Here’s your **“60-second recall kit”** and **5-line pseudo-code skeleton** for the **Union of Arrays with Duplicates** problem.

---

## 🧠 5-Line Pseudo-Code (universal skeleton)

```
function union(a, b):
    seen = empty set                   # keeps unique elements
    for each x in a: add x to seen
    for each x in b: add x to seen
    return sorted(list(seen))          # sorted for deterministic output
```

✅ Works in Python, C++, Java, or C#.
Just replace `set` with your language’s hash-set or boolean array.

---

## 🧩 Mnemonic (easy to recall)

> **“Add–Add–Sort–Return.”**

1️⃣ **Add** all from `a` into a set
2️⃣ **Add** all from `b` into the same set
3️⃣ **Sort** it (only if required)
4️⃣ **Return** result

→ Say to yourself: **“Add–Add–Sort–Return”** before coding.

---

## ⚙️ If interviewer asks for O(1) extra space

Use **two-pointer technique** on sorted arrays:

```
sort(a), sort(b)
i=j=0
while i<n and j<m:
    take smaller (or equal) value, skip duplicates
drain remaining values (skip duplicates)
```

✅ Mnemonic: **“Sort–Merge–Skip–Append.”**

---

## 🧩 Dry-run example

```
a = [1,2,3,2,1]
b = [3,2,2,3,3,2]
```

1️⃣ Add from `a`: seen = {1,2,3}
2️⃣ Add from `b`: seen = {1,2,3} (unchanged)
3️⃣ Sorted output = `[1,2,3]`

---

## 🧠 60-Second Recall Before Interview

1️⃣ **Goal:** every unique element once (union, not concat).
2️⃣ **Hash-set or merge** both arrays.
3️⃣ **Skip duplicates** (set or manual).
4️⃣ **Sort if needed.**
5️⃣ **Return.**

---

## 💬 10-Second “Why” Answer

> “A union keeps all distinct elements from both arrays exactly once.
> I use a set (O(n+m) average time) or two-pointer merge if arrays are sorted (O(n+m) time).
> Sorting adds O((n+m) log (n+m)) if needed.”

---

## ⚙️ Quick Complexity Recap

| Approach           | Time               | Space  | When to use              |
| ------------------ | ------------------ | ------ | ------------------------ |
| **Set union**      | O(n+m) avg         | O(n+m) | Fastest to code          |
| **Sorted + merge** | O((n+m) log (n+m)) | O(1)   | Arrays already sorted    |
| **Counting array** | O(n+m+U)           | O(U)   | When 0 ≤ a[i],b[i] ≤ 10⁵ |

---

**✅ Mnemonic summary table**

| Step | Action                 | Keyword |
| ---- | ---------------------- | ------- |
| 1️⃣  | Add elements from `a`  | Add-A   |
| 2️⃣  | Add elements from `b`  | Add-B   |
| 3️⃣  | Sort result (optional) | Sort    |
| 4️⃣  | Return final list      | Return  |

> **“Add-A, Add-B, Sort, Return.”**
> That’s your 5-line mental skeleton for **Union of Arrays with Duplicates** — rebuildable in **30 seconds** anywhere.
