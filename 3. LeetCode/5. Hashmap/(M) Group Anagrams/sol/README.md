
---

### ✅ Full Program with Inline Comments and Complexity

```python
from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Dictionary where the key is the sorted version of the string,
        # and the value is a list of all anagrams with that sorted signature.
        anagram_map = defaultdict(list)  # O(1) space per key/value init

        for word in strs:
            # Step 1: Sort the characters in the word to form the key
            sorted_key = ''.join(sorted(word))  # O(K log K), K = len(word)

            # Step 2: Append the word to its anagram group in the hashmap
            anagram_map[sorted_key].append(word)  # O(1) per append

        # Step 3: Return the grouped anagrams as a list of lists
        return list(anagram_map.values())  # O(N) to gather all groups
```

---

### ⏱ Time Complexity Breakdown

Let:

* `N` = number of words in `strs`
* `K` = average length of each word

| Step              | Complexity            |
| ----------------- | --------------------- |
| Sorting each word | O(K log K)            |
| Loop over N words | O(N \* K log K)       |
| Appending to map  | O(1) per append       |
| Returning result  | O(N)                  |
| **Total Time**    | ✅ **O(N \* K log K)** |

---

### 🧠 Space Complexity Breakdown

| Component                | Space           |
| ------------------------ | --------------- |
| Hashmap for anagram\_map | O(N \* K)       |
| Output list of lists     | O(N \* K)       |
| Temporary sorted strings | O(K) at a time  |
| **Total Space**          | ✅ **O(N \* K)** |

---

### 🧪 Sample Input and Output

```python
# Input
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

# Execution
sol = Solution()
output = sol.groupAnagrams(strs)

# Output (Order may vary)
print(output)
# Possible Output:
# [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
```

---

### 🔍 Dry Run for: `["eat", "tea", "tan", "ate", "nat", "bat"]`

| Word | Sorted Key | anagram\_map State                               |
| ---- | ---------- | ------------------------------------------------ |
| eat  | aet        | { 'aet': \['eat'] }                              |
| tea  | aet        | { 'aet': \['eat', 'tea'] }                       |
| tan  | ant        | { 'aet': \[...], 'ant': \['tan'] }               |
| ate  | aet        | { 'aet': \['eat', 'tea', 'ate'], 'ant': \[...] } |
| nat  | ant        | { 'aet': \[...], 'ant': \['tan', 'nat'] }        |
| bat  | abt        | { ..., 'abt': \['bat'] }                         |

---

### ✅ Final Output:

```python
[['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
```

(Note: The outer list and the order of inner lists may vary due to dictionary hashing.)

---

Optimized version of the **Group Anagrams** problem using **character frequency array as the key**, which achieves **O(K)** time per word instead of `O(K log K)` for sorting.

---

### ✅ Full Python Program (Frequency Array Key)

```python
from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Hash map to group anagrams by their frequency signature
        anagram_map = defaultdict(list)  # key: tuple(freq[26]), value: list of words

        for word in strs:
            # Step 1: Create a frequency array of 26 lowercase letters
            freq = [0] * 26  # O(1) space for fixed size
            for char in word:
                freq[ord(char) - ord('a')] += 1  # O(K) per word

            # Step 2: Use the tuple of freq as the hashmap key
            key = tuple(freq)  # O(1) to convert since fixed size

            # Step 3: Append the word to the group corresponding to its freq pattern
            anagram_map[key].append(word)

        # Step 4: Return grouped anagrams
        return list(anagram_map.values())
```

---

### ⏱ Time Complexity

* **Let N = number of words, K = average length of a word**

| Step                     | Complexity      |
| ------------------------ | --------------- |
| Frequency build per word | O(K)            |
| Looping over N words     | O(N \* K)       |
| Using tuple of 26        | O(1)            |
| Appending to map         | O(1) per append |
| Final conversion to list | O(N)            |
| **Total Time**           | ✅ **O(N \* K)** |

---

### 🧠 Space Complexity

| Component                       | Space           |
| ------------------------------- | --------------- |
| Hashmap keys (26-tuple)         | O(N)            |
| Grouped anagrams (output)       | O(N \* K)       |
| Frequency array (per iteration) | O(1)            |
| **Total Space**                 | ✅ **O(N \* K)** |

---

### 🧪 Example

```python
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

sol = Solution()
output = sol.groupAnagrams(strs)
print(output)
# Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
```

---

### 🔍 Dry Run (Word = "ate")

* `freq = [0]*26`
* for 'a' → freq\[0] += 1
* for 't' → freq\[19] += 1
* for 'e' → freq\[4] += 1
* `tuple(freq)` → key = `(1, 0, 0, 0, 1, ..., 1, ..., 0)`
* `anagram_map[key] = ['ate']`

This same key will be reused for "eat" and "tea".

---
