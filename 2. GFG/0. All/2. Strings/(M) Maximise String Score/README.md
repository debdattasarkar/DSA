# Maximise String Score 🧵

**Difficulty:** Medium  
**Accuracy:** 0.0%  
**Submissions:** 4+  
**Points:** 4  

---

## Problem Statement

You are given a string **s**, and a list of **jumps[][]** of size **n**, where each `jumps[i] = [s1, s2]` denotes that you are allowed to **jump from character `s1` to `s2` in the forward direction**.

Additionally, you are allowed to **jump forward from a character to any other occurrence of the same character** within the string.

You start at **index 0** of the string. After every valid jump from index `i` to index `j`, where `s[i] = s1` and `s[j] = s2`, you earn a score equal to the **sum of ASCII values of all characters between the jump except for the characters equal to `s2`**, i.e.

\[
\text{score}(i, j) = \sum \text{ascii}(s[k]) \quad \text{for } i \le k < j \text{ and } s[k] \ne s[j]
\]

Determine the **maximum score** that can be achieved by performing a sequence of **valid jumps** starting from index 0.

---

## Examples

### Example 1

**Input:**  
`s = "forgfg"`, `jumps[][] = [['f', 'r'], ['r', 'g']]`  

**Output:**  
`429`  

**Explanation:**  

- We can jump from `'f'` to `'r'` at index 2.  
  This gives a score equal to the sum of ASCII values of `'f'`, `'o'`, i.e. **213**.  
- Now we can jump from `'r'` to `'g'` at index 5.  
  This gives a score equal to the sum of ASCII values of `'r'`, `'f'`, i.e. **216**.  

Hence the **maximum total score** obtained will be `213 + 216 = 429`.

---

### Example 2

**Input:**  
`s = "abcda"`, `jumps[][] = [['b', 'd']]`  

**Output:**  
`297`  

**Explanation:**  

We can jump from `'a'` to `'a'` (as both are the same character) at index 4.  
This gives a score equal to the sum of ASCII values of `'b'`, `'c'`, `'d'`, i.e. **297**.  

Hence the **maximum total score** obtained will be `297`.

---

## Constraints

- \( 1 \le |s| \le 2 \times 10^5 \)  
- \( 1 \le \text{jumps.size()} \le 676 \)  
- There are **at least two distinct characters** in `s`.

---

## Expected Complexities

- **Time Complexity:** `O(26 * n)`  
- **Auxiliary Space:** `O(26 * n)`

---

## Topic Tags

- prefix-sum  
- Strings  
- Dynamic Programming  

---

---

I’ll follow your numbering: explanation + dry run → brute + optimized Python → interview memory + Q&A.

---

## 2. Explanation + Step-by-Step Dry Run

### Problem in my own words

* We have a string `s` (lowercase letters).
* We start at **index 0**.
* We can do **forward jumps**:

  * From char `s1` to char `s2` if `[s1, s2]` is in `jumps`.
  * From a char to **the same char** anywhere later in the string (always allowed).
* A jump goes from index `i` to index `j` (`i < j` and the characters match the rule).
* Score of this jump:

[
score(i, j) = \sum_{k=i}^{j-1} \text{ASCII}(s[k]) \quad \text{ignoring positions where } s[k] = s[j]
]

* We can make many jumps; total score is the sum of scores of all jumps.
* We want the **maximum possible total score**.

Think of indices `0..n-1` as nodes in a DAG; a jump is a directed edge forward with some positive weight. We want the **maximum path sum** starting at node 0.
Naively, there can be `O(n²)` edges → too slow for `n = 2 * 10^5`.

---

### Key observations

1. **Score of one jump depends only on the substring and target char**

For jump `i → j` with `c = s[j]`:

```text
score(i, j) = sum of ASCII(s[i..j-1]) - ASCII(c) * (# of c's in s[i..j-1])
```

If we know:

* `prefix_ascii[i] = sum ASCII(s[0..i-1])`
* `prefix_count[c][i] = count of character c in s[0..i-1]`

then:

```text
sum_ascii(i..j-1) = prefix_ascii[j] - prefix_ascii[i]
cnt_c(i..j-1)      = prefix_count[c][j] - prefix_count[c][i]

score(i, j) = (prefix_ascii[j] - prefix_ascii[i]) \
             - (prefix_count[c][j] - prefix_count[c][i]) * ASCII(c)
```

2. **Dynamic Programming on destination index**

Let `dp[j]` = maximum total score when we **land** on index `j`.

For every allowed jump `i → j`:

```text
dp[j] = max(dp[j], dp[i] + score(i, j))
```

But doing this over all `i < j` is still `O(n²)`. We need to reorganize using the fact there are only **26 letters** and at most `26 * 26` jump pairs.

---

### Magic algebra trick

For a fixed destination index `j` with character `c = s[j]`:

```text
dp[j] = max over allowed i<j of:
        dp[i] + (prefix_ascii[j] - prefix_ascii[i]) \
              - (prefix_count[c][j] - prefix_count[c][i]) * ASCII(c)
```

Rearrange terms that depend on `j` and those that depend on `i`:

```text
dp[j] = prefix_ascii[j] - prefix_count[c][j] * ASCII(c) \
        + max over allowed i<j of [ dp[i] - prefix_ascii[i] \
                                    + prefix_count[c][i] * ASCII(c) ]
```

For a **fixed target character c**, the term in brackets depends only on `i` and `c`, not `j`.

So when scanning the string left→right, we can maintain for each character `c`:

```text
best_for_target[c] = max over all earlier i that can jump to c of
                     dp[i] - prefix_ascii[i] + prefix_count[c][i] * ASCII(c)
```

Then for any position `j` with character `c`, we can compute:

```text
dp[j] = prefix_ascii[j] - prefix_count[c][j] * ASCII(c) + best_for_target[c]
```

in **O(1)**.

We just need to keep `best_for_target` updated as we progress.

3. **Which targets can we jump to from a given character?**

For each character `a`, we have a list `allowed_targets[a]`:

* It **always includes `a` itself** (same-character jumps).
* For every pair `[s1, s2]` in the given `jumps`, add `s2` to `allowed_targets[s1]`.

When we’re at index `i` with character `s[i] = a`, we update `best_for_target[t]` for **every `t` in `allowed_targets[a]`** using the expression above.

Since there are at most 26 targets per letter, and 26 letters total, this is `O(26 * n)`.

4. **We can do this streaming, without full prefix arrays**

As we scan from left to right,

* maintain `ascii_sum_so_far` = sum ASCII(s[0..i-1])
* maintain `count_char[c]` = # of character `c` in s[0..i-1]

At index `i`, those are exactly `prefix_ascii[i]` and `prefix_count[*][i]`.
So we don’t need arrays `O(26*n)`; just O(26) variables updated on the fly.

---

### Step-by-step dry run – `s = "forgfg"`, `jumps = [['f','r'], ['r','g']]`

ASCII values we need:

* `'f'` = 102, `'o'` = 111, `'r'` = 114, `'g'` = 103

Also remember: we can always jump from a char to **same char** later.

We’ll track:

* `ascii_sum` (prefix sum before current index)
* `count_char[letter]` (prefix counts)
* `best_for_target[c]` (for each character `c`)
* `dp[i]`

Initialize:

```text
ascii_sum = 0
count_char[*] = 0
best_for_target[*] = -∞
dp[*] = -∞
dp[0] = 0  (start at index 0 with score 0)
```

We also precompute `allowed_targets`:

* From `'f'`: `['f', 'r']`
* From `'r'`: `['r', 'g']`
* Others: only themselves.

---

#### Index 0: char 'f'

* `ascii_sum` = 0, `count_char` all 0.

We start at 0 with score 0 (`dp[0] = 0` by definition).
Use index 0 to update `best_for_target` for its allowed targets (`'f'` and `'r'`):

For each target `t` in `['f', 'r']`:

```text
candidate = dp[0] - ascii_sum + count_char[t] * ASCII(t)
          = 0 - 0 + 0 = 0
best_for_target[t] = max(-∞, 0) = 0
```

Now:

```text
best_for_target['f'] = 0
best_for_target['r'] = 0
```

Update prefix:

```text
ascii_sum += ASCII('f') = 102
count_char['f'] += 1
```

---

#### Index 1: char 'o'

For char `'o'`, there are no allowed jumps to `'o'` yet (`best_for_target['o'] = -∞`),
so `dp[1]` remains `-∞` (we can’t land on 1 via a valid jump).

We **do not** update `best_for_target` from here because `dp[1]` is `-∞` (unreachable).

Update prefix:

```text
ascii_sum += ASCII('o') = 102 + 111 = 213
count_char['o'] += 1
```

---

#### Index 2: char 'r'

Compute `dp[2]` using `best_for_target['r']`:

```text
c = 'r', ASCII(c) = 114
prefix_ascii = ascii_sum = 213    # sum of 'f' + 'o'
prefix_count['r'] = count_char['r'] = 0

dp[2] = 213 - 0 * 114 + best_for_target['r']
      = 213 + 0
      = 213
```

This matches “jump from index 0 (`'f'`) to index 2 (`'r'`)”:

* Between them you see `['f','o']` => 102 + 111 = 213.

Now update `best_for_target` from index 2 (`'r'` allowed to `['r', 'g']`):

For each target `t` in `['r', 'g']`:

```text
candidate = dp[2] - ascii_sum + count_char[t] * ASCII(t)
          = 213 - 213 + count_char[t] * ASCII(t)
```

* `t = 'r'`: `count_char['r'] = 0` → candidate = 0 → `best_for_target['r']` stays 0.
* `t = 'g'`: `count_char['g'] = 0` → candidate = 0 → `best_for_target['g'] = 0`.

Update prefix:

```text
ascii_sum += ASCII('r') = 213 + 114 = 327
count_char['r'] += 1
```

---

#### Index 3: char 'g'

Compute `dp[3]` via `best_for_target['g']`:

```text
c = 'g', ASCII(c) = 103
prefix_ascii = ascii_sum = 327      # 'f' + 'o' + 'r'
prefix_count['g'] = 0

dp[3] = 327 - 0 * 103 + best_for_target['g']
      = 327 + 0 = 327
```

This corresponds to chain: 0 `'f'` → 2 `'r'` → 3 `'g'`
Score:

* 0→2: `'f','o'` = 213
* 2→3: in-between `'r'` = 114
  Total = 327 ✔

We then update `best_for_target` from `'g'` (but no special jumps from `'g'` except `'g'`→`'g'`). I’ll skip those details; the final answer for string is `429` when we go to index 5, matching the example.

(We eventually jump further to the last `'g'`, accumulating the optimal score → 429.)

---

## 3. Python Solutions

### 3.1 Brute Force DP (O(n²) – for understanding)

```python
class Solution:
    def maxScore_bruteforce(self, s, jumps):
        """
        Brute-force DP:
        - Build all forward edges i -> j where:
              * s[i] == s[j]   OR
              * (s[i], s[j]) is in jumps list
        - For each edge compute its score by scanning substring.
        - Run DP on this DAG: dp[j] = max over incoming i of dp[i] + score(i, j).

        Time complexity  (very rough worst-case):
            - For each pair (i, j) we might scan substring => O(n^3).
            - Even with prefix sums it's at least O(n^2) edges.
        Space complexity:
            - O(n^2) if we explicitly store all edges.
        This is mainly for conceptual understanding, not for large constraints.
        """
        n = len(s)

        # Map jumps into a fast lookup set
        allowed_pair = set()
        for c1, c2 in jumps:
            allowed_pair.add((c1, c2))

        # Precompute ASCII prefix sums to speed up scoring
        prefix_ascii = [0] * (n + 1)
        for i, ch in enumerate(s):
            prefix_ascii[i + 1] = prefix_ascii[i] + ord(ch)

        def jump_score(i, j):
            # score(s[i -> j]) ignoring characters equal to s[j]
            target = s[j]
            total = prefix_ascii[j] - prefix_ascii[i]
            subtract = 0
            for k in range(i, j):
                if s[k] == target:
                    subtract += ord(target)
            return total - subtract

        # DP over all indices
        NEG_INF = float("-inf")
        dp = [NEG_INF] * n
        dp[0] = 0  # start at index 0 with score 0

        for j in range(1, n):
            for i in range(0, j):
                if s[i] == s[j] or (s[i], s[j]) in allowed_pair:
                    dp[j] = max(dp[j], dp[i] + jump_score(i, j))

        return max(0, max(dp))
```

Again: too slow for real constraints, but clarifies the problem structure.

---

### 3.2 Optimized O(26·n) DP (streaming with per-letter “best”)

This is the version you want in interviews.

```python
class Solution:
    def maxScore(self, s, jumps):
        """
        Optimized solution using per-character DP and streaming prefix data.

        Idea:
        - Let dp[i] be the best score when we land at index i.
        - For character c at index j, we can show:

            dp[j] = prefix_ascii(j) - count_c(j) * ASCII(c)
                    + best_for_target[c]

          where best_for_target[c] is:

            best_for_target[c] = max over earlier indices i that can jump to c of    
                                 dp[i] - prefix_ascii(i)
                                 + count_c(i) * ASCII(c)

        - While we scan the string left to right, we maintain:
            * ascii_sum: sum ASCII of characters before current index
            * count_char[26]: frequency of each letter before current index
            * best_for_target[26]: value above for each letter as target

        - For each index i:
            1. Compute dp[i] from best_for_target[ s[i] ].
            2. Use dp[i] to update best_for_target for all characters that
               can be jumped TO from s[i].
            3. Update ascii_sum and count_char with s[i].

        Complexity:
            Let B = 26 (letters)

            - For each of n indices:
                * O(1) work to compute dp[i]
                * O(#allowed_targets) ≤ O(26) work to update best_for_target
            => O(B * n) time  (≈ O(n)).
            - Space: O(B) for best_for_target + O(B) for counts + O(n) for dp.
              So O(B + n) auxiliary space.
        """

        n = len(s)
        if n == 0:
            return 0

        # Helper to map 'a'..'z' -> 0..25
        def char_index(ch):
            return ord(ch) - ord('a')

        # ---------- Build allowed target list for each source character ----------
        # Start with self-jumps: char -> same char
        allowed_targets_from = [[] for _ in range(26)]
        for c in range(26):
            allowed_targets_from[c].append(c)

        # Add directed jumps from input list
        for c1, c2 in jumps:
            i1 = char_index(c1)
            i2 = char_index(c2)
            allowed_targets_from[i1].append(i2)

        # ---------- DP and helpers ----------
        NEG_INF = -10**18

        # best_for_target[c]: the "bracket" term for character c as target
        best_for_target = [NEG_INF] * 26

        # prefix info (before current index)
        ascii_sum = 0                     # sum of ASCII of s[0..i-1]
        count_char = [0] * 26             # count_char[c] = # of c in s[0..i-1]

        # dp[i]: best score when landing at index i
        dp = [NEG_INF] * n

        # ---------- Handle index 0 specially ----------
        dp[0] = 0  # we start at index 0 with score 0

        idx0 = char_index(s[0])

        # index 0 can be a start of jumps to all its allowed targets
        for tgt in allowed_targets_from[idx0]:
            # Here ascii_sum = 0, count_char[*] = 0
            cand = dp[0] - ascii_sum + count_char[tgt] * ord(chr(tgt + ord('a')))
            if cand > best_for_target[tgt]:
                best_for_target[tgt] = cand

        # Update prefix after index 0
        ascii_sum += ord(s[0])
        count_char[idx0] += 1

        # ---------- Process remaining indices 1..n-1 ----------
        for i in range(1, n):
            current_char = s[i]
            c_idx = char_index(current_char)
            ascii_c = ord(current_char)

            # Step 1: compute dp[i] if there is any valid way to land here
            if best_for_target[c_idx] != NEG_INF:
                dp[i] = (
                    ascii_sum
                    - count_char[c_idx] * ascii_c
                    + best_for_target[c_idx]
                )
                # otherwise stays NEG_INF (unreachable)

            # Step 2: use dp[i] to update future best_for_target values
            if dp[i] != NEG_INF:
                for tgt in allowed_targets_from[c_idx]:
                    target_char_ascii = ord(chr(tgt + ord('a')))
                    cand = (
                        dp[i]
                        - ascii_sum
                        + count_char[tgt] * target_char_ascii
                    )
                    if cand > best_for_target[tgt]:
                        best_for_target[tgt] = cand

            # Step 3: update prefix information for next iteration
            ascii_sum += ascii_c
            count_char[c_idx] += 1

        # We can always choose to make no jumps, so answer is at least 0
        best_score = max(0, max(dp))
        return best_score
```

This is interview-ready: clear variables, step-by-step DP, and good complexity.

---

## 4. Interview Memory Tricks + Likely Q&A

### Quick memory hook

Two short phrases:

1. **“Edge score = sum − target_count * ASCII(target)”**
   → Remember how to get score(i, j) using prefix sums and counts.

2. **“For each target char c, keep best bracket value”**
   → The bracket is:

[
\text{best_for_target[c]} = \max (dp[i] - prefix_ascii(i) + count_c(i) * ASCII(c))
]

Then:

[
dp[j] = prefix_ascii(j) - count_c(j) * ASCII(c) + best_for_target[c]
]

And we update `best_for_target` for all `t` reachable from current char.

Once you know those two formulas, the code flows naturally.

---

### 5-line pseudo-code template

```text
build allowed_targets_from for each char (include self)
init best_for_target[c] = -INF, dp[0] = 0
for i from 0..n-1 (maintain ascii_sum, count_char):
    if i > 0: dp[i] = ascii_sum - count_char[c]*ASCII(c) + best_for_target[c]
    for each t in allowed_targets_from[c]:
        best_for_target[t] = max(best_for_target[t],
                                 dp[i] - ascii_sum + count_char[t]*ASCII(t))
    update ascii_sum, count_char with s[i]
answer = max(0, max(dp))
```

That’s the “skeleton” you can re-create quickly in any language.

---

### Likely Interview Questions & Answers

---

**Q1: What’s the brute-force approach and its complexity?**

**A:**
Try all pairs `i < j`. For each pair, check if jump `i → j` is allowed (same character or in `jumps`). If yes, compute `score(i, j)` by scanning the substring and run DP over this DAG. This leads to at least `O(n²)` edges and `O(n²)`–`O(n³)` time (depending on whether we use prefix sums). That’s too slow for `n = 2 * 10^5`.

---

**Q2: What’s the high-level idea of your optimized solution?**

**A:**
I treat it as DP on indices but use algebra + character grouping to avoid `O(n²)`. For each character `c`, I maintain a value `best_for_target[c]` summarizing the best previous landing index we can jump from to `c`. Using prefix sums and prefix counts, I can compute the best score to land at `j` with character `c` in O(1). Then I update `best_for_target` for all characters that can be jumped to from the current character.

---

**Q3: Can you derive the recurrence for `dp[j]`?**

**A:**

For a destination `j` with char `c = s[j]`:

[
dp[j] = \max_{i<j, i→j allowed} \left( dp[i] + score(i, j) \right)
]

with

[
score(i, j) = (\text{prefix_ascii}[j] - \text{prefix_ascii}[i])
- (\text{prefix_count}_c[j] - \text{prefix_count}_c[i]) \cdot ASCII(c)
]

Rewriting:

[
dp[j] = \text{prefix_ascii}[j] - \text{prefix_count}*c[j]\cdot ASCII(c)
+ \max*{i} \left( dp[i] - \text{prefix_ascii}[i]
+ \text{prefix_count}_c[i]\cdot ASCII(c) \right)
]

The max term depends only on `c` and previous positions, so I maintain it as `best_for_target[c]`.

---

**Q4: How do you update `best_for_target`?**

**A:**
When I’ve computed `dp[i]` for index `i` with char `a = s[i]`, I know this index can be the start of future jumps to certain target characters `t` (from `allowed_targets_from[a]`). For each such `t`:

[
best_for_target[t] = \max\left(best_for_target[t],
dp[i] - prefix_ascii[i]
+ prefix_count_t[i]\cdot ASCII(t)\right)
]

I compute this in `O(1)` per target, and there are at most 26 targets.

---

**Q5: Why do you say the complexity is O(26 · n)?**

**A:**
For each of the `n` characters in the string:

* Computing `dp[i]` is O(1).
* Updating `best_for_target` requires looping over all allowed targets from the current char. Each list has size ≤ 26 (self + possible 26 jump pairs). So each index costs O(26). Overall complexity is `O(26 * n)`, which is linear in `n` with a small constant factor.

Space is `O(26)` for per-letter arrays plus O(n) for `dp`.

---

**Q6: Why do you handle index 0 differently?**

**A:**
We start at index 0 with score 0 without needing to land there via a jump. So I set `dp[0] = 0` manually and immediately use index 0 to update `best_for_target` for all its possible outgoing characters. All other indices are reached through the general DP formula.

---

If you can remember:

> **“Jump score = sum − count*ASCII, and for each target char keep a running best bracket.”**

you’ll be able to reproduce the recurrence, explain the optimization, and write the code confidently in an interview.

---

---

Alright, let’s finish this problem properly.

---

## 5. Real-World Use Cases (few, but interview-friendly)

You can map this “max string score with jumps” to a few real problems:

1. **Workflow / Pipeline Optimization with Constraints**

   * Think of each character as a *task type* (A, B, C, …).
   * `jumps[i] = [s1, s2]` means: from a task of type `s1` we’re allowed to jump forward to a task of type `s2`.
   * The “score between i and j” is like collecting revenue/benefit from the intermediate tasks you “pass through”.
   * Goal = choose a sequence of allowed task transitions to **maximize total benefit**.
   * This matches scheduling / pipeline optimization with type-based transitions.

2. **Game Level / Checkpoint Path Planning**

   * String positions = checkpoints in a level; character = type of checkpoint (e.g., enemy, heal, treasure).
   * Jumps represent allowed teleports (e.g., teleport from `f` to `r`, or warp to another same-type checkpoint).
   * Score of a jump = total value of things you collect on the way, ignoring some types (target char).
   * Task: find a sequence of teleports to **maximize collected reward**.

3. **Log Analysis with Pattern Skips**

   * String = sequence of log-event categories (letters).
   * Jumps encode allowed “quick skips” an analyst/tool can make (e.g., from `ERROR` to next `WARN` or same `ERROR`).
   * Score = weight/importance of events you *scan through* between two key events.
   * We want the best sequence of skips that **captures the most important in-between information**.

4. **DNA / Protein Motif Skipping**

   * Characters = nucleotides/amino acids.
   * Jumps define allowed motif transitions or same-motif repetition.
   * Score between two motifs = sum of “importance” of bases between them except the final motif type.
   * Helps model certain motif scoring / path selection in sequence analysis.

Mentioning one or two of these (workflow + game) is usually enough to convince the interviewer you can connect DP/string problems to real systems.

---

## 6. Full Python Program (with timing + detailed complexity comments)

This uses the optimized `O(26 * n)` DP we discussed.

```python
import time


class Solution:
    def maxScore(self, s, jumps):
        """
        Compute the maximum score of valid jumps in a string.

        Approach summary:
        - Let dp[i] be the best score when we LAND on index i.
        - A jump i -> j (i < j) is allowed if:
              * s[i] == s[j]                     (same-char jump) OR
              * [s[i], s[j]] present in jumps[]  (explicit jump)
        - Score(i, j) = sum ASCII(s[k]) for k in [i..j-1] where s[k] != s[j].
        - Using prefix sums and counts, this score can be rewritten so that:

            dp[j] = prefix_ascii(j)
                     - count_of_sj(j) * ASCII(s[j])
                     + best_for_target[s[j]]

          where best_for_target[c] is a precomputed value that summarizes all
          possible previous landing positions that can jump TO character c.

        - As we scan s left to right, we maintain:
            ascii_sum      = sum ASCII(s[0..i-1])
            count_char[c]  = count of character c in s[0..i-1]
            best_for_target[c] for each character c

        - For each i we:
            1) compute dp[i] using best_for_target[ s[i] ]
            2) update best_for_target for ALL characters we can jump TO from s[i]
            3) update ascii_sum and count_char with s[i]

        Complexity:
            Let n = len(s), ALPHA = 26 (letters)
            - For each of n indices:
                * O(1) to compute dp[i]
                * O(#targets_from_this_char) <= O(ALPHA) to update best_for_target
            => O(ALPHA * n) time  ~  O(n) in practice.
            - Space: O(ALPHA) for best_for_target & counts + O(n) for dp.
              => O(ALPHA + n) auxiliary space.
        """

        n = len(s)
        if n == 0:
            return 0

        # Helper: map 'a'..'z' -> 0..25
        def idx(ch):
            return ord(ch) - ord('a')

        ALPHA = 26

        # ---------- Build allowed target list for each source character ----------
        # Time: O(ALPHA + len(jumps)), Space: O(ALPHA^2) worst (<= 26*26)
        allowed_targets_from = [[] for _ in range(ALPHA)]

        # Always allow jumping from a character to itself (same-character jump)
        for c in range(ALPHA):
            allowed_targets_from[c].append(c)

        # Add the explicitly given jumps
        for c1, c2 in jumps:
            allowed_targets_from[idx(c1)].append(idx(c2))

        # ---------- DP + prefix tracking ----------
        NEG_INF = -10**18

        # best_for_target[c]: the max of
        #   dp[i] - prefix_ascii(i) + prefix_count_c(i) * ASCII(c)
        # over all i that can jump TO character c
        # Time to init: O(ALPHA), Space: O(ALPHA)
        best_for_target = [NEG_INF] * ALPHA

        # Prefix info (BEFORE current index)
        ascii_sum = 0                  # prefix_ascii(i)
        count_char = [0] * ALPHA       # prefix_count for each char

        # dp[i] = best score when we land at index i
        # Space: O(n)
        dp = [NEG_INF] * n

        # ---------- Handle index 0 specially ----------
        # We "start" at index 0 with score 0.
        # Time: O(1)
        dp[0] = 0
        c0 = idx(s[0])

        # Use index 0 to update best_for_target for every char we can jump TO.
        # Time: O(#targets_from[s[0]]) <= O(ALPHA)
        for target in allowed_targets_from[c0]:
            target_ascii = ord(chr(target + ord('a')))
            # prefix at i=0 is empty: ascii_sum = 0, count_char[*] = 0
            candidate = dp[0] - ascii_sum + count_char[target] * target_ascii
            if candidate > best_for_target[target]:
                best_for_target[target] = candidate

        # Update prefix AFTER processing index 0
        # Time: O(1)
        ascii_sum += ord(s[0])
        count_char[c0] += 1

        # ---------- Process indices 1..n-1 ----------
        # Overall Time: O(n * ALPHA)
        for i in range(1, n):
            ch = s[i]
            c_index = idx(ch)
            ascii_c = ord(ch)

            # Step 1: compute dp[i] if we can land here via some jump.
            # Time: O(1)
            if best_for_target[c_index] != NEG_INF:
                dp[i] = (
                    ascii_sum
                    - count_char[c_index] * ascii_c
                    + best_for_target[c_index]
                )
            # else dp[i] stays NEG_INF (unreachable index by valid jumps)

            # Step 2: use dp[i] to update future best_for_target values
            # only if index i is reachable.
            # Time: O(#targets_from[s[i]]) <= O(ALPHA)
            if dp[i] != NEG_INF:
                for target in allowed_targets_from[c_index]:
                    target_ascii = ord(chr(target + ord('a')))
                    candidate = (
                        dp[i]
                        - ascii_sum
                        + count_char[target] * target_ascii
                    )
                    if candidate > best_for_target[target]:
                        best_for_target[target] = candidate

            # Step 3: update prefix data for next iteration
            # Time: O(1)
            ascii_sum += ascii_c
            count_char[c_index] += 1

        # We can choose to make no jumps, so answer is at least 0.
        # Time: O(n) to scan dp
        best_score = max(0, max(dp))
        return best_score


# -------------------- Driver with Timing -------------------- #

def main():
    """
    Driver function:
    - Reads input:
          line 1: string s
          line 2: integer m (number of jumps)
          next m lines: two chars "c1 c2" representing a jump.
    - Measures time for maxScore() using time.perf_counter()
    - Prints the result and elapsed time.

    Complexity of main (excluding the algorithm itself):
    - Input reading: O(|s| + m)
    - Printing: O(1)
    """

    print("Enter string s (lowercase letters):")
    s = input().strip()

    print("Enter number of jump pairs m:")
    m = int(input().strip())

    jumps = []
    if m > 0:
        print("Enter each jump as two lowercase letters: s1 s2")
    for _ in range(m):
        parts = input().split()
        if len(parts) != 2:
            raise ValueError("Each jump line must contain exactly two characters.")
        c1, c2 = parts[0], parts[1]
        jumps.append([c1, c2])

    solver = Solution()

    # Start timing just before the core algorithm
    start = time.perf_counter()
    answer = solver.maxScore(s, jumps)
    end = time.perf_counter()

    print("\nMaximum obtainable score:", answer)
    print(f"Total elapsed time (seconds): {end - start:.6f}")


if __name__ == "__main__":
    main()
```

### Example (how a run looks)

Input (interactive):

```text
forgfg
2
f r
r g
```

Possible output:

```text
Enter string s (lowercase letters):
forgfg
Enter number of jump pairs m:
2
Enter each jump as two lowercase letters: s1 s2
f r
r g

Maximum obtainable score: 429
Total elapsed time (seconds): 0.0000xx
```

You can use this full script locally to test and profile.
In interviews / coding platforms, you just drop in the `Solution` class with `maxScore`.
