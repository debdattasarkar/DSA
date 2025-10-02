
# Alien Dictionary
---

A new alien language uses the English alphabet, but the order of letters is unknown. You are given a list of `words[]` from the alien language’s dictionary, where the words are claimed to be **sorted lexicographically** according to the language’s rules.

## Problem Statement

Your task is to determine **the correct order of letters** in this alien language based on the given words. If the order is valid, return a string containing the unique letters in lexicographically increasing order as per the new language's rules.

If there are multiple valid orders, return any one of them.  
If the arrangement is inconsistent with any possible letter ordering, return an empty string `""`.

A string `a` is lexicographically smaller than a string `b` if, at the first position where they differ, the character in `a` appears earlier in the alien language than the corresponding character in `b`.  
If all characters in the shorter word match the beginning of the longer word, the shorter word is considered smaller.

> **Note:** Your implementation will be tested using a driver code. It will print `true` if your returned order correctly follows the alien language’s lexicographic rules; otherwise, it will print `false`.

---

## Examples

### Example 1
**Input:**  
```python
words = ["baa", "abcd", "abca", "cab", "cad"]
```

**Output:**

```python
"bdac"
```

**Explanation:**

* "baa" vs "abcd" → `b` before `a`
* "abcd" vs "abca" → `d` before `a`
* "abca" vs "cab" → `a` before `c`
* "cab" vs "cad" → `b` before `d`

Valid ordering: `b → d → a → c`

---

### Example 2

**Input:**

```python
words = ["caa", "aaa", "aab"]
```

**Output:**

```python
"cab"
```

**Explanation:**

* "caa" vs "aaa" → `c` before `a`
* "aaa" vs "aab" → `a` before `b`

Valid ordering: `c → a → b`

---

### Example 3

**Input:**

```python
words = ["ab", "cd", "ef", "ad"]
```

**Output:**

```python
""
```

**Explanation:**

* "ab" vs "ef" → `a` before `e`
* "ef" vs "ad" → `e` before `a`
  Contradiction found, hence no valid order.

---

## Constraints

* `1 ≤ words.length ≤ 500`
* `1 ≤ words[i].length ≤ 100`
* All words consist only of lowercase English letters.

---

## Expected Complexities

* **Time Complexity**: O(n \* m)
* **Auxiliary Space**: O(n \* m)
  Where `n` is the number of words and `m` is the average word length.

---

## Tags

**Company Tags:** Flipkart, Amazon, Microsoft, OYO Rooms, Walmart, Google
**Topic Tags:** Strings, Sorting, Graph, Data Structures, Algorithms

---

## Related Articles

* [Given Sorted Dictionary, Find Precedence Characters](#)

## Related Interview Experiences

* Walmart Lab Interview Experience Set 9 Off Campus
* Amazon Interview Experience For SDE 1 (6 Months Internship)
* Flipkart Interview SDE 2 (Set 2)

---

Here’s a complete **text explanation with a step-by-step dry run**, followed by **Python, C++, and JavaScript** implementations — all with inline comments.

---

## 🧠 **Problem Intuition: Alien Dictionary**

You're given a dictionary of words sorted in lexicographic order according to some *unknown alphabet*. Your goal is to **infer the character order**.

This is a classic **topological sort** problem:

* Think of each character as a node.
* If character `x` comes before `y` in any two words, you have a directed edge from `x` to `y`.
* Then, **topologically sort** this graph to determine the valid character order.

---

## 🔍 **Step-by-Step Explanation and Dry Run**

### Example Input:

```python
words = ["caa", "aaa", "aab"]
```

### Step 1: Build Graph

Compare consecutive words:

1. **"caa" vs "aaa"**

   * First difference: `'c'` vs `'a'` → `c` → `a`

2. **"aaa" vs "aab"**

   * First difference: `'a'` vs `'a'`, `'a'` vs `'a'`, `'a'` vs `'b'` → `a` → `b`

### Graph:

* `c → a`
* `a → b`

### Step 2: Topological Sort (Kahn’s Algorithm)

* In-degrees:

  * `a`: 1 (from `c`)
  * `b`: 1 (from `a`)
  * `c`: 0

* Start with `c`, then go to `a`, then `b`.

✅ **Final Order**: `cab`

---

# ✅ Python Code

```python
from collections import defaultdict, deque

class Solution:
    def findOrder(words):
        # Step 1: Build graph and in-degree count
        graph = defaultdict(list)
        in_degree = {char: 0 for word in words for char in word}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            min_len = min(len(w1), len(w2))
            for j in range(min_len):
                if w1[j] != w2[j]:
                    graph[w1[j]].append(w2[j])
                    in_degree[w2[j]] += 1
                    break
            else:
                # Check invalid case like ["abc", "ab"]
                if len(w1) > len(w2):
                    return ""

        # Step 2: Topological Sort using BFS
        queue = deque([ch for ch in in_degree if in_degree[ch] == 0])
        res = []

        while queue:
            ch = queue.popleft()
            res.append(ch)
            for nei in graph[ch]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    queue.append(nei)

        return "".join(res) if len(res) == len(in_degree) else ""
```

---

# ✅ C++ Code

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
  public:
    string findOrder(vector<string> &words) {
        unordered_map<char, vector<char>> graph;
        unordered_map<char, int> in_degree;

        for (auto &word : words)
            for (char c : word)
                in_degree[c] = 0;

        for (int i = 0; i < words.size() - 1; i++) {
            string w1 = words[i], w2 = words[i+1];
            int minLen = min(w1.length(), w2.length());

            for (int j = 0; j < minLen; j++) {
                if (w1[j] != w2[j]) {
                    graph[w1[j]].push_back(w2[j]);
                    in_degree[w2[j]]++;
                    break;
                }
            }

            if (w1.substr(0, minLen) == w2 && w1.length() > w2.length())
                return "";
        }

        queue<char> q;
        for (auto &entry : in_degree)
            if (entry.second == 0) q.push(entry.first);

        string res;
        while (!q.empty()) {
            char ch = q.front(); q.pop();
            res += ch;
            for (char nei : graph[ch]) {
                if (--in_degree[nei] == 0)
                    q.push(nei);
            }
        }

        return res.length() == in_degree.size() ? res : "";
    }
};
```

---

# ✅ JavaScript Code

```javascript
class Solution {
    findOrder(words) {
        const graph = new Map();
        const inDegree = new Map();

        // Initialize in-degree map
        for (let word of words) {
            for (let char of word) {
                inDegree.set(char, 0);
                graph.set(char, []);
            }
        }

        // Build graph
        for (let i = 0; i < words.length - 1; i++) {
            let w1 = words[i], w2 = words[i+1];
            let minLen = Math.min(w1.length, w2.length);

            for (let j = 0; j < minLen; j++) {
                if (w1[j] !== w2[j]) {
                    graph.get(w1[j]).push(w2[j]);
                    inDegree.set(w2[j], inDegree.get(w2[j]) + 1);
                    break;
                }
            }

            if (w1.length > w2.length && w1.startsWith(w2))
                return "";
        }

        // Kahn's Algorithm (BFS Topological Sort)
        let queue = [];
        for (let [ch, deg] of inDegree.entries()) {
            if (deg === 0) queue.push(ch);
        }

        let res = "";
        while (queue.length > 0) {
            let ch = queue.shift();
            res += ch;
            for (let nei of graph.get(ch)) {
                inDegree.set(nei, inDegree.get(nei) - 1);
                if (inDegree.get(nei) === 0)
                    queue.push(nei);
            }
        }

        return res.length === inDegree.size ? res : "";
    }
}
```

---

Let me know if you'd like to see this implemented using **DFS/topological sort** as an alternative!

Great! Let's now solve the **Alien Dictionary** problem using **DFS-based Topological Sort**, which is an alternative to the Kahn’s Algorithm (BFS approach). This is especially useful when you want to use recursion and stack for topological order.

---

## ✅ **Topological Sort via DFS: Explanation**

1. Build a **graph** (adjacency list) from characters and inferred edges between them.
2. Use **DFS traversal**:

   * Mark nodes as **visited** or **visiting** (for cycle detection).
   * Use a **stack** to record the order of nodes after all their dependencies are visited.
3. **If a cycle is detected**, return an empty string `""`.

---

### 🔁 **Dry Run Example**

Input: `["caa", "aaa", "aab"]`

Edges:

* `c → a`
* `a → b`

Topological DFS:

* Visit `c`: go to `a`
* Visit `a`: go to `b`
* Visit `b`: done
  **Stack = \['b', 'a', 'c']`→ Reverse →`"cab"\`**

---

# ✅ Python (DFS)

```python
from collections import defaultdict

class Solution:
    def findOrder(words):
        graph = defaultdict(list)
        all_chars = set(''.join(words))

        # Build graph
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            min_len = min(len(w1), len(w2))
            for j in range(min_len):
                if w1[j] != w2[j]:
                    graph[w1[j]].append(w2[j])
                    break
            else:
                if len(w1) > len(w2):
                    return ""

        visited = {}
        result = []
        has_cycle = [False]

        def dfs(node):
            if node in visited:
                return visited[node]  # False if visiting (cycle), True if visited
            visited[node] = False  # Mark as visiting
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            visited[node] = True
            result.append(node)
            return True

        for ch in all_chars:
            if ch not in visited:
                if not dfs(ch):
                    return ""

        return ''.join(reversed(result))
```

---

# ✅ C++ (DFS)

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
  public:
    string findOrder(vector<string>& words) {
        unordered_map<char, vector<char>> graph;
        unordered_set<char> all_chars;
        for (auto &word : words)
            for (char c : word)
                all_chars.insert(c);

        for (int i = 0; i < words.size() - 1; i++) {
            string w1 = words[i], w2 = words[i+1];
            int minLen = min(w1.size(), w2.size());
            for (int j = 0; j < minLen; j++) {
                if (w1[j] != w2[j]) {
                    graph[w1[j]].push_back(w2[j]);
                    break;
                }
            }
            if (w1.substr(0, minLen) == w2 && w1.size() > w2.size())
                return "";
        }

        unordered_map<char, bool> visited;
        unordered_map<char, bool> visiting;
        stack<char> st;
        function<bool(char)> dfs = [&](char node) {
            if (visiting[node]) return false; // cycle
            if (visited[node]) return true;

            visiting[node] = true;
            for (char nei : graph[node])
                if (!dfs(nei)) return false;

            visiting[node] = false;
            visited[node] = true;
            st.push(node);
            return true;
        };

        for (char c : all_chars) {
            if (!visited[c])
                if (!dfs(c))
                    return "";
        }

        string res;
        while (!st.empty()) {
            res += st.top();
            st.pop();
        }
        return res;
    }
};
```

---

# ✅ JavaScript (DFS)

```javascript
class Solution {
    findOrder(words) {
        const graph = new Map();
        const allChars = new Set();

        // Build graph
        for (let word of words)
            for (let ch of word)
                allChars.add(ch), graph.set(ch, []);

        for (let i = 0; i < words.length - 1; i++) {
            let w1 = words[i], w2 = words[i+1];
            let minLen = Math.min(w1.length, w2.length);
            for (let j = 0; j < minLen; j++) {
                if (w1[j] !== w2[j]) {
                    graph.get(w1[j]).push(w2[j]);
                    break;
                }
            }
            if (w1.startsWith(w2) && w1.length > w2.length) return "";
        }

        let visited = new Map();
        let visiting = new Set();
        let res = [];

        const dfs = (node) => {
            if (visiting.has(node)) return false;
            if (visited.has(node)) return true;

            visiting.add(node);
            for (let nei of graph.get(node)) {
                if (!dfs(nei)) return false;
            }
            visiting.delete(node);
            visited.set(node, true);
            res.push(node);
            return true;
        };

        for (let ch of allChars) {
            if (!visited.has(ch)) {
                if (!dfs(ch)) return "";
            }
        }

        return res.reverse().join('');
    }
}
```

---

Let me know if you'd like to compare DFS vs BFS performance or edge case behavior!

Great question! Let's compare **DFS (Depth-First Search)** and **BFS (Breadth-First Search, a.k.a. Kahn's Algorithm)** for solving the **Alien Dictionary** problem, both in terms of **performance** and **edge case behavior**.

---

## ⚔️ DFS vs BFS Comparison

| Aspect                      | **DFS (Topological Sort via Recursion)** | **BFS (Kahn's Algorithm)**             |
| --------------------------- | ---------------------------------------- | -------------------------------------- |
| **Time Complexity**         | O(N + E)                                 | O(N + E)                               |
| **Space Complexity**        | O(N + E) + O(N) stack                    | O(N + E) + O(N) queue                  |
| **Cycle Detection**         | ✅ Built-in (via "visiting" state)        | ✅ Based on in-degree not reaching zero |
| **Implementation**          | Recursive, uses post-order               | Iterative, uses queue                  |
| **Result Order**            | Reversed post-order of DFS               | Order of zero in-degree processing     |
| **Stability (determinism)** | Depends on recursion order (may vary)    | Depends on queue order (may vary)      |
| **Ease of Use**             | Better when recursion is intuitive       | More intuitive for beginners           |
| **Stack Overflow Risk**     | ⚠️ Possible with deep recursion          | ❌ No risk, fully iterative             |
| **Common Use**              | Dependency resolution, build systems     | Scheduling, layer-wise traversal       |

---

## ⚠️ Edge Case Behavior Differences

### ✅ **Case 1: Cycle in Graph**

```python
words = ["abc", "ab"]
```

* **Meaning:** "abc" should come before "ab", but "ab" is a prefix.
* **Expected Result:** `""` (invalid)

**DFS**: Will catch the issue during traversal or loop.
**BFS**: Will detect it via in-degree not reducing to 0 for all nodes.

✅ **Both handle this properly** if implemented with cycle/invalid case detection.

---

### ✅ **Case 2: Disconnected Graph**

```python
words = ["z", "x", "a", "b"]
```

* Multiple isolated letters or chains, e.g., `z→x`, `a→b`.

**DFS**: Will handle multiple DFS calls to cover all nodes.
**BFS**: Will add multiple zero in-degree nodes to queue.

✅ **Both handle disconnected components** well.

---

### ✅ **Case 3: Multiple Valid Orders**

```python
words = ["abc", "abd", "abf"]
```

* `c→d`, `d→f`, but also possible `c→f` depending on order.

Both **DFS** and **BFS** will return *one valid topological ordering*.
Different runs may return different (but valid) results.

🟡 **Non-determinism** can differ slightly based on:

* DFS: order of adjacency list traversal
* BFS: queue order when multiple 0 in-degree nodes exist

---

## 🏁 Final Verdict

| Use Case                                           | Recommended Approach                        |
| -------------------------------------------------- | ------------------------------------------- |
| Want **iterative** and beginner-friendly           | ✅ **BFS (Kahn's)**                          |
| Need **custom ordering** or recursion is intuitive | ✅ **DFS**                                   |
| Deep graphs with high node count                   | ⚠️ Prefer **BFS** to avoid recursion limits |
| Debugging cycle detection clearly                  | ✅ **DFS** is often easier to visualize      |

---

Let me know if you want to benchmark both or add lexicographic ordering preference for multiple valid outputs!

