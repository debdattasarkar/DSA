# Count of distinct substrings 🧵

**Difficulty:** Medium  
**Accuracy:** 40.21%  
**Submissions:** 28K+  
**Points:** 4  

---

## Problem Statement

Given a string **s** consisting of lowercase English characters, determine the **total number of distinct non-empty substrings** present in the string.  

A substring is defined as a contiguous block of characters within the string.

Two substrings are considered distinct if their contents differ, even if they originate from different positions in the string.

> **Note:** The empty substring is **not** counted.

---

## Examples

### Example 1

**Input:** `s = "ababa"`  
**Output:** `9`  

**Explanation:**  
All distinct substrings of `"ababa"` are:  
`"a"`, `"b"`, `"ab"`, `"ba"`, `"aba"`, `"bab"`, `"abab"`, `"baba"`, `"ababa"`.

---

### Example 2

**Input:** `s = "aaa"`  
**Output:** `3`  

**Explanation:**  
The distinct substrings of `"aaa"` are:  
`"a"`, `"aa"`, `"aaa"`.

---

## Constraints

\[
1 \leq s.\text{size()} \leq 3000
\]

---

## Expected Complexities

- **Time Complexity:** `O(n^2)`  
- **Auxiliary Space:** `O(n^2)`

---

## Topic Tags

- Arrays  
- Trie  
- Data Structures  
- Advanced Data Structure  

---

## Related Articles

- Count Number Of Distinct Substring In A String

---

---

I’ll follow your numbering.

---

## 2. Explanation + Step-by-Step Dry Run

We’re given a lowercase string `s`.
We must return **how many distinct non-empty substrings** it has.

* A **substring** = contiguous slice `s[i..j]`.
* Distinct substrings = different contents (even if they appear at many positions).
* Empty substring is *not* counted.

Total substrings (with duplicates) = `n * (n + 1) / 2`, where `n = len(s)`.

The challenge: **avoid double-counting duplicates** efficiently.

---

### Intuition 1 – Brute Force with a Set

1. Generate **all substrings** `s[i:j+1]` for `0 ≤ i ≤ j < n`.
2. Insert each substring into a `set` (which stores only unique elements).
3. Answer = `len(set)`.

This is very simple but in theory it’s **O(n³)** in Python:

* There are `O(n²)` substrings.
* Each substring creation `s[i:j+1]` costs `O(length)` = up to `O(n)`.
* Total worst-case ≈ `O(n³)` character work.

For `n ≤ 3000`, in C++ this might still pass with some optimizations, but we want something cleaner.

---

### Intuition 2 – Trie of Substrings (Expected `O(n²)`)

We use a **Trie (prefix tree)** over *all suffixes* / substrings.

Idea:

* Each path from the root down to some node represents a substring.
* While inserting all substrings, **each new node created corresponds to a new distinct substring**.
* So, we can just **count nodes** we create.

Algorithm:

1. Have a `root` node.
2. For every starting index `i` from `0` to `n-1`:

   * Start at `node = root`.
   * For every ending index `j` from `i` to `n-1`:

     * Let `c = s[j]`.
     * If `c` is not in `node.children`:

       * Create new child node → this represents a **new distinct substring**.
       * Increment `unique_count`.
     * Move `node` to this child and continue.

Each pair `(i, j)` corresponds to visiting exactly one character and maybe creating one node.
Total characters processed = total length of all substrings = `O(n²)` → Time `O(n²)`.
Total nodes created = number of distinct substrings ≤ `O(n²)` → Space `O(n²)`.

This matches the expected complexity.

---

### Step-by-Step Dry Run (Trie) for `s = "ababa"`

We’ll track `(i, j)` and new nodes.

**Initial:**

* Trie is empty (only `root`).
* `unique_count = 0`.

---

#### Start i = 0 (substrings starting at index 0)

Current suffix: `"ababa"`

1. `j = 0`, substring `"a"`

   * `root` has no child `'a'` → create `root -> 'a'`.
   * `unique_count = 1` (substring `"a"`).
   * Move `node` to `'a'`.

2. `j = 1`, substring `"ab"`

   * From `'a'`, no child `'b'` → create `'a' -> 'b'`.
   * `unique_count = 2` (substring `"ab"`).
   * Node is `'b'`.

3. `j = 2`, substring `"aba"`

   * From `'b'`, no child `'a'` → create `'b' -> 'a'`.
   * `unique_count = 3` (substring `"aba"`).

4. `j = 3`, substring `"abab"`

   * From last `'a'`, no child `'b'` → create.
   * `unique_count = 4` (substring `"abab"`).

5. `j = 4`, substring `"ababa"`

   * From last `'b'`, no child `'a'` → create.
   * `unique_count = 5` (substring `"ababa"`).

After `i = 0`, trie contains path for suffix `"ababa"` → 5 new substrings.

---

#### Start i = 1 (substrings starting at index 1)

Current suffix: `"baba"`

1. `j = 1`, substring `"b"`

   * From `root`, `'b'` child does **not** exist → create.
   * `unique_count = 6` (substring `"b"`).

2. `j = 2`, substring `"ba"`

   * From `'b'`, no child `'a'` yet (this `'b'` is under `root`, different from the one under `'a'`) → create.
   * `unique_count = 7` (`"ba"`).

3. `j = 3`, substring `"bab"`

   * From that `'a'`, no `'b'` child → create.
   * `unique_count = 8` (`"bab"`).

4. `j = 4`, substring `"baba"`

   * From `'b'`, no `'a'` child → create.
   * `unique_count = 9` (`"baba"`).

So far we have 9 distinct substrings.

---

#### Start i = 2 (suffix `"aba"`)

1. `j = 2`, substring `"a"`

   * From `root`, `'a'` *already exists* → **no new node**, no new substring.
2. `j = 3`, substring `"ab"`

   * From that `'a'`, `'b'` already exists → no new node.
3. `j = 4`, substring `"aba"`

   * Under `'a' -> 'b'`, `'a'` already exists → no new node.

So **no** new substrings from index 2 (we’ve seen them already).

---

#### Start i = 3 (suffix `"ba"`)

1. `j = 3`, substring `"b"`

   * `root -> 'b'` already exists.
2. `j = 4`, substring `"ba"`

   * Under `root -> 'b'`, `'a'` already exists.

No new substrings.

---

#### Start i = 4 (suffix `"a"`)

1. `j = 4`, substring `"a"`

   * `root -> 'a'` already exists.

No new substrings.

Final `unique_count = 9`, which matches the example.

---

## 3. Python Solutions

### 3.1 Brute-Force Using a Set (simple, but slower)

```python
class Solution:
    def countSubs_bruteforce(self, s: str) -> int:
        """
        Brute-force approach:
        - Generate every substring s[i:j+1]
        - Put into a set to keep only distinct ones
        - Return size of the set

        Time complexity:
            There are O(n^2) substrings.
            Creating each substring in Python is O(length) = O(n) in the worst case.
            So worst-case time is O(n^3).
        Space complexity:
            We may store up to O(n^2) distinct substrings, so O(n^2) space.
        """
        n = len(s)
        distinct_substrings = set()

        # Choose every starting index i
        for start in range(n):
            # Choose every ending index j >= start
            for end in range(start, n):
                # Python slice s[start:end+1] creates a new string
                # representing substring from start to end inclusive
                substring = s[start:end + 1]
                distinct_substrings.add(substring)

        return len(distinct_substrings)
```

Good for understanding, not ideal if `n` is big.

---

### 3.2 Optimized Trie-Based Solution (Expected in Interviews)

```python
class TrieNode:
    def __init__(self):
        # Each node holds outgoing edges for characters
        self.children = {}  # dict: char -> TrieNode


class Solution:
    def countSubs(self, s: str) -> int:
        """
        Optimized O(n^2) solution using a Trie (prefix tree) of all substrings.

        Logic:
        - Insert every suffix s[i:] into a Trie.
        - While inserting from position i, we walk characters s[i], s[i+1], ...
        - Whenever we need to create a NEW child node, that path corresponds
          to a NEW distinct substring. So we increment the count.
        - Existing nodes mean the substring was already seen before starting
          from some earlier position.

        Time complexity:
            - There are O(n^2) characters across all substrings.
            - For each character we perform O(1) dict operations.
            => O(n^2) time.

        Space complexity:
            - Each distinct substring adds exactly one node.
            - Maximum distinct substrings is O(n^2).
            => O(n^2) space.
        """
        root = TrieNode()
        unique_substring_count = 0
        n = len(s)

        # For every starting index of substring
        for start in range(n):
            current_node = root

            # Extend substring one character at a time
            for end in range(start, n):
                current_char = s[end]

                # If this character edge doesn't exist from current node,
                # it means this substring (s[start:end+1]) is seen for the first time.
                if current_char not in current_node.children:
                    current_node.children[current_char] = TrieNode()
                    unique_substring_count += 1  # new distinct substring

                # Move deeper into the trie
                current_node = current_node.children[current_char]

        return unique_substring_count
```

This is neat, matches the problem’s tags (`Trie`, `Advanced Data Structure`) and expected `O(n^2)`.

---

### 3.3 Hash-Set with Rolling String (still simple, but slightly optimized idea)

Python-specific optimization: instead of slicing every time from scratch, we can **build the substring incrementally** using a list of chars and join once per `(start..end)` run.

It’s still `O(n^3)` worst-case in theory (due to joins), but often faster in practice and easy to code:

```python
class Solution:
    def countSubs_with_build(self, s: str) -> int:
        """
        Slightly optimized brute approach:
        - For each start, grow substring char-by-char using a list.
        - Join the list to string and add to set.

        Still O(n^3) in worst-case but good to understand and okay for smaller n.
        """
        n = len(s)
        distinct_substrings = set()

        for start in range(n):
            chars = []  # will hold s[start..end]
            for end in range(start, n):
                chars.append(s[end])
                # build substring up to end
                substring = ''.join(chars)
                distinct_substrings.add(substring)

        return len(distinct_substrings)
```

For interviews, **prefer to talk about the Trie-based `O(n^2)` solution**.

---

## 4. Interview Strategy: How to Remember & Expected Q&A

### Quick Memory Hook

Think: **“Insert all suffixes into a Trie, count new nodes.”**

Or as a 4-step chant:

> **Start, Walk, New-Node, Count**

1. **Start** at each index `i`.
2. **Walk** through characters `s[i..]`.
3. If edge for current char doesn’t exist → **New-Node**.
4. Every new node → **Count** one new distinct substring.

Right before the interview, remind yourself:

* Distinct substrings ↔ different paths in a Trie.
* Each new node created during insertion equals one new distinct substring.

---

### 5-line Pseudo-Code Skeleton (Trie version)

```text
root = new TrieNode()
ans = 0
for each start in [0..n-1]:
    node = root
    for each end in [start..n-1]:
        c = s[end]
        if c not in node.children: node.children[c] = new TrieNode(); ans++
        node = node.children[c]
return ans
```

From this template you can code it in Python/C++/Java in under a minute.

---

### Likely Interview Questions & Short Answers

---

**Q1: What’s the brute-force solution? Complexity?**

**A:**
Generate all substrings `s[i:j+1]` for every `0 ≤ i ≤ j < n` and insert them into a hash set. Answer = size of set.

* There are `O(n^2)` substrings, each substring copy costs `O(length) = O(n)` in worst case, so overall complexity ≈ `O(n^3)` in languages with copying slices.
* Space: `O(n^2)` to store all distinct substrings.

---

**Q2: How does the Trie-based optimized solution work?**

**A:**
I build a Trie over all substrings (or equivalently, insert all suffixes). Starting from each position `i`, I traverse the Trie following characters `s[i], s[i+1], ...`. Every time I need to create a new child node, that path represents a substring I’ve never seen before, so I increment a counter. At the end, the counter gives the number of distinct substrings.

---

**Q3: Why is the complexity O(n²) for the Trie approach?**

**A:**
For each starting index `i` I process characters `s[i..n-1]` once, so total character visits equals the total length of all substrings:
[
1 + 2 + \dots + n = O(n^2)
]
Every visit does only O(1) work (dictionary lookup / insert). So time is `O(n^2)`.
Each distinct substring adds exactly one node in the Trie. Maximum number of distinct substrings is also `O(n^2)`, so memory is `O(n^2)`.

---

**Q4: Why does each new Trie node correspond to exactly one new distinct substring?**

**A:**
Each path from the root to a node spells out a specific substring. When inserting substrings, if we create a brand-new node, it means the path for that substring never existed before; hence it’s a new unique substring. If we follow an existing path, it means that substring was already inserted (from another starting position), so it isn’t new.

---

**Q5: Are there even faster solutions than O(n²)?**

**A:**
Yes, advanced structures like **suffix automaton** or **suffix array + LCP** can compute the number of distinct substrings in `O(n)` or `O(n log n)` time. But for constraints up to 3000 and expected complexity `O(n^2)`, the Trie approach is typically what’s expected on this problem.

---

**Q6: How would you briefly compare the set-based and Trie-based approaches?**

**A:**

* **Set-based:**

  * Simple to implement.
  * Conceptually: “generate all substrings, deduplicate with a set.”
  * But can be `O(n^3)` due to substring copying.

* **Trie-based:**

  * A bit more code (need a node structure).
  * Conceptually: “build a prefix tree of substrings; each new node = new distinct substring.”
  * Achieves `O(n^2)` time and space, matching problem expectations.

---

If you rehearse:

> “Distinct substrings = **new nodes in substring Trie**”

and keep that 5-line pseudo-code in mind, you’ll be able to reconstruct both the explanation and the solution quickly in an interview.

---

---

Let’s wrap this one cleanly.

---

## 5. Real-World Use Cases (easy to talk about)

You can connect “count of distinct substrings” to real systems like this:

1. **Search / Autocomplete Engines (prefix-based queries)**

   * Many search boxes suggest completions based on all different substrings/prefixes users might type.
   * Distinct substrings of a dictionary or corpus give you the **space of all possible query fragments**.
   * A Trie of substrings or suffixes is a natural backing data structure for autocomplete / “did you mean…” features.

2. **Plagiarism / Similarity Detection**

   * Longer common substrings between two documents indicate high similarity.
   * Counting distinct substrings of each document (or using a shared suffix structure) is a building block for **measuring document similarity** and detecting plagiarism.

3. **Compression and Dictionary Building (LZ-like schemes)**

   * Compression schemes often build a **dictionary of repeated substrings**.
   * Understanding how many distinct substrings exist helps estimate dictionary size, memory needs, or decide which substrings are worth encoding.

4. **Bioinformatics (DNA / Protein sequences)**

   * DNA strings are huge; distinct substrings correspond to **distinct motifs or patterns**.
   * Tries/suffix structures are used to count and search motifs efficiently across genomes.

These are short and believable—perfect for an interviewer when they ask “Where would this be useful?”.

---

## 6. Full Python Program (Trie solution + timing + inline complexity notes)

This program:

* Implements the `Solution.countSubs` method using the Trie (O(n²) time, O(n²) space).
* Reads `s` from input.
* Measures elapsed time using `time.perf_counter()`.
* Prints the result and the runtime.

```python
import time


class TrieNode:
    def __init__(self):
        # Children edges: character -> TrieNode
        # Space for each node: O(σ) pointers in the worst case (σ = alphabet size)
        # but we keep it as a dict, so we only store existing edges.
        self.children = {}  # average O(1) lookup/insert


class Solution:
    def countSubs(self, s: str) -> int:
        """
        Count number of DISTINCT non-empty substrings of s using a Trie.

        High-level:
        - For each starting position i, walk characters s[i], s[i+1], ...
        - Insert them into a Trie.
        - When we create a NEW node, that substring has never been seen before.
        - Count how many nodes we create.

        Let n = len(s)

        Time complexity:
            - Outer loop over start: runs n times.
            - Inner loop over end: runs ~n, n-1, ..., 1 => O(n^2) iterations.
            - Each iteration does:
                * one dict "in" check, maybe one insert, and a pointer move
                => O(1) average work per character.
            - Total: O(n^2) time.

        Space complexity:
            - Each distinct substring contributes exactly one node.
            - Maximum distinct substrings is O(n^2).
            - So the Trie and bookkeeping require O(n^2) space.
        """

        root = TrieNode()
        distinct_count = 0
        n = len(s)

        # ---------- Outer loop: choose starting index ----------
        # Runs n times => O(n) iterations
        for start_index in range(n):
            current_node = root  # always start from root for each new substring start

            # ---------- Inner loop: extend substring character by character ----------
            # Total across all starts is O(n^2) character steps.
            for end_index in range(start_index, n):
                current_char = s[end_index]

                # Check if there is already an outgoing edge with this character.
                # Dict lookup: average O(1) time.
                if current_char not in current_node.children:
                    # Creating a new child node:
                    # This represents a new distinct substring s[start_index:end_index+1].
                    current_node.children[current_char] = TrieNode()
                    distinct_count += 1  # count the new distinct substring

                # Move to child node for next character
                current_node = current_node.children[current_char]

        return distinct_count


def main():
    """
    Driver code:
    - Reads input string.
    - Times the call to countSubs.
    - Prints result and runtime.

    Complexity of main (ignoring the Solution internals):
        - Input reading: O(n) where n = len(s)
        - One call to countSubs(s): O(n^2) time, O(n^2) space (Trie)
        - Printing: O(1)
    """

    print("Enter string s (lowercase letters):")

    # Start timer before reading input and processing.
    overall_start = time.perf_counter()

    # Input read
    # Time: O(n) to read line into memory
    s = input().strip()

    solver = Solution()

    # Core computation: O(n^2) time
    distinct_substring_count = solver.countSubs(s)

    # Stop timer after computation
    overall_end = time.perf_counter()

    # Output results
    print(f"Total number of distinct non-empty substrings of '{s}':")
    print(distinct_substring_count)

    elapsed_seconds = overall_end - overall_start
    print(f"Total elapsed time (seconds): {elapsed_seconds:.6f}")


if __name__ == "__main__":
    main()
```

### Example (conceptual) run

**Input**

```text
ababa
```

**Output**

```text
Enter string s (lowercase letters):
Total number of distinct non-empty substrings of 'ababa':
9
Total elapsed time (seconds): 0.0000xx
```

You can use this exact structure in practice; in an interview or on a judge, you’d usually only provide the `Solution` class with `countSubs`.
