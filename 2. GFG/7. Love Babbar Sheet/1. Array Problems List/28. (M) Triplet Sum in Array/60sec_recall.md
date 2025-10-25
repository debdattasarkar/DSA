👌**5-line pseudo-code template + 60-second recall mnemonic** for
🧩 **Triplet Sum in Array** (a classic interview favorite).

---

## ⚙️ 5-Line Pseudo-Code Template (Universal Skeleton)

```
sort(arr)
for i in 0..n-3:
    l, r = i+1, n-1
    while l < r:
        s = arr[i] + arr[l] + arr[r]
        if s == target: return True
        elif s < target: l += 1
        else: r -= 1
return False
```

✅ **O(n²)** time
✅ **O(1)** extra space
✅ Works for positive, negative, and mixed arrays

---

## 🧠 Easy Mnemonic — “**S-F-T**” → *Sort, Fix, Two-pointers*

| Step  | Meaning                                         | Visual Image                            |
| ----- | ----------------------------------------------- | --------------------------------------- |
| **S** | **Sort** the array                              | 🪜 laying the numbers in order          |
| **F** | **Fix** one number `arr[i]`                     | 🎯 anchor for two-pointer search        |
| **T** | Use **Two pointers** (`l` & `r`) to move inward | 🔁 like a zipper closing from both ends |

> 💭 **Catchphrase:**
> “Sort → Fix → Two-pointer shrink — match target or move inward.”

---

## 🕒 60-Second Recall Routine (before interview)

1. **Say the problem clearly:**
   “Find any 3 numbers that sum to a target — `O(n²)` two-pointer after sorting.”

2. **Recall the core loop mentally:**

   * Sort.
   * For each `i`, set `l=i+1`, `r=n-1`.
   * If `sum==target` ✅ return True.
   * If `sum<target` ➡️ move `l++`.
   * If `sum>target` ⬅️ move `r--`.

3. **Edge handling (5 seconds):**

   * `len(arr)<3 → False`
   * Works fine with negatives/positives.
   * Sorting removes duplicates handling complexity.

4. **Complexity mantra:**
   “Time O(n²), Space O(1). Sorting enables pointer motion.”

5. **Verbal memory line:**

   > 🧩 “**Sort, Fix, Shrink — till Sum fits Target.**”

