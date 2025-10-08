# 🧩 Word Ladder I

**Difficulty:** Hard
**Accuracy:** 37.65%
**Submissions:** 56K+
**Points:** 8
**Average Time:** 25m

---

## 📜 Problem Statement

Given two distinct words `startWord` and `targetWord`, and a list denoting `wordList` of unique words of equal lengths,
find the **length of the shortest transformation sequence** from `startWord` to `targetWord`.

---

### ⚙️ Keep the following conditions in mind:

1. A word can only consist of **lowercase characters**.
2. Only **one letter** can be changed in each transformation.
3. Each transformed word **must exist** in the wordList including the targetWord.
4. `startWord` may or may not be part of the `wordList`.

---

The second part of this problem can be found [here](https://www.geeksforgeeks.org/word-ladder-ii/).

> **Note:**
> If no possible way to transform sequence from `startWord` to `targetWord`, **return 0**.

---

## 🧠 Example 1

### **Input:**

```
wordList  = {"des", "der", "dfr", "dgt", "dfs"}
startWord = "der"
targetWord = "dfs"
```

### **Output:**

```
3
```

### **Explanation:**

The length of the smallest transformation sequence from `"der"` to `"dfs"` is **3**,
i.e. `"der" → "dfr" → "dfs"`.

---

## 🧠 Example 2

### **Input:**

```
wordList  = {"geek", "gefk"}
startWord = "gedk"
targetWord = "geek"
```

### **Output:**

```
2
```

### **Explanation:**

The only valid transformation is:
`"gedk" → "geek"`

---

## 🧠 Example 3

### **Input:**

```
wordList  = {"poon", "plee", "same", "poie", "plea", "plie", "poin"}
startWord = "toon"
targetWord = "plea"
```

### **Output:**

```
7
```

### **Explanation:**

The shortest transformation sequence is:

```
toon → poon → poin → poie → plie → plee → plea
```

---

## 🧩 Your Task

You don’t need to read input or print anything.
Your task is to complete the function:

```python
def wordLadderLength(self, startWord, targetWord, wordList):
    # code here
```

which takes `startWord`, `targetWord`, and `wordList` as input parameters and returns the **length of the shortest transformation sequence** from `startWord` to `targetWord`.

If not possible, return `0`.

---

## ⏱️ Expected Complexities

* **Expected Time Complexity:** `O(N² * M)`
* **Expected Auxiliary Space:** `O(N * M)`
  where
  `N = length of wordList`
  `M = |wordList[i]|`

---

## 🔢 Constraints

```
1 ≤ N ≤ 100
1 ≤ M ≤ 10
```

---

## 🏢 Company Tags

* Flipkart
* Amazon
* Adobe
* Google

---

## 📚 Topic Tags

* Graph
* BFS
* Data Structures
* Algorithms

---

## 💼 Related Interview Experiences

* Adobe Interview Experience (MTS 2 | 1.5 Years Experienced)
* Flipkart Interview Experience for SDE 1 (On Campus 2020)

---

## 🔗 Related Articles

* [Word Ladder – Length of Shortest Chain to Reach a Target Word](https://www.geeksforgeeks.org/word-ladder-length-of-shortest-chain-to-reach-a-target-word/)

---

---

Here’s everything you asked for on **Word Ladder I**—why BFS is the right tool, a worked dry-run, multiple Python solutions in interview-ready style, and a short Q&A you can expect.

---

# 2) Intuition + Step-by-Step Dry Run

## Why BFS?

Every step (change exactly one letter and keep the word in the dictionary) costs **1 move**. We want the **fewest moves** from `startWord` to `targetWord`. That is exactly the “shortest path in an unweighted graph,” so **BFS** finds the answer.

We treat each valid dictionary word (and optionally the start word) as a node. There’s an edge between two words if they differ in **exactly one** character.

## Dry run (Example 1)

```
startWord = "der"
targetWord = "dfs"
wordList  = {"des","der","dfr","dgt","dfs"}
```

### Build helper map (wildcard buckets)

For each word, replace each position with `*` and map:

* "der" → ["*er", "d*r", "de*"]
* "des" → ["*es", "d*s", "de*"]
* "dfr" → ["*fr", "d*r", "df*"]
* "dgt" → ["*gt", "d*t", "dg*"]
* "dfs" → ["*fs", "d*s", "df*"]

This lets us find neighbors (one-letter different words) in O(1) bucket lookups.

### BFS levels

* **Level 1**: start = `"der"`.
  Visited = { "der" }. Queue = [("der", dist=1)]

* Pop `"der"` (dist 1)
  Wildcards: `*er`, `d*r`, `de*`
  Neighbors via buckets:

  * `*er` → {"der"} (only itself)
  * `d*r` → {"der","dfr"} → unseen: `"dfr"`
  * `de*` → {"der","des"} → unseen: `"des"`
    Push: `("dfr",2)`, `("des",2)`; mark visited.

* **Level 2**: pop `"dfr"` (2)
  Wildcards: `*fr`, `d*r`, `df*`
  Neighbors: `"dfr"` (itself), and `"dfs"` via `df*`.
  We discover **target `"dfs"`** → return `2 + 1 = 3`.

Answer = **3** (der → dfr → dfs).
If we had popped `"des"` first, we’d still reach `"dfs"` in 3 via `des → dfs`.

---

# 3) Python Solutions (multiple flavors)

## A) Optimal & standard (BFS + wildcard buckets) — O(N·M) build + O(N·M) BFS

```python
class Solution:
    def wordLadderLength(self, startWord, targetWord, wordList):
        
```

### Why interviewers like it

* Clean BFS.
* Correctly handles “start not in list”.
* Uses buckets to avoid O(N²) neighbor checks.

---

## B) Bidirectional BFS (usually fastest in practice)

Reduces frontier size by searching from both ends. Stops when frontiers meet.

```python
class Solution:
    def wordLadderLength(self, startWord, targetWord, wordList):
        if startWord == targetWord:
            return 1
        L = len(startWord)
        wordSet = set(wordList)
        if targetWord not in wordSet:
            return 0
        wordSet.add(startWord)

        # Precompute buckets (same idea)
        from collections import defaultdict
        buckets = defaultdict(list)
        for w in wordSet:
            for i in range(L):
                buckets[w[:i] + '*' + w[i+1:]].append(w)

        # Two frontiers
        front = {startWord}
        back  = {targetWord}
        visited = {startWord, targetWord}
        level = 1

        while front and back:
            # Always expand the smaller frontier
            if len(front) > len(back):
                front, back = back, front
            level += 1
            new_front = set()

            for word in front:
                for i in range(L):
                    key = word[:i] + '*' + word[i+1:]
                    for nxt in buckets[key]:
                        if nxt in back:
                            return level
                        if nxt not in visited:
                            visited.add(nxt)
                            new_front.add(nxt)
            front = new_front

        return 0
```

**Complexity:** Same big-O as A in worst case, but often much faster due to smaller frontiers.

---

## C) Simple (but slower) BFS without buckets — O(N²·M) in worst case

This compares the current word to **all** words to find neighbors (1-letter different). Useful if an interviewer asks for the first idea you’d write before optimizing.

```python
class Solution:
    def wordLadderLength(self, startWord, targetWord, wordList):
        if startWord == targetWord:
            return 1
        from collections import deque
        def one_off(a, b):
            # Check if a and b differ by exactly one character
            diff = 0
            for x, y in zip(a, b):
                if x != y:
                    diff += 1
                    if diff > 1:
                        return False
            return diff == 1

        words = set(wordList)
        if targetWord not in words:
            return 0
        words.add(startWord)

        q = deque([(startWord, 1)])
        visited = {startWord}
        while q:
            w, d = q.popleft()
            if w == targetWord:
                return d
            # naive neighbor search
            for nxt in list(words):
                if nxt not in visited and one_off(w, nxt):
                    visited.add(nxt)
                    q.append((nxt, d + 1))
        return 0
```

---

# 4) Interview Q&A (most common)

**Q1. Why BFS (not DFS/DP)?**
BFS on an unweighted graph guarantees the first time we see the target is along a **shortest path**. DFS can find a path but not necessarily the shortest.

**Q2. How do you generate neighbors efficiently?**
Use **wildcard buckets** (e.g., `h*t`, `*it`, `hi*`). Precompute a map: bucket → list of words. Then for a word, all one-letter neighbors are the union of its buckets.

**Q3. What’s the complexity?**
Let `N` be number of words (including start if needed) and `M` be word length.

* Preprocessing buckets: **O(N·M)**.
* BFS: each word popped once, touching **M** buckets and iterating their contents → **O(N·M)** overall (each edge visited constant number of times).
* Space: **O(N·M)** (buckets + visited + queue).

**Q4. What if `startWord` isn’t in the list?**
Add it to the set so it becomes a node in the graph.

**Q5. What if `targetWord` isn’t in the list?**
Then no valid ladder exists by problem rules → return **0** immediately.

**Q6. How would you speed it up further?**
Use **bidirectional BFS**. In practice, expanding the smaller frontier drastically reduces states visited.

**Q7. How do you avoid revisiting words (cycles)?**
Maintain a `visited` set. Optional micro-opt: after using a wildcard bucket, **clear** it to avoid re-iterating the same neighbors from other words on the same level.

**Q8. Can this handle very large dictionaries (N ~ 1e5)?**
Yes, bucket method scales well. Bidirectional BFS helps a lot when the ladder exists but is not too deep.

---

---

Awesome—here’s a **complete, runnable program** for **Word Ladder I** that:

* Implements the optimal **BFS + wildcard buckets** solution
* Documents **time/space complexity** right where each step happens
* Includes a **`main`** that runs a few inputs, prints outputs, and uses **`timeit`** to measure end-to-end runtime

> You can paste this into a single `.py` file and run it as is.

```python
#!/usr/bin/env python3
"""
Word Ladder I — Full program with timing

We return the length of the shortest transformation sequence from startWord
to targetWord where each step changes exactly one character and every intermediate
word must exist in the dictionary (wordList).

Approach: BFS on an implicit graph, using "wildcard buckets" to fetch 1-letter
neighbors in near O(1).

Let:
  N = number of unique words (including startWord if needed)
  M = word length (all words have equal length)
"""

from collections import defaultdict, deque
import timeit


class Solution:
    def wordLadderLength(self, startWord: str, targetWord: str, wordList):
        """
        Returns the shortest path length (number of words in the path, including start & target).
        If no path exists, returns 0.

        ─────────────────────────────────────────────────────────────────────────────
        OVERALL COMPLEXITY (high level)
          Time:  O(N * M) for building buckets + O(N * M) for BFS ≈ O(N * M)
          Space: O(N * M) for buckets + O(N) visited/queue
        ─────────────────────────────────────────────────────────────────────────────
        """
        # Edge case — if already equal:
        # Time: O(1), Space: O(1)
        if startWord == targetWord:
            return 1

        L = len(startWord)

        # Build word set; ensure target is present (otherwise no valid ladder)
        # Time: O(N), Space: O(N)
        wordSet = set(wordList)
        if targetWord not in wordSet:
            return 0

        # Ensure start is present so we can start BFS "inside" the graph
        # Time: O(1), Space: O(1) additional
        wordSet.add(startWord)

        # ─────────────────────────────────────────────────────────────────────
        # 1) BUILD WILDCARD BUCKETS
        #    For each word, generate M keys by replacing position i with '*'
        #    Example: 'hot' -> '*ot','h*t','ho*'
        #    These buckets let us fetch all 1-letter neighbors in one hash lookup.
        #
        #    Time:  O(N * M)  (N words, M keys per word)
        #    Space: O(N * M)  (store each (key -> list of words))
        # ─────────────────────────────────────────────────────────────────────
        buckets = defaultdict(list)
        for w in wordSet:
            for i in range(L):
                key = w[:i] + '*' + w[i + 1 :]
                buckets[key].append(w)

        # ─────────────────────────────────────────────────────────────────────
        # 2) BFS FROM startWord
        #    Each pop explores all its M wildcard buckets; we enqueue unseen neighbors.
        #
        #    Worst-case Time: O(N * M) (each word processed once, touching M buckets)
        #    Space:           O(N) for visited + queue (in addition to buckets)
        # ─────────────────────────────────────────────────────────────────────
        q = deque([(startWord, 1)])  # (word, distance)
        visited = {startWord}

        while q:
            word, dist = q.popleft()

            if word == targetWord:
                # Found the shortest distance (BFS guarantees optimality)
                # Time: O(1)
                return dist

            # Explore neighbors by wildcard keys
            # Time per node: O(M + total neighbors in those buckets)
            for i in range(L):
                key = word[:i] + '*' + word[i + 1 :]
                for nxt in buckets[key]:
                    if nxt not in visited:
                        visited.add(nxt)   # Space: O(1) amortized
                        q.append((nxt, dist + 1))
                # Micro-optimization: clear this bucket so future nodes don't re-iterate
                # Time: O(1) per bucket on average, reduces total iteration
                buckets[key].clear()

        # No ladder
        return 0


# ─────────────────────────────────────────────────────────────────────────────
# Demo + timing
# ─────────────────────────────────────────────────────────────────────────────

def run_cases():
    sol = Solution()

    cases = [
        # Example 1
        dict(
            start="der",
            target="dfs",
            words=["des", "der", "dfr", "dgt", "dfs"],
            expected=3,
        ),
        # Example 2
        dict(
            start="gedk",
            target="geek",
            words=["geek", "gefk"],
            expected=2,
        ),
        # Classic longer example
        dict(
            start="toon",
            target="plea",
            words=["poon", "plee", "same", "poie", "plea", "plie", "poin", "plea"],
            expected=7,
        ),
        # No path (target missing)
        dict(
            start="hit",
            target="cog",
            words=["hot", "dot", "dog", "lot", "log"],  # 'cog' not present
            expected=0,
        ),
        # Trivial equal
        dict(
            start="aaa",
            target="aaa",
            words=["aaa"],
            expected=1,
        ),
    ]

    for i, c in enumerate(cases, 1):
        ans = sol.wordLadderLength(c["start"], c["target"], c["words"])
        print(f"Case {i}: start={c['start']} target={c['target']} -> result={ans}  (expected={c['expected']})")


def time_full_program():
    # Time the entire `run_cases` using timeit for fairness (includes construction, calls, etc.)
    # We use number=3 to get a stable-ish reading; adjust as needed.
    t = timeit.timeit(stmt=run_cases, number=3)
    print(f"\nTotal runtime over 3 iterations: {t:.6f} seconds")
    print("(Note: runtime depends on machine, Python version, and input sizes.)")


if __name__ == "__main__":
    run_cases()
    time_full_program()
```

---

## What the program prints (illustrative)

On running, you’ll see outputs like:

```
Case 1: start=der target=dfs -> result=3  (expected=3)
Case 2: start=gedk target=geek -> result=2  (expected=2)
Case 3: start=toon target=plea -> result=7  (expected=7)
Case 4: start=hit target=cog -> result=0  (expected=0)
Case 5: start=aaa target=aaa -> result=1  (expected=1)

Total runtime over 3 iterations: 0.001234 seconds
(Note: runtime depends on machine, Python version, and input sizes.)
```

(The timing number will vary on your machine; it’s there for quick profiling.)

---

## 6) Real-World Use Cases (a few important ones)

1. **Spelling correction / keyboard neighbors**
   Suggest the shortest series of single-letter edits to transform a misspelled word to a valid dictionary word.

2. **Molecule/Protein mutation modeling**
   Model allowed one-mutation transitions to reach a target sequence with the fewest mutations (e.g., gene-editing steps).

3. **Phishing/domain squatting detection**
   Detect if a suspicious domain name is a few single-character changes away from a legitimate brand’s domain.

4. **Version migration planning**
   When only certain single changes are allowed per step (e.g., config flags), compute the minimum steps to reach a desired configuration.
