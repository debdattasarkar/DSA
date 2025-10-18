**“60-second recall kit”** and **5-line pseudo-code skeleton** for the classic **Minimize the Heights II** (Greedy + Sorting) problem — a problem that’s both **mathematically elegant** and **commonly asked** in interviews by Microsoft and Adobe.

---

## 🧠 5-Line Pseudo-code Template (Universal)

```
function getMinDiff(arr, k):
    sort(arr)                                      # 1️⃣ sort heights
    ans = arr[n-1] - arr[0]                        # 2️⃣ initial difference
    for i from 1 to n-1:                           # 3️⃣ try each partition
        if arr[i] - k < 0: continue                # skip negatives
        small = min(arr[0] + k, arr[i] - k)        # 4️⃣ new min
        big   = max(arr[i-1] + k, arr[n-1] - k)    # 5️⃣ new max
        ans = min(ans, big - small)
    return ans
```

✅ That’s all — you can literally rebuild this in **any language** in under **30 seconds**.

---

## 🧩 Mnemonic (to remember easily)

> **“Sort → Split → Skip → Shrink.”**

1️⃣ **Sort** the array (so the order is predictable).
2️⃣ **Split** at every index `i` — left `(+k)` and right `(-k)`.
3️⃣ **Skip** invalid cases (no negatives allowed).
4️⃣ **Shrink** the difference by choosing new min/max.

Say it once before coding:

> “Sort, Split, Skip, Shrink.”

---

## ⚙️ Intuitive Explanation

After sorting:

* If you **add `k`** to the first `i` towers and **subtract `k`** from the rest,
  you’re exploring every valid configuration of raises and lowers.
* The smallest height after modification can come from either:

  * the leftmost tower raised by `k`
  * or a tower on the right decreased by `k`.
* The largest height can come from:

  * the rightmost tower lowered by `k`
  * or a tower on the left increased by `k`.

You compute both, take their difference, and minimize it.

---

## ⚡ Quick Example (dry run mentally)

```
arr = [1, 5, 8, 10], k = 2
Sorted → [1, 5, 8, 10]
Initial ans = 10 - 1 = 9

i = 1 → small = min(3, 3)=3, big=max(3,8)=8 → diff=5
i = 2 → small=min(3,6)=3, big=max(7,8)=8 → diff=5
i = 3 → small=min(3,8)=3, big=max(10,8)=10 → diff=7

✅ Minimum diff = 5
```

---

## 🧠 60-Second Recall Before Interview

When interviewer says:

> “Minimize the difference between max and min heights by ±K.”

You instantly recall:

1️⃣ **Sort the array.**
2️⃣ **Initial diff = last - first.**
3️⃣ **Loop i = 1 → n-1:**

* Skip negatives (`arr[i]-k < 0`).
* Compute `small` = min(first+k, arr[i]-k).
* Compute `big` = max(last-k, arr[i-1]+k).
* Minimize `ans`.
  4️⃣ **Return ans.**

**Time:** O(n log n) (sorting)
**Space:** O(1)

---

## 🧩 Quick “Why It Works” for Interviewers

> “Once sorted, the optimal configuration will always be a single split — all elements before `i` increased by `k`, all elements after `i` decreased by `k`.
> Trying every split guarantees we find the smallest possible max-min difference.”

---

## ✅ Final 10-Second Recap

| Step | Action           | Purpose                | Mnemonic   |
| ---- | ---------------- | ---------------------- | ---------- |
| 1️⃣  | Sort array       | To apply uniform logic | **Sort**   |
| 2️⃣  | Initialize `ans` | Start with max spread  | **Start**  |
| 3️⃣  | Loop `i`         | Try each split         | **Split**  |
| 4️⃣  | Skip invalids    | Avoid negatives        | **Skip**   |
| 5️⃣  | Update min/max   | Shrink difference      | **Shrink** |

💡 **Mnemonic:** **“Sort, Start, Split, Skip, Shrink.”**

Say that rhythm once, and you’ll recall the full solution instantly in interviews.
