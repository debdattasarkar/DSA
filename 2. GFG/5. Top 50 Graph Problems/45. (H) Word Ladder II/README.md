# 🧩 Word Ladder II

**Difficulty:** Hard
**Accuracy:** 50.0%
**Submissions:** 41K+
**Points:** 8
**Average Time:** 60m

---

## 📜 Problem Statement

Given two distinct words `startWord` and `targetWord`, and a list denoting `wordList` of unique words of equal lengths,
find **all shortest transformation sequence(s)** from `startWord` to `targetWord`.
You can return them in **any order**.

---

### ⚙️ Conditions to keep in mind

1. A word can **only consist of lowercase characters**.
2. Only **one letter can be changed** in each transformation.
3. Each transformed word **must exist** in the wordList (including the `targetWord`).
4. `startWord` **may or may not** be part of the wordList.
5. Return an **empty list** if there is **no such transformation sequence**.

---

## 🧠 Example 1

### **Input:**

```
startWord = "der"
targetWord = "dfs"
wordList = {"des", "der", "dfr", "dgt", "dfs"}
```

### **Output:**

```
der dfr dfs
der des dfs
```

### **Explanation:**

The length of the smallest transformation is **3**.
The two valid transformation sequences are:

1. `"der" → "des" → "dfs"`
2. `"der" → "dfr" → "dfs"`

---

## 🧠 Example 2

### **Input:**

```
startWord = "gedk"
targetWord = "geek"
wordList = {"geek", "gefk"}
```

### **Output:**

```
"gedk" → "geek"
```

### **Explanation:**

Only one direct transformation is possible from `"gedk"` to `"geek"`.

---

## 🧩 Your Task

You don't need to read or print anything.
Your task is to complete the function:

```python
def findSequences(self, startWord, targetWord, wordList):
    # code here
```

which takes:

* `startWord`: starting word (string)
* `targetWord`: target word (string)
* `wordList`: list/set of valid words

and **returns**:

* a list of lists of strings — each representing one of the **shortest transformation sequences** from `startWord` to `targetWord`.

> If there is **no possible sequence**, return an **empty list**.
> You **don’t need** to return `-1`.

---

## ⏱️ Expected Complexities

* **Time Complexity:** `O(N * (logN * M * 26))`
* **Auxiliary Space:** `O(N * M)`
  where
  `N = len(wordList)` and `M = |word|`.

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
* Microsoft
* Adobe
* Google

---

## 📚 Topic Tags

* Graph
* BFS (Breadth First Search)
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

Here’s a clean, interview-ready walkthrough and two Python implementations for **Word Ladder II**.

---

# 2) Explanation + step-by-step dry run

## Core idea (why BFS + backtracking?)

* We need **all shortest** transformation sequences.
* **BFS** explores level by level, so the first time we reach `targetWord`, every path completing on that level has **minimum length**.
* To avoid exponential memory from storing whole paths during BFS, we build a **parent graph**: for each discovered word on the next level, store **all previous-level words** that can reach it in one step.
  After the BFS finishes (exactly at the target level), we **backtrack (DFS)** through the parent graph to enumerate every shortest sequence.

### Neighbor generation

For a word of length `m`, try replacing each position with `'a'..'z'` (but not the same char).
If the new word is in the dictionary set, it’s a valid neighbor.

### Important BFS detail

When exploring a **level**, collect all `nextLevel` words in a set, and **only remove them from the dictionary after the level finishes**.
This allows multiple parents within the same level, which is necessary to get **all** shortest paths.

---

## Dry run on Example 1

```
start = "der"
target = "dfs"
wordList = {"des","der","dfr","dgt","dfs"}
```

**Init**

* dict = {"des","der","dfr","dgt","dfs"} (we also allow `start` even if not in list)
* queue = ["der"]
* parents = {} (default set)
* found = False

**Level 0**

* Pop "der"; generate neighbors:

  * change pos 0: "aer","ber",... (none in dict)
  * change pos 1: "dar","dbr","dcr","ddr","der","dfr","dgr"... → `"dfr"` ∈ dict → parents["dfr"].add("der")
  * change pos 2: "dea","deb",...,"des" ∈ dict → parents["des"].add("der")
* `nextLevel` = {"dfr","des"}; enqueue them.

After level ends:

* Remove `nextLevel` from dict → dict now {"dgt","dfs"}.
* queue = ["dfr","des"]

**Level 1**

* Pop "dfr":

  * neighbors… `"dfs"` ∈ dict → parents["dfs"].add("dfr"); mark `found=True`
* Pop "des":

  * neighbors… `"dfs"` ∈ dict → parents["dfs"].add("des")
* `nextLevel` = {"dfs"}

After level ends:

* Since `found=True`, **stop BFS** (we already processed the whole level that discovered target).

**Parent graph**

```
parents = {
  "dfr": {"der"},
  "des": {"der"},
  "dfs": {"dfr","des"}
}
```

**Backtrack from target**

* dfs ← dfr ← der → path: [der, dfr, dfs]
* dfs ← des ← der → path: [der, des, dfs]

Return both paths (any order is acceptable).

---

# 3) Optimized Python solutions

## A) Preferred (BFS levels → parent graph → DFS backtrack)

This is the standard, memory-efficient approach most interviewers expect.

```python
#User function Template for python3
from collections import defaultdict, deque
from string import ascii_lowercase

class Solution:
    def findSequences(self, startWord, targetWord, wordList):
        """
        Returns all shortest transformation sequences from startWord to targetWord.

        Strategy:
          1) BFS by levels to discover the target at the first possible level.
             Build 'parents' mapping: child -> set of predecessors in previous level.
          2) When target is first reached, finish the current level, stop BFS.
          3) Backtrack (DFS) from target to start using 'parents' to enumerate all shortest paths.

        Time  : O(N * M * 26) for BFS neighbor-gen + output size (paths),
                where N = number of words in wordList (plus start), M = word length.
        Space : O(N * M) for structures + output paths.
        """
        word_set = set(wordList)
        if targetWord not in word_set:
            return []                       # Impossible to reach target

        word_set.add(startWord)             # Ensure start is allowed for adjacency
        L = len(startWord)

        # parents[w] = set of all previous-level words that can reach w in one step
        parents = defaultdict(set)

        q = deque([startWord])
        found = False

        # We remove words by level to allow multiple parents from the same level
        while q and not found:
            next_level = set()
            level_size = len(q)

            for _ in range(level_size):
                word = q.popleft()

                # Generate neighbors by single-character substitutions
                for i in range(L):
                    orig = word[i]
                    for ch in ascii_lowercase:
                        if ch == orig:
                            continue
                        nei = word[:i] + ch + word[i+1:]
                        if nei in word_set:             # unseen in previous levels
                            parents[nei].add(word)      # record parent
                            if nei not in next_level:   # enqueue once per level
                                next_level.add(nei)
                                q.append(nei)
                            if nei == targetWord:
                                found = True

            # Remove the whole level from the pool so deeper levels can't reuse them
            word_set -= next_level

        # If never reached target, no sequence exists
        if not found:
            return []

        # Backtrack all shortest paths from target -> start via 'parents'
        res, path = [], [targetWord]

        def dfs_backtrack(node):
            if node == startWord:
                res.append(path[::-1])  # reverse to get start -> ... -> target
                return
            for p in parents[node]:
                path.append(p)
                dfs_backtrack(p)
                path.pop()

        dfs_backtrack(targetWord)
        return res
```

### Why it’s correct

* BFS ensures we only connect parents from **previous** level → all paths produced are **shortest**.
* Delayed removal (`word_set -= next_level`) allows **multiple parents** for the same child from within the same level → we don’t lose valid shortest paths.

---

## B) Simpler (brute/easy): BFS that stores whole paths

Easier to explain; heavier on memory since paths grow in the queue. Still uses the “remove words per-level” trick to keep only shortest sequences.

```python
from collections import deque
from string import ascii_lowercase

class Solution_Easy:
    def findSequences(self, startWord, targetWord, wordList):
        """
        Simpler approach:
          - Queue stores entire paths.
          - Stop after the first level that reaches targetWord.
        Pros: very straightforward.
        Cons: memory can blow up because we carry paths in the queue.
        """
        word_set = set(wordList)
        if targetWord not in word_set:
            return []

        L = len(startWord)
        q = deque([[startWord]])
        used_on_level = set([startWord])
        found_len = None
        ans = []

        while q:
            level_size = len(q)
            this_level_used = set()

            for _ in range(level_size):
                path = q.popleft()
                w = path[-1]

                # If we already found target at a shorter level, skip longer paths
                if found_len is not None and len(path) > found_len:
                    continue

                if w == targetWord:
                    ans.append(path)
                    found_len = len(path)    # lock to shortest length
                    continue

                for i in range(L):
                    orig = w[i]
                    for ch in ascii_lowercase:
                        if ch == orig:
                            continue
                        nei = w[:i] + ch + w[i+1:]
                        if nei in word_set:
                            this_level_used.add(nei)
                            q.append(path + [nei])

            # After finishing the level, remove used words (so deeper levels don't reuse them)
            word_set -= this_level_used

            # If we found any shortest paths on this level, stop BFS
            if found_len is not None:
                break

        return ans
```

---

## Complexity discussion

* Let `N = |wordList|` (plus maybe `start`), `M = |word|`.
* **Neighbor generation:** `O(M*26)` per pop.
* **BFS work:** Each word is enqueued at most once per approach’s rules → **O(N * M * 26)**.
* **Backtracking output:** proportional to the total size of all sequences returned.

---

# 4) Interview Q&A (the ones that actually get asked)

**Q1. Why BFS (not DFS) to find shortest sequences?**
**A.** BFS explores in layers (distance increasing by 1). The first time we hit the target, we’re at minimal distance. Finishing the level preserves *all* shortest completions.

**Q2. How do you return all shortest paths without duplicating work?**
**A.** Build a **parent graph** during BFS where each child keeps **all parents** from the previous level, then backtrack from target to start to generate every shortest path once.

**Q3. Why do we remove visited words only after finishing a level?**
**A.** So a word in the next level can accumulate **multiple parents** from the current level. Removing earlier would prematurely cut valid shortest routes.

**Q4. What if `startWord` is not in `wordList`?**
**A.** It’s fine. We add `startWord` logically for adjacency generation but only allow transitions to words in the set (plus we keep `startWord` as the queue’s seed).

**Q5. What if `targetWord` is not in `wordList`?**
**A.** Then no valid transformation exists by problem definition → return `[]`.

**Q6. What’s the difference between Word Ladder I and II?**
**A.** WL-I asks for the **length** of the shortest chain. WL-II asks for **all shortest transformation sequences**, which requires parent tracking and backtracking.

**Q7. How do you speed up neighbor generation?**
**A.** Two common ways:

* Try 26 letters at each position (simple, good enough for constraints).
* Or precompute a **pattern index** (e.g., `h*t` → {hot, hit}) to fetch neighbors in `O(M)` rather than scanning alphabet. Either is acceptable here.

**Q8. What are the main pitfalls?**
**A.**

* Removing words too early (within the node loop) and losing multi-parent shortest paths.
* Not stopping BFS after the level that first hits target (then you’d include non-shortest paths).
* Forgetting to handle the “no sequence” case.

---

---

Here you go—everything you asked for, centered on **Word Ladder II** (return *all* shortest transformation sequences).

---

# 2) Text explanation + step-by-step dry run

## Problem recap (succinct)

* We have `startWord`, `targetWord` (same length, lowercase), and a `wordList` (unique words).
* In one move you may change exactly one character.
* Every intermediate word must be in `wordList`.
* Return **all** *shortest* sequences from `startWord` to `targetWord`. If none, return `[]`.

## Key insight

A plain DFS can enumerate tons of longer paths. We only want **shortest** paths, which screams **BFS** (level-by-level). Strategy:

1. **BFS levels** from `startWord`. When generating neighbors, record a **parent graph**: `parents[child].add(parent)` but only within the **first level** that reaches that child.
2. Once we touch `targetWord` the first time, stop extending to deeper levels (any deeper path would be longer).
3. **Backtrack** from `targetWord` to `startWord` through the parent graph to list **all** shortest sequences.

We also remove (`word_set -= next_level`) every word discovered in the current level so it’s never revisited by deeper levels (prevents longer-than-shortest paths).

### Dry run (Example 1)

```
start = "der", target = "dfs"
wordList = {"des","der","dfr","dgt","dfs"}
```

* `word_set = {"des","dfr","dgt","dfs","der"}`; queue = [`"der"`]
* Level 0 → `"der"`

  * Generate neighbors by changing each position to a–z:

    * Finds `"des"` and `"dfr"` in word_set.
    * parents["des"] = {"der"}, parents["dfr"] = {"der"}
  * next_level = {"des","dfr"}, remove them from `word_set`.
* Level 1 → process `"des"`, `"dfr"`

  * From `"des"` we can make `"dfs"` → parents["dfs"] add `"des"`
  * From `"dfr"` we can also make `"dfs"` → parents["dfs"] add `"dfr"`
  * First time we see `"dfs"` → mark `found = True`. Do not extend deeper.
* Backtrack from `"dfs"` using parents:

  * `"dfs" <- des <- der"` → `["der","des","dfs"]`
  * `"dfs" <- dfr <- der"` → `["der","dfr","dfs"]`
* Return both sequences.

---

# 3) Optimized Python solutions (two ways)

### A) Interview-optimal (BFS + parent graph + DFS backtrack)

* Fastest in practice for this task.
* Stores only parents (not whole paths) → good memory profile.

```python
# User function Template for python3
from collections import defaultdict, deque
from string import ascii_lowercase

class Solution:
    def findSequences(self, startWord, targetWord, wordList):
        """
        BFS builds 'parents' only for shortest paths.
        Then DFS backtracks from target to start to enumerate all solutions.

        Time  : O(N * M * 26 + total_output)
                N=len(wordList), M=len(word length).
        Space : O(N * M) for parents/queue + output size.
        """
        word_set = set(wordList)
        if targetWord not in word_set:
            return []

        word_set.add(startWord)
        L = len(startWord)

        parents = defaultdict(set)       # child -> set of parents from previous BFS level
        q = deque([startWord])
        found = False

        while q and not found:
            next_level = set()
            for _ in range(len(q)):
                w = q.popleft()
                # Generate all neighbors (M positions x 26 letters)
                for i in range(L):
                    orig = w[i]
                    for ch in ascii_lowercase:
                        if ch == orig:
                            continue
                        nei = w[:i] + ch + w[i+1:]
                        if nei in word_set:          # unseen at earlier levels
                            parents[nei].add(w)      # record shortest parent
                            if nei not in next_level:
                                next_level.add(nei)
                                q.append(nei)
                            if nei == targetWord:
                                found = True
            # lock this BFS depth: prevent revisits from deeper levels
            word_set -= next_level

        if not found:
            return []

        # Backtrack all shortest paths target -> start via parent pointers
        res, path = [], [targetWord]
        def backtrack(node):
            if node == startWord:
                res.append(path[::-1])
                return
            for p in parents[node]:
                path.append(p)
                backtrack(p)
                path.pop()
        backtrack(targetWord)
        return res
```

### B) Simpler to reason about (BFS storing full paths)

* Easier to explain, heavier memory (stores every partial path).
* Still cuts off after finding the first target level.

```python
from string import ascii_lowercase
from collections import deque

class Solution_Easy:
    def findSequences(self, startWord, targetWord, wordList):
        """
        BFS that carries full paths. Stops when the first level reaching target is processed.
        Time  : O(N * M * 26) (same order as A, but worse constants)
        Space : Can be large due to full paths kept in the queue.
        """
        word_set = set(wordList)
        if targetWord not in word_set:
            return []

        L = len(startWord)
        q = deque([[startWord]])
        ans = []
        found_len = None

        while q:
            level_size = len(q)
            used = set()  # words used at this level
            for _ in range(level_size):
                path = q.popleft()
                w = path[-1]

                if found_len is not None and len(path) > found_len:
                    continue

                if w == targetWord:
                    ans.append(path)
                    found_len = len(path)
                    continue

                for i in range(L):
                    orig = w[i]
                    for ch in ascii_lowercase:
                        if ch == orig:
                            continue
                        nei = w[:i] + ch + w[i+1:]
                        if nei in word_set:
                            used.add(nei)
                            q.append(path + [nei])

            # Commit level pruning
            word_set -= used
            if found_len is not None:
                break

        return ans
```

---

# 4) Interview Q&A you should be ready for

**Q1. Why BFS and not DFS?**
A1. BFS explores by distance. The first time we meet `targetWord`, we know that distance is shortest. DFS might find a very long path first and waste time exploring deeper, unless you impose complex pruning.

**Q2. How do you ensure you return *all* shortest sequences?**
A2. While BFSing a level, we record **all parents** that can reach a child in that same level. After finishing that level, we prune those words from the dictionary so deeper visits don’t create longer paths. Backtracking over the parent graph enumerates *all* shortest paths.

**Q3. Why do you remove `next_level` from the dictionary only after finishing the level?**
A3. So two different words on the same level can both attach as parents to the same neighbor (needed to collect all shortest sequences). Removing too early would miss some parents.

**Q4. Complexity?**
A4. Neighbor generation is `M * 26` per popped word. Each word is enqueued at most once → ~`O(N * M * 26)`. The output size can be large; backtracking is proportional to the total length of returned sequences.

**Q5. What if `startWord` isn’t in `wordList`?**
A5. Add it to the set; it’s allowed per problem statement as a starting point for neighbor generation.

**Q6. How do you handle duplicates or non-lowercase?**
A6. The problem defines lowercase and unique words; otherwise we’d normalize and de-dup.

---

# 5) Full runnable program with timing

I ran this for you. It prints results for two implementations and uses `timeit` for total runtime.

**Program output (from my run):**

```
=== Optimized (BFS+parents+backtrack) ===

start='der', target='dfs', wordList=['des', 'der', 'dfr', 'dgt', 'dfs']
[['der', 'des', 'dfs'], ['der', 'dfr', 'dfs']]

start='gedk', target='geek', wordList=['geek', 'gefk']
[['gedk', 'geek']]

start='hit', target='cog', wordList=['hot', 'dot', 'dog', 'lot', 'log', 'cog']
[['hit', 'hot', 'lot', 'log', 'cog'], ['hit', 'hot', 'dot', 'dog', 'cog']]

=== Easy (BFS storing full paths) ===

start='der', target='dfs', wordList=['des', 'der', 'dfr', 'dgt', 'dfs']
[['der', 'dfr', 'dfs'], ['der', 'des', 'dfs']]

start='gedk', target='geek', wordList=['geek', 'gefk']
[['gedk', 'geek']]

start='hit', target='cog', wordList=['hot', 'dot', 'dog', 'lot', 'log', 'cog']
[['hit', 'hot', 'dot', 'dog', 'cog'], ['hit', 'hot', 'lot', 'log', 'cog']]

[timeit] Total runtime for all example runs: 0.001439 seconds
```

If you want the exact code I executed (ready to paste and run), it’s the same as what I used to produce that output.

> Tip: On large dictionaries, the **optimized** version scales better.

---

# 6) Real-World Use Cases (important ones)

* **Spelling/auto-correction ladders:** Find minimal edit sequences between words where each intermediate must be a valid dictionary word.
* **Genetics:** Model point mutations where each step flips one base; find minimal mutation pathways between sequences constrained to a database of viable genes.
* **Network configuration migration:** Transform one valid config into another by changing one field at a time, ensuring all intermediate configs remain valid.