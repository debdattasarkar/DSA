
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

## 💡 Problem: Minimum Number of Moves to Make a Palindrome

### ✅ Strategy:

Use a **two-pointer technique** combined with **greedy swaps** to bring matching characters from both ends toward the center.

---

### 🧩 Step-by-Step Breakdown:

1. **Initialize:**

   * `moves = 0` – track number of adjacent swaps.
   * Two pointers:

     * `i = 0` → start of string
     * `j = len(s) - 1` → end of string

2. **Match and Swap:**

   * Goal: Match `s[i]` with `s[j]`.
   * If `s[i] == s[j]` → move inward.
   * If not:

     * Search from `j` to `i` to find a match for `s[i]`.
     * If match is found at `k`, swap it toward `j`, incrementing `moves` for each step.
     * If match not found, `s[i]` is the unique center char → move it to center in `(n // 2) - i` steps.

3. **Post-Match:**

   * Continue matching next unmatched pair after each move.
   * Terminate when `i >= j`.

---

### 🧮 Time Complexity:

* **Worst Case:** `O(n²)`
  (Nested pointer movement with multiple swaps per character)

### 🗂 Space Complexity:

* **O(n)** – due to character list manipulation.

---

### 💡 Key Observations:

* At most one character can be unmatched (odd-length center).
* Swaps are local (adjacent only), so count each shift individually.
* Efficient greedy search from `j → i` minimizes swap count.

---
