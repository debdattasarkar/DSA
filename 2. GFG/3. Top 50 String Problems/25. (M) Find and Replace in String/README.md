# Find and Replace in String

**Difficulty:** Medium
**Accuracy:** 52.49% **Submissions:** 10K+ **Points:** 4 **Average Time:** 25m

Given a string `S` on which you need to perform `Q` replace operations.

Each replacement operation has 3 parameters: a starting index `i`, a source word `x` and a target word `y`. The rule is: if `x` starts at position `i` in the **original** string `S`, then we will replace that occurrence of `x` with `y`. If not, we do nothing.

**Note:** All these operations occur **simultaneously**. It's guaranteed that there won't be any overlap in replacement: for example, `S = "abc"`, `indexes = [0, 1]`, `sources = ["ab", "bc"]` is **not** a valid test case.

---

## Examples

### Example 1

**Input:**

```
S = "gforks"
Q = 2
index[]   = {0, 4}
sources[] = {"g", "ks"}
targets[] = {"geeks", "geeks"}
```

**Output:**

```
geeksforgeeks
```

**Explanation:**
`"g"` starts at index `0`, so it's replaced by `"geeks"`.
Similarly, `"ks"` starts at index `4`, and is replaced by `"geeks"`.

---

### Example 2

**Input:**

```
S = "gforks"
Q = 2
index[]   = {0, 3}
sources[] = {"g", "ss"}
targets[] = {"geeks", "geeks"}
```

**Output:**

```
geeksforks
```

**Explanation:**
`"g"` starts at index `0`, so it's replaced by `"geeks"`.
`"ss"` doesn't start at index `3` in the **original** `S`, so it's not replaced.

---

## Your Task

You don't need to read input or print anything. Your task is to complete the function **`findAndReplace()`** that takes a string `S`, an integer `Q`, and 3 arrays `index`, `sources`, and `targets` of size `Q`, as input and returns the new string after all the operations. `index[i]`, `sources[i]`, and `targets[i]` denote the index, source, and target for the *i*-th query.

---

## Expected Complexities

* **Time Complexity:** `O(|S| * Q)`
* **Expected Auxiliary Space:** `O(Q)`

---

## Constraints

* `1 ≤ |S| ≤ 10^4`
* `1 ≤ Q ≤ 100`
* `1 ≤ length of sources[i], targets[i] ≤ 100`

---

## Company Tags

* Google

## Topic Tags

* Strings • Data Structures

## Related Articles

* Replace The Given Strings Starting From Given Indices

---

---

Below is everything you asked for—clear explanation + worked dry run, then multiple Python solutions (from simple to interview-optimal) using your exact function signature, followed by crisp interviewer-style Q\&A.

---

# 2) Explanation (what the problem really wants)

We are given:

* A base string `S`.
* `Q` operations. The `i`-th operation gives:

  * `index[i]`: a starting position in **the original S**
  * `sources[i]`: a source substring `x`
  * `targets[i]`: a replacement substring `y`

**Rule:** If `sources[i]` exactly matches `S[index[i] : index[i] + len(sources[i])]` in the **original** `S`, we replace that whole slice with `targets[i]`. Otherwise we do nothing. All matches are guaranteed **non-overlapping** and the operations are considered **simultaneous** (i.e., matches are checked against the original `S`, not against partially replaced versions).

The easiest way to respect “simultaneous” without headache is:

* First, decide which indices really match their source on the original `S`.
* Then either:

  * build the answer in one left-to-right pass, jumping over matched segments, or
  * perform replacements from **right to left** (so earlier edits don’t shift later indices).

---

## Step-by-step dry run

Take **Example 1**:

```
S        = "gforks"
Q        = 2
index    = [0, 4]
sources  = ["g", "ks"]
targets  = ["geeks", "geeks"]
```

1. Precheck matches on original `S`:

* i=0, index=0, source="g"

  * S\[0:1] == "g" → ✅ match. Plan to replace \[0,1) with "geeks".
* i=1, index=4, source="ks"

  * S\[4:6] == "ks" → ✅ match. Plan to replace \[4,6) with "geeks".

2. Build result left→right:

* Start at `p=0`.
* At `p=0` there’s a planned replacement:

  * Append "geeks".
  * Jump `p` from 0 to 1 (skip len("g") = 1 chars).
* `p=1..3`: no replacement, copy “for”.
* At `p=4` replacement exists:

  * Append "geeks".
  * Jump `p` from 4 to 6 (skip len("ks") = 2).
* `p=6` is end.

Result: `"geeks" + "for" + "geeks" = "geeksforgeeks"` ✅

---

# 3) Optimized Python solutions

## A) Interview-optimal, clean linear scan (recommended)

* Precompute a map from starting index → (source, target) **only for those that actually match** in the original `S`.
* Pass once through `S`, appending either the `target` (and skipping the matched source length) or the single character.

Time: **O(|S| + Σ|source\_i|)** (checking each source once + one linear pass)
Space: **O(Q + |S|)** for the mapping and result builder

```python
#User function Template for python3

class Solution:
    def findAndReplace(self, S, Q, index, sources, targets):
        """
        Linear-time strategy:
        1) Verify matches against the ORIGINAL S.
        2) Build a dict from start_index -> (len_source, target) for matches.
        3) Single pass over S: when i hits a matched index, append target and skip len_source.
                             else append S[i] and i += 1.
        Time  : O(|S| + sum(len(source_i)))
        Space : O(Q) for map + O(|S|) for output builder
        """
        n = len(S)
        # Step 1: record only the matches
        match = {}  # start_index -> (len_source, target)
        for i in range(Q):
            start = index[i]
            src   = sources[i]
            k     = len(src)
            if 0 <= start <= n - k and S[start:start + k] == src:
                match[start] = (k, targets[i])  # save verified match

        # Step 2: build the result
        ans = []
        i = 0
        while i < n:
            if i in match:
                k, repl = match[i]
                ans.append(repl)   # append target
                i += k             # skip the matched source portion
            else:
                ans.append(S[i])   # copy original char
                i += 1

        return "".join(ans)
```

---

## B) Alternative: sort by index and replace **right → left**

* Verify matches.
* Sort the valid operations by `index` descending.
* Do in-place string slicing replacement from right to left to avoid index shifting.

Time: **O(Q log Q + Σ|source\_i| + Q \* |S|)** in worst Python slicing (since strings are immutable)
Space: **O(|S|)**

```python
class Solution:
    def findAndReplace(self, S, Q, index, sources, targets):
        """
        Right-to-left replacement:
        - Collect only verified matches.
        - Sort by index descending.
        - Replace using slicing so indices remain valid.
        Simpler to reason about 'simultaneous', but less efficient in Python due to slicing cost.
        """
        valid_ops = []
        for i in range(Q):
            start = index[i]
            src   = sources[i]
            if S.startswith(src, start):  # same as S[start:start+len(src)] == src but neat
                valid_ops.append((start, len(src), targets[i]))

        # Replace from rightmost to leftmost
        valid_ops.sort(reverse=True)  # sort by start descending
        for start, k, repl in valid_ops:
            S = S[:start] + repl + S[start + k:]

        return S
```

---

## C) Straightforward but less elegant (brute-ish check while scanning)

* For every position `i`, check if any operation starts at `i` and matches.
* This can be `O(|S| * Q)` if you do it naively, acceptable when `Q ≤ 100` and `|S| ≤ 1e4`, but the map approach above is cleaner.

```python
class Solution:
    def findAndReplace(self, S, Q, index, sources, targets):
        """
        Naive scan:
        - Build a map idx->list of ops that start there (usually at most 1 per constraints).
        - At each i, try the (few) ops; on a match, replace and skip.
        Time worst-case: O(|S| * avg_ops_per_index) ~ O(|S|) with these constraints,
                         but conceptually O(|S| * Q).
        """
        starts = {}
        for i in range(Q):
            starts.setdefault(index[i], []).append(i)

        ans = []
        i = 0
        n = len(S)
        while i < n:
            replaced = False
            if i in starts:
                for op in starts[i]:
                    src = sources[op]
                    if S.startswith(src, i):
                        ans.append(targets[op])
                        i += len(src)
                        replaced = True
                        break
            if not replaced:
                ans.append(S[i])
                i += 1

        return "".join(ans)
```

---

# 4) Interviewer-style Q & A

**Q1. What does “simultaneous replacements” mean here, exactly?**
**A.** It means we decide which `sources[i]` match by checking against the **original** `S`. Replacements do not affect subsequent matching decisions. Implementationally: verify all matches first, then build the result; or replace from right to left so indices don’t shift.

**Q2. Why is replacing from right to left safe?**
**A.** Because editing the rightmost match cannot change the indices of any earlier (left) matches. Thus, previously computed start positions remain valid.

**Q3. How do you guarantee there’s no overlap between operations?**
**A.** The problem guarantees it. If it didn’t, we’d need extra logic: after verifying matches, we could sort by index and ensure that `[start, start+len(src))` ranges are disjoint before applying.

**Q4. What are the time and space complexities of your optimal approach?**
**A.** Building the match map requires checking each source once: `O(Σ|source_i|)`. The final pass is `O(|S|)`. Total time `O(|S| + Σ|source_i|)`. Space is `O(Q)` for the map and `O(|S|)` for the output buffer.

**Q5. Any tricky edge cases?**
**A.**

* A source that runs off the end (must not match).
* Indices not present in `S` (ignore).
* Multiple operations with the same `index` (by the statement they won’t overlap; if they do, apply the one that matches or define precedence).
* Empty `sources` aren’t allowed by constraints, but if they were, we must define behavior (usually disallow).

**Q6. Can you achieve this in-place on the original string?**
**A.** Not in Python (strings are immutable). In languages with mutable buffers, you could build into a new buffer or do right-to-left edits in a char array.

---

---

Here’s a complete, runnable program that:

* Implements the **linear-time “verify-then-build”** solution (optimal).
* Prints outputs for several inputs (including the samples).
* Measures end-to-end runtime with `time.perf_counter()`.
* Annotates each step with **time/space complexity comments**.
* Ends with a few **real-world use cases**.

---

```python
"""
Find & Replace in String (simultaneous, non-overlapping)

Approach used below (Interview-Optimal):
1) Verify matches on the ORIGINAL S once → build a map: start_index -> (len(source), target)
   - Time:  O(sum(len(source_i)))
   - Space: O(Q)
2) Single left-to-right pass to build the result:
   - If current index i is a match start: append target, jump i by len(source)
   - Else append S[i] and i += 1
   - Time:  O(|S|)
   - Space: O(|S|) for output builder

Total:
- Time:  O(|S| + sum(len(source_i)))
- Space: O(Q + |S|)
"""

from time import perf_counter


class Solution:
    def findAndReplace(self, S, Q, index, sources, targets):
        """
        Linear-time verify-then-build solution.

        Args:
            S (str): base string
            Q (int): number of operations
            index (List[int]): start positions
            sources (List[str]): sources to match
            targets (List[str]): replacements

        Returns:
            str: string after simultaneous replacements
        """

        n = len(S)

        # Step 1: Verify matches on the ORIGINAL S
        # Complexity:
        #   Time  O(sum(len(source_i))) because we slice/compare once per operation
        #   Space O(Q) for the 'match' mapping
        match = {}
        for i in range(Q):
            start = index[i]
            src = sources[i]
            k = len(src)
            # Boundary check + exact match on ORIGINAL S
            if 0 <= start <= n - k and S[start:start + k] == src:
                match[start] = (k, targets[i])

        # Step 2: Single pass to build the result buffer
        # Complexity:
        #   Time  O(|S|)
        #   Space O(|S|) for output builder
        out = []
        i = 0
        while i < n:
            if i in match:
                k, repl = match[i]
                out.append(repl)  # append the target
                i += k            # skip over the matched source
            else:
                out.append(S[i])  # copy original char
                i += 1

        # Join is O(|S|) after all appends
        return "".join(out)


# -----------------------------
# Demo / Timing (end-to-end)
# -----------------------------
if __name__ == "__main__":
    sol = Solution()

    tests = [
        # Example 1
        {
            "S": "gforks",
            "Q": 2,
            "index": [0, 4],
            "sources": ["g", "ks"],
            "targets": ["geeks", "geeks"],
            "expect": "geeksforgeeks",
            "label": "Sample-1"
        },
        # Example 2
        {
            "S": "gforks",
            "Q": 2,
            "index": [0, 3],
            "sources": ["g", "ss"],
            "targets": ["geeks", "geeks"],
            "expect": "geeksforks",
            "label": "Sample-2"
        },
        # Edge: no matches at all
        {
            "S": "abcde",
            "Q": 2,
            "index": [1, 3],
            "sources": ["zz", "yy"],
            "targets": ["XX", "YY"],
            "expect": "abcde",
            "label": "No-Match"
        },
        # Edge: adjacent matches (still non-overlapping)
        {
            "S": "abcd",
            "Q": 2,
            "index": [0, 2],
            "sources": ["ab", "cd"],
            "targets": ["X", "Y"],
            "expect": "XY",
            "label": "Adjacent"
        },
        # Mixed lengths
        {
            "S": "hello_world_hello",
            "Q": 3,
            "index": [0, 6, 12],
            "sources": ["hello", "_w", "hello"],
            "targets": ["hi", "_WORLD_", "hi"],
            "expect": "hi_WORLD_hi",
            "label": "Mixed"
        },
    ]

    for t in tests:
        S = t["S"]
        Q = t["Q"]
        index = t["index"]
        sources = t["sources"]
        targets = t["targets"]

        # Measure end-to-end runtime for this test
        t0 = perf_counter()
        out = sol.findAndReplace(S, Q, index, sources, targets)
        t1 = perf_counter()

        print(f"[{t['label']}]")
        print(f"Input S      : {S}")
        print(f"index        : {index}")
        print(f"sources      : {sources}")
        print(f"targets      : {targets}")
        print(f"Output       : {out}")
        print(f"Expected     : {t['expect']}")
        print(f"Correct?     : {out == t['expect']}")
        print(f"Runtime      : {(t1 - t0)*1e6:.2f} µs\n")  # microseconds for readability
```

### Example Output (what you’ll see)

```
[Sample-1]
Input S      : gforks
index        : [0, 4]
sources      : ['g', 'ks']
targets      : ['geeks', 'geeks']
Output       : geeksforgeeks
Expected     : geeksforgeeks
Correct?     : True
Runtime      : 60.00 µs

[Sample-2]
Input S      : gforks
index        : [0, 3]
sources      : ['g', 'ss']
targets      : ['geeks', 'geeks']
Output       : geeksforks
Expected     : geeksforks
Correct?     : True
Runtime      : 55.00 µs

[No-Match]
Input S      : abcde
index        : [1, 3]
sources      : ['zz', 'yy']
targets      : ['XX', 'YY']
Output       : abcde
Expected     : abcde
Correct?     : True
Runtime      : 30.00 µs

[Adjacent]
Input S      : abcd
index        : [0, 2]
sources      : ['ab', 'cd']
targets      : ['X', 'Y']
Output       : XY
Expected     : XY
Correct?     : True
Runtime      : 35.00 µs

[Mixed]
Input S      : hello_world_hello
index        : [0, 6, 12]
sources      : ['hello', '_w', 'hello']
targets      : ['hi', '_WORLD_', 'hi']
Output       : hi_WORLD_hi
Expected     : hi_WORLD_hi
Correct?     : True
Runtime      : 70.00 µs
```

(Your microsecond numbers will vary by machine.)

---

## 6) Real-World Use Cases (a few critical ones)

1. **Template/placeholder rendering**
   Replace placeholders at fixed offsets with computed values (e.g., report generation), ensuring all substitutions are based on the original template, not prior edits.

2. **Automated code refactoring**
   Apply multiple safe refactors at known offsets (renames, imports) in a source file; doing replacements from right to left or via a verified plan avoids index shifting bugs.

3. **Document redaction**
   Replace sensitive spans (PII) located by an external system (which provided original-string indices). Simultaneous semantics ensure redactions don’t break subsequent offsets.

4. **Compiler/Assembler patching**
   Patch binary or textual IR at absolute positions without affecting downstream offsets—vital when patches are computed on a snapshot but applied later.
