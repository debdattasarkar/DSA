# Stream First Non-repeating

**Difficulty:** Medium  
**Accuracy:** 31.65%  
**Submissions:** 235K+  
**Points:** 4  
**Average Time:** 15m  

---

## Problem Statement

Given a string **s** consisting of only lowercase alphabets, for each index **i** in the string (`0 ≤ i < n`), find the **first non-repeating character** in the prefix `s[0..i]`. If no such character exists, use `'#'`.

---

## Examples

### Example 1
**Input:**  
`s = "aabc"`  

**Output:**  
`a#bb`

**Explanation:**  
At `i=0` (`"a"`): First non-repeating character is `'a'`.  
At `i=1` (`"aa"`): No non-repeating character, so `'#'`.  
At `i=2` (`"aab"`): First non-repeating character is `'b'`.  
At `i=3` (`"aabc"`): Non-repeating characters are `'b'` and `'c'`; `'b'` appeared first, so `'b'`.

---

### Example 2
**Input:**  
`s = "bb"`  

**Output:**  
`"b#"`

**Explanation:**  
At `i=0` (`"b"`): First non-repeating character is `'b'`.  
At `i=1` (`"bb"`): No non-repeating character, so `'#'`.

---

## Constraints

- `1 ≤ s.size() ≤ 10^5`

---

## Expected Complexities

- **Time Complexity:** `O(n)`
- **Auxiliary Space:** `O(1)`

---

## Company Tags

- Flipkart  
- Amazon  
- Microsoft  
- FactSet  
- Payu  
- Adobe  
- Yahoo  

---

## Topic Tags

- Hash  
- Queue  
- Data Structures  

---

## Related Interview Experiences

- Flipkart Interview For Sde Ii 2  

---

## Related Articles

- [Find First Non Repeating Character Stream Characters](https://www.geeksforgeeks.org/find-first-non-repeating-character-stream-characters/)

---

---

## 2) Text explanation (stream / prefix-wise first non-repeating)

For every prefix `s[0..i]`, we must output:

* the **first character whose frequency is 1** in that prefix,
* else `'#'`.

This is a classic **stream processing** problem.

### Interview-standard idea: `frequency + queue`

Maintain:

1. `freq[26]` = frequency of each character seen so far.
2. A queue that stores characters in the **order they appeared** (candidates for “first non-repeating”).

For each new character `ch`:

* increment `freq[ch]`
* push `ch` into queue
* while queue front has `freq > 1`, pop it (it’s no longer non-repeating)
* answer is queue front if exists else `'#'`

This guarantees **O(n)** because each character is pushed once and popped at most once.

---

## Step-by-step dry run (s = "aabc")

Initialize:

* `freq[a..z] = 0`
* `queue = []`
* `ans = ""`

### i=0, ch='a'

* freq[a]=1, queue=[a]
* front 'a' has freq 1 → output 'a'
* ans="a"

### i=1, ch='a'

* freq[a]=2, queue=[a,a]
* front 'a' freq 2 → pop → queue=[a]
* front 'a' freq 2 → pop → queue=[]
* queue empty → output '#'
* ans="a#"

### i=2, ch='b'

* freq[b]=1, queue=[b]
* front 'b' freq 1 → output 'b'
* ans="a#b"

### i=3, ch='c'

* freq[c]=1, queue=[b,c]
* front 'b' freq 1 → output 'b'
* ans="a#bb"

✅ Output: `"a#bb"`

---

## 3) Python solutions (brute + optimized interview way)

### A) Brute (easy but slow) — recompute first non-repeating for every prefix

For each prefix, scan from start and find first char with count 1.

**Time:** `O(n^2)`
**Space:** `O(1)` (26 counts per prefix)

```python
class Solution:
    def firstNonRepeating(self, s):
        result = []

        # For each prefix ending at i, recompute counts and find first unique
        for i in range(len(s)):
            freq = [0] * 26  # O(1) space
            for j in range(i + 1):  # counts for prefix s[0..i]
                freq[ord(s[j]) - 97] += 1

            # find first character in prefix with freq 1
            first_unique = '#'
            for j in range(i + 1):
                if freq[ord(s[j]) - 97] == 1:
                    first_unique = s[j]
                    break

            result.append(first_unique)

        return "".join(result)
```

---

### B) Most expected (Optimal): Frequency + Queue

**Time:** `O(n)`
**Aux Space:** `O(1)` because only 26 frequencies + queue up to n (some platforms still call it O(1) due to fixed alphabet; practically queue can be O(n)).

```python
from collections import deque

class Solution:
    def firstNonRepeating(self, s):
        # freq for 26 lowercase letters => O(1) space
        frequency = [0] * 26

        # queue keeps characters in the order they appear
        candidate_queue = deque()

        output_chars = []

        for ch in s:
            idx = ord(ch) - ord('a')

            # Step 1: update frequency
            frequency[idx] += 1

            # Step 2: add to queue as a candidate
            candidate_queue.append(ch)

            # Step 3: remove all repeated chars from the front
            while candidate_queue and frequency[ord(candidate_queue[0]) - ord('a')] > 1:
                candidate_queue.popleft()

            # Step 4: current answer for this prefix
            if candidate_queue:
                output_chars.append(candidate_queue[0])
            else:
                output_chars.append('#')

        return "".join(output_chars)
```

---

### C) Alternative “clean” version using dict + queue (works for any charset)

Same logic, just not limited to lowercase.

```python
from collections import deque

class Solution:
    def firstNonRepeating(self, s):
        freq = {}
        q = deque()
        ans = []

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
            q.append(ch)

            while q and freq[q[0]] > 1:
                q.popleft()

            ans.append(q[0] if q else '#')

        return "".join(ans)
```

---

## 4) Interview quick recall + expected Q&A

### Quick memory trick

**“Count + Queue + Clean Front”**

Mnemonic:
**“Push → Count → Pop repeats → Peek answer”**

### 5-line interview skeleton

```text
freq[26]=0, q=empty, ans=""
for ch in s: freq[ch]++, q.push(ch)
while q not empty and freq[q.front] > 1: q.pop()
ans += (q.front if q else '#')
return ans
```

---

## Expected Interview Questions & Answers

### Q1) Why do we need a queue?

**A:** To preserve insertion order so we can quickly know the earliest candidate that might be non-repeating.

### Q2) Why is it O(n)?

**A:** Each character enters the queue once and can be removed at most once. Total queue operations are linear.

### Q3) Why not just keep counts and scan each time?

**A:** That would be `O(n^2)` for n up to `1e5`, too slow.

### Q4) What if characters weren’t only lowercase?

**A:** Use a hashmap (`dict`) for counts instead of a fixed array of size 26.

### Q5) What does “first non-repeating in prefix” mean exactly?

**A:** Among characters in `s[0..i]` with frequency 1, pick the one that appeared earliest in that prefix.

### Q6) Space complexity: is it really O(1)?

**A:** Frequency is O(1) for fixed alphabet (26). Queue can hold up to O(n) in worst case, but often described as O(1) extra for bounded alphabet problems; practically it’s O(n).

---

---

## 5) Real-world use cases (few, interviewer-relatable)

1. **Live chat / comment moderation (stream processing)**

   * As characters/messages arrive, you may want the “first unique” signal (e.g., detect first unique token/character pattern) in real-time.

2. **Log/telemetry pipelines**

   * In a stream of events/IDs, finding the earliest event that has occurred exactly once so far helps detect anomalies or “new/rare” signals.

3. **Network/security monitoring**

   * First non-repeating request signature / byte pattern in a stream can indicate a unique probe or suspicious one-off behavior.

---

## 6) Full Python program (timed) + inline time/space notes + sample I/O

* Input format:

  * One line string `s`
* Output:

  * Result string (first non-repeating for each prefix)
* Runtime printed to **stderr** (so normal judge output remains clean)

```python
import sys
import time
from collections import deque

class Solution:
    def firstNonRepeating(self, s):
        """
        Optimized stream approach using frequency + queue.

        Time Complexity: O(n)
          - Each character is pushed once and popped at most once.

        Auxiliary Space:
          - frequency array: O(1) (size 26)
          - queue: up to O(n) in worst case (stores candidates)
        """
        # Step 1: frequency array for lowercase letters
        # Time: O(1), Space: O(1)
        frequency = [0] * 26

        # Step 2: queue to maintain order of candidates
        # Time: O(1), Space: up to O(n)
        candidate_queue = deque()

        # Step 3: build output incrementally
        # Time: O(n), Space: O(n) for output
        output = []

        for ch in s:
            idx = ord(ch) - ord('a')

            # Update frequency
            # Time: O(1)
            frequency[idx] += 1

            # Add to queue as a candidate
            # Time: O(1)
            candidate_queue.append(ch)

            # Remove repeated elements from the front
            # Total across whole run: O(n) pops
            while candidate_queue and frequency[ord(candidate_queue[0]) - ord('a')] > 1:
                candidate_queue.popleft()

            # Append current first non-repeating or '#'
            # Time: O(1)
            output.append(candidate_queue[0] if candidate_queue else '#')

        return "".join(output)


def main():
    """
    Input:
      s (single line lowercase string)

    Output:
      stream result string
    """
    start_time = time.perf_counter()  # full program runtime timer

    data = sys.stdin.read().strip()
    if not data:
        return

    s = data  # input string

    solver = Solution()

    # Solve
    # Time: O(n), Space: as described above
    result = solver.firstNonRepeating(s)

    # Print answer to stdout
    print(result)

    end_time = time.perf_counter()
    # Print timing to stderr (does not affect expected stdout output)
    print(f"[Execution Time] {end_time - start_time:.6f} seconds", file=sys.stderr)


if __name__ == "__main__":
    main()


"""
Sample Input:
aabc

Expected Output:
a#bb

Explanation:
prefix "a" -> a
prefix "aa" -> #
prefix "aab" -> b
prefix "aabc" -> b
"""
```
