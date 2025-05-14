Here's a **step-by-step explanation with dry run** and complete solutions for the **"Snake and Ladder Problem"** from GeeksforGeeks in **Python, C++, and JavaScript**, with inline logic comments.

---

### 🔍 Problem Summary:

You are given a board of size `30`, and `N` snakes or ladders represented as an array of `2*N` size:

* For every ladder or snake, `arr[2*i]` is the start and `arr[2*i + 1]` is the end.

**Goal:** Find the **minimum number of dice throws** required to reach the last cell (cell 30) starting from cell 1.

---

### 🧠 Dry Run of Example

**Input:**
`N = 8`
`arr = [3, 22, 5, 8, 11, 26, 20, 29, 17, 4, 19, 7, 27, 1, 21, 9]`

**Explanation:**

* There are ladders and snakes that either move you forward (ladder) or backward (snake).
* Use **BFS traversal** to find the shortest path (min throws) from 1 to 30.

**Output:** `3`
**Reason:**

* Throw 1: Roll a 2 → move to cell 3 → ladder to 22
* Throw 2: Roll a 6 → move to 28
* Throw 3: Roll a 2 → reach 30

---

### ✅ Python Code

```python
from collections import deque

class Solution:
    def minThrow(self, N, arr):
        # Build board mapping with ladders and snakes
        board = list(range(31))  # board[0] unused, board[i] = i by default
        for i in range(0, 2 * N, 2):
            board[arr[i]] = arr[i + 1]  # map start -> end

        visited = [False] * 31
        q = deque()
        q.append((1, 0))  # (current position, throw count)
        visited[1] = True

        while q:
            pos, throws = q.popleft()

            # Try all dice rolls from 1 to 6
            for die in range(1, 7):
                next_pos = pos + die
                if next_pos <= 30:
                    final_pos = board[next_pos]  # Apply snake/ladder
                    if final_pos == 30:
                        return throws + 1
                    if not visited[final_pos]:
                        visited[final_pos] = True
                        q.append((final_pos, throws + 1))
        return -1
```

---

### ✅ C++ Code

```cpp
class Solution {
  public:
    int minThrow(int N, int arr[]) {
        vector<int> board(31);
        for (int i = 1; i <= 30; i++) board[i] = i;

        // Apply ladders and snakes
        for (int i = 0; i < 2 * N; i += 2)
            board[arr[i]] = arr[i + 1];

        vector<bool> visited(31, false);
        queue<pair<int, int>> q;
        q.push({1, 0});
        visited[1] = true;

        while (!q.empty()) {
            int pos = q.front().first;
            int throws = q.front().second;
            q.pop();

            for (int die = 1; die <= 6; die++) {
                int next = pos + die;
                if (next <= 30) {
                    int finalPos = board[next];
                    if (finalPos == 30) return throws + 1;
                    if (!visited[finalPos]) {
                        visited[finalPos] = true;
                        q.push({finalPos, throws + 1});
                    }
                }
            }
        }
        return -1;
    }
};
```

---

### ✅ JavaScript Code

```javascript
class Solution {
    minThrow(arr, n) {
        let board = Array(31).fill(0).map((_, i) => i);
        
        for (let i = 0; i < 2 * n; i += 2) {
            board[arr[i]] = arr[i + 1];
        }

        let visited = Array(31).fill(false);
        let queue = [[1, 0]];
        visited[1] = true;

        while (queue.length > 0) {
            let [pos, throws] = queue.shift();

            for (let die = 1; die <= 6; die++) {
                let next = pos + die;
                if (next <= 30) {
                    let finalPos = board[next];
                    if (finalPos === 30) return throws + 1;
                    if (!visited[finalPos]) {
                        visited[finalPos] = true;
                        queue.push([finalPos, throws + 1]);
                    }
                }
            }
        }
        return -1;
    }
}
```

---

### ⏱ Time & Space Complexity

* **Time Complexity:** `O(N)` — since board size is constant and BFS explores at most 30 cells.
* **Space Complexity:** `O(N)` — to maintain visited array and board mapping.

---

Let me know if you'd like a visualization of the BFS tree or a custom test case breakdown!
