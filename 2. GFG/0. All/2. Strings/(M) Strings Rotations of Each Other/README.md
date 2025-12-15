# Strings Rotations of Each Other 🔁

**Difficulty:** Medium  
**Accuracy:** 43.83%  
**Submissions:** 327K+  
**Points:** 4  
**Average Time:** 15m  

---

## Problem Statement

You are given two strings `s1` and `s2`, of equal lengths. The task is to check if **`s2` is a rotated version of the string `s1`**.

> **Note:**  
> A string is a rotation of another if it can be formed by moving characters from the start to the end (or vice versa) **without rearranging them**.

---

## Examples

### Example 1

**Input:** `s1 = "abcd", s2 = "cdab"`  
**Output:** `true`  

**Explanation:**  
After 2 right rotations, `s1` will become equal to `s2`.

---

### Example 2

**Input:** `s1 = "aab", s2 = "aba"`  
**Output:** `true`  

**Explanation:**  
After 1 left rotation, `s1` will become equal to `s2`.

---

### Example 3

**Input:** `s1 = "abcd", s2 = "acbd"`  
**Output:** `false`  

**Explanation:**  
Strings are not rotations of each other.

---

## Constraints

- \(1 \le s1.\text{size}(), s2.\text{size}() \le 10^5\)  
- `s1`, `s2` consist of lowercase English alphabets.

---

## Expected Complexities

- **Time Complexity:** `O(n)`  
- **Auxiliary Space:** `O(n)`  

---

## Company Tags

- Oracle  
- Adobe  

---

## Topic Tags

- Strings  
- Data Structures  

---

## Related Interview Experiences

- Adobe Interview Experience Set 44 For Mts 1  

---

## Related Articles

- A Program To Check If Strings Are Rotations Of Each Other  


---

---

I’ll follow your numbering.

---

## 2. Explanation + Step-by-step dry run

### Problem in plain words

You’re given two strings `s1` and `s2` (same length).
You must check:

> Can `s2` be obtained by taking some prefix of `s1` and moving it to the end (or vice-versa) without reordering characters?

That is exactly what *rotation* means.

Examples:

* `"abcd"` → rotations: `"abcd"`, `"bcda"`, `"cdab"`, `"dabc"`.
* `"aab"` → rotations: `"aab"`, `"aba"`, `"baa"`.

---

### Key observation (super-important trick)

If `s2` is a rotation of `s1`, then:

> `s2` will appear as a **substring of** `s1 + s1`.

Why?
Because concatenating `s1` with itself essentially lists all ways of wrapping around the end.

Example:

`s1 = "abcd"`
`s1 + s1 = "abcdabcd"`

All length-4 substrings of `"abcdabcd"`:

* `"abcd"` (shift 0)
* `"bcda"` (shift 1)
* `"cdab"` (shift 2)
* `"dabc"` (shift 3)

That’s exactly all rotations of `s1`.

So algorithm is:

1. If lengths differ → **not** rotations (`False`).
2. Otherwise, create `doubled = s1 + s1`.
3. If `s2` is a substring of `doubled` → rotations (`True`), else `False`.

Time: O(n) if substring search is O(n).
Space: O(n) for `doubled` (size 2n).

---

### Dry run 1: `s1 = "abcd", s2 = "cdab"`

1. Length check: both length 4 → OK.
2. `doubled = "abcdabcd"`.
3. Check if `"cdab"` appears inside `"abcdabcd"`:

   Substrings of length 4:

   * `"abcd"` (idx 0–3)
   * `"bcda"` (1–4)
   * `"cdab"` (2–5) ✅ match
   * ...

Since we find `"cdab"` inside, answer = `True`.

---

### Dry run 2: `s1 = "aab", s2 = "aba"`

1. Length check: both length 3 → OK.
2. `doubled = "aab" + "aab" = "aabaab"`.
3. Look for `"aba"` inside `"aabaab"`:

   Substrings of length 3:

   * `"aab"` (0–2)
   * `"aba"` (1–3) ✅ match
   * `"baa"` (2–4)
   * `"aab"` (3–5)

Found → `True`.

---

### Dry run 3: `s1 = "abcd", s2 = "acbd"`

1. Length check: both length 4 → OK.
2. `doubled = "abcdabcd"`.
3. Substrings of length 4 are `"abcd"`, `"bcda"`, `"cdab"`, `"dabc"`.

`"acbd"` never appears → `False`.

---

## 3. Python solutions

We’ll write:

1. **Brute force**: generate each rotation and compare.
2. **Optimized**: use the `s1 + s1` substring trick.
3. (Optional) **KMP version**: if interviewer asks for manual O(n) substring search.

Signature you gave:

```python
class Solution:
    def areRotations(self, s1, s2):
        # code here
```

### 3.1 Brute-force solution (generate all rotations)

```python
class Solution:
    def areRotations_bruteforce(self, s1: str, s2: str) -> bool:
        """
        Brute-force approach:
            - If lengths differ, can't be rotations.
            - For every possible rotation index 'k' from 0..n-1:
                * Build the rotation: s1[k:] + s1[:k]
                * Compare with s2.

        Time  : O(n^2)   (we build/compare O(n) strings of length n)
        Space : O(n)     (temporary rotated string)
        """
        if len(s1) != len(s2):
            return False

        n = len(s1)
        for k in range(n):
            rotated = s1[k:] + s1[:k]  # rotation by k characters
            if rotated == s2:
                return True

        return False
```

Good for understanding, but not optimal for large `n`.

---

### 3.2 Optimized solution (using `s1 + s1`)

```python
class Solution:
    def areRotations(self, s1: str, s2: str) -> bool:
        """
        Optimized solution using concatenation trick.

        Logic:
            - Two strings of equal length are rotations iff
              s2 is a substring of (s1 + s1).

        Steps:
            1. If lengths are different -> immediately return False.
            2. Compute doubled = s1 + s1.
            3. Check if s2 occurs in doubled using 'in' (Python's substring search).

        Complexity:
            Let n = len(s1) = len(s2).

            - Building 'doubled' (size 2n):      O(n) time & O(n) space.
            - Substring search 's2 in doubled':  O(n) average and O(n) worst-case.
            - Total Time: O(n)
            - Extra Space: O(n) for 'doubled'.
        """
        # Length must match
        if len(s1) != len(s2):
            return False

        # Empty strings case: two empty strings are rotations of each other
        if not s1 and not s2:
            return True

        doubled = s1 + s1
        return s2 in doubled
```

This is the standard and most expected answer in interviews.

---

### 3.3 (Optional) KMP-based version (manual O(n))

If an interviewer says “don’t rely on library substring search; implement O(n) yourself”, you can embed a classic KMP matcher on top of `doubled`.

High-level idea:

* Precompute LPS (longest proper prefix which is also suffix) for `s2`.
* Run KMP pattern matching for `s2` in `doubled`.
* If found → rotation.

I’ll keep it short and commented:

```python
class Solution:
    def _build_lps(self, pattern: str):
        """
        Build LPS (Longest Prefix Suffix) array for KMP.
        lps[i] = length of the longest prefix of pattern that is also a suffix
                 for the substring pattern[0..i].

        Time:  O(m) where m = len(pattern)
        Space: O(m)
        """
        m = len(pattern)
        lps = [0] * m
        length = 0  # length of current longest prefix-suffix
        i = 1

        while i < m:
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1

        return lps

    def areRotations_kmp(self, s1: str, s2: str) -> bool:
        """
        KMP-based rotation check:
            - Same as optimized, but perform substring search (s2 in s1+s1)
              manually using KMP to guarantee O(n).

        Time:  O(n)
        Space: O(n) for 'doubled' and lps.
        """
        if len(s1) != len(s2):
            return False

        doubled = s1 + s1
        text = doubled
        pattern = s2

        n = len(text)
        m = len(pattern)

        if m == 0:
            return True  # empty is substring

        lps = self._build_lps(pattern)

        i = j = 0  # i -> text index, j -> pattern index

        while i < n:
            if text[i] == pattern[j]:
                i += 1
                j += 1
                if j == m:
                    return True  # found match
            else:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1

        return False
```

In practice for interviews, the `s2 in s1 + s1` version is usually enough, but knowing KMP gives you “bonus points”.

---

## 4. Interview strategy: How to remember & what they’ll ask

### Super-short memory hook

Just memorize:

> **“Same length AND s2 in s1+s1 → rotation.”**

That’s literally the whole algorithm.

Mini mnemonic:

> **“Concat & find”**
>
> 1. Compare lengths.
> 2. Concatenate `s1+s1`.
> 3. Check substring.

If you can recall that 3-step recipe, you can code the solution in < 1 minute.

---

### Likely interview questions & good answers

---

**Q1: What’s your brute-force approach and its complexity?**

**A:**
Generate every rotation of `s1` and compare with `s2`:

```text
for k in 0..n-1:
    rotation = s1[k:] + s1[:k]
    if rotation == s2: return True
return False
```

* There are `n` rotations, each length `n` → O(n²) time, O(n) space.

---

**Q2: How did you optimize it?**

**A:**
Use this property:

> `s2` is a rotation of `s1` ↔ `len(s1) == len(s2)` and `s2` is a substring of `s1 + s1`.

So I:

1. Check length equality. If not equal → immediately `False`.
2. Compute `doubled = s1 + s1`.
3. Return `s2 in doubled`.

Creating `doubled` is O(n); substring search is O(n) using efficient algorithms → overall O(n) time, O(n) extra space.

---

**Q3: Why does `s2` in `s1 + s1` guarantee it’s a rotation and not some random substring?**

**A:**
Any rotation of `s1` is created by choosing a cut position `k`:

```text
rotation_k = s1[k:] + s1[:k]
```

If you write `s1 + s1`, you literally concatenate `s1[k:]` with `s1[:k]` for every possible `k` somewhere inside that concatenation. So every rotation appears as a contiguous substring of `s1 + s1`. Conversely, any length-`n` substring of `s1 + s1` that starts within the first `n` characters corresponds to a rotation of `s1`.

---

**Q4: What are the time and space complexities of your optimized solution?**

**A:**

* Let `n = len(s1) = len(s2)`.

Time:

* Building `doubled = s1 + s1` → O(n).
* Checking if `s2` is substring of `doubled` → O(n) using standard substring algorithms.
* Total = **O(n)**.

Space:

* Need `2n` characters for `doubled` → **O(n)** auxiliary space.

---

**Q5: Could you do it without building `s1 + s1`?**

**A:**
Yes, conceptually you can simulate the same idea without allocating a new string, by:

* Implementing a custom comparator that treats indices modulo `n`, or
* Using a rolling hash / KMP on the fly over `s1` considered circular.

But the simplest, most readable method is to build `s1 + s1` explicitly. In most practical settings O(n) extra memory is acceptable.

---

**Q6: Are all permutations rotations? What’s the difference?**

**A:**
No. Rotations keep the **relative order** of characters, they just wrap around the ends. Permutations can reorder arbitrarily.
For example, `s1 = "abcd"`:

* Rotations: `"abcd"`, `"bcda"`, `"cdab"`, `"dabc"`.
* `"acbd"` is a permutation but not a rotation (order broken).

---

If you remember just:

> **“Check length, then `s2 in s1+s1`.”**

you’ll be able to reconstruct the algorithm and code confidently under interview pressure.


---

---

Let’s finish this one cleanly.

---

## 5. Real-World Use Cases (easy to talk about)

These are scenarios where checking “rotation equivalence” of strings is directly useful or a very natural analogy:

1. **Circular Buffers / Ring Logs**

   * Many systems use circular buffers for logs or streaming data.
   * A buffer’s content can “start” at any internal index, then wrap around.
   * Two dumps of the same circular buffer at different times will look like **rotations** of each other.
   * To check if two dumps represent the same sequence of events (ignoring where the head is), you check if one string is a rotation of the other.

2. **Clock / Cyclic Schedule Matching**

   * Daily schedules or cyclic patterns (e.g., “ABCDABCD…” for tasks) might shift based on time zones or start times.
   * If you want to know whether two schedules are the *same cycle* but start at different times, you check if one is a rotation of the other.
   * Example: `“work-gym-dinner-sleep”` vs `“gym-dinner-sleep-work”`.

3. **DNA / Circular Genome Matching (conceptual)**

   * Some DNA molecules (like bacterial plasmids) are circular.
   * The same circular sequence may be “cut” and written starting at different nucleotides.
   * Those different linear representations are rotations of each other; rotation checks help confirm they’re the same circular molecule.

These are easy to explain in an interview and map perfectly to the “s1+s1 contains s2?” idea.

---

## 6. Full Python Program with Timing + Complexity Comments

Below is a complete script:

* Reads `s1` and `s2` from input.
* Uses the optimized `s1 + s1` rotation check.
* Prints whether they are rotations.
* Measures and prints runtime using `time.perf_counter()`.

```python
import time


class Solution:
    def areRotations(self, s1: str, s2: str) -> bool:
        """
        Check if s2 is a rotation of s1 using the 's1 + s1' trick.

        1) If lengths differ, they cannot be rotations.
           Time : O(1)
           Space: O(1)

        2) Create a new string doubled = s1 + s1.
           - Length of doubled is 2 * n (where n = len(s1))
           Time : O(n)   (we copy n characters twice)
           Space: O(n)   (extra memory to store doubled)

        3) Check if s2 is a substring of doubled using Python's 'in':
           - Python uses efficient substring search (roughly O(n))
           Time : O(n)   (worst case)
           Space: O(1)   (no extra big structures, just indices internally)

        Overall Complexity:
            Let n = len(s1) = len(s2).
            Time : O(n)  (build doubled + substring search)
            Space: O(n)  (for the doubled string)
        """
        # Step 1: length check (O(1))
        if len(s1) != len(s2):
            return False

        # Edge case: two empty strings are rotations of each other
        if not s1 and not s2:
            return True

        # Step 2: concatenation, O(n) time and O(n) space
        doubled = s1 + s1

        # Step 3: substring check, O(n) time
        return s2 in doubled


# --------------------------- Driver with timing --------------------------- #

def main():
    """
    Driver program to:
      - Read input strings.
      - Call Solution.areRotations.
      - Print result and total runtime.

    Input format (simple):
        s1
        s2

    Example:
        abcd
        cdab

    Output:
        Are rotations? True
        Total elapsed time (seconds): 0.00000xx
    """

    print("Enter first string s1:")
    s1 = input().strip()

    print("Enter second string s2:")
    s2 = input().strip()

    solver = Solution()

    # Start timer just before the core logic.
    # time.perf_counter() gives high-resolution wall-clock time.
    start_time = time.perf_counter()

    # Core algorithm: O(n) time, O(n) space
    result = solver.areRotations(s1, s2)

    # Stop timer right after.
    end_time = time.perf_counter()

    print("\nAre rotations?", result)
    print(f"Total elapsed time (seconds): {end_time - start_time:.8f}")


if __name__ == "__main__":
    main()
```

### Example run (mentally)

Input:

```text
abcd
cdab
```

Output:

```text
Enter first string s1:
abcd
Enter second string s2:
cdab

Are rotations? True
Total elapsed time (seconds): 0.00000xx
```

You can paste this file (e.g., `string_rotation.py`) and run it directly.
On a coding platform, you’d only submit the `Solution` class with `areRotations`, but this full program is perfect for local practice and performance intuition.
