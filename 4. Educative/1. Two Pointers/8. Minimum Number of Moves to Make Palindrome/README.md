
---

## 🧠 Problem: Minimum Number of Moves to Make Palindrome

### ❓ Statement:

Given a string `s`, return the **minimum number of adjacent swaps** required to transform `s` into a palindrome.

**You can swap any two adjacent characters.**

---

### ✅ Constraints:

* 1 ≤ `s.length` ≤ 2000
* Only lowercase English letters
* The input is **guaranteed to be convertible** into a palindrome.

---

## 🪄 Key Insight:

A string can be transformed into a palindrome **by making character pairs symmetric**, moving characters that are "out of place" to their matching positions using adjacent swaps.

---

## 🔁 Step-by-Step Algorithm:

1. **Initialize**:

   * `moves = 0` to track total number of swaps.
   * `left = 0`, `right = len(s) - 1`.

2. **Loop while left < right**:

   * If characters match at `left` and `right`:
     → move both inward.
   * Else:

     * **Search from `right` inward** to find a matching character for `s[left]`.
     * If found:
       → Swap it step-by-step until it reaches the `right` position.
       → Count each swap.
     * If not found (i.e., a lone middle char):
       → Swap it toward the middle and adjust.

3. **Repeat** until all pairs are matched.

4. **Return** total `moves`.

---

### 🔄 Dry Run Example:

**Input:** `"ccaxx"`
**Process:**

```
ccaxx → ccxax → ccxxa → cxcxa → xccxa → axccx → xccxa
```

**Output:** `2`

---

## ⏱️ Time Complexity:

* Worst-case: **O(n²)** (nested loop for matching and swapping)

## 🧠 Optimization Tip:

* Use **greedy pairing**: Always match the leftmost unmatched character with its rightmost mirror.

---


