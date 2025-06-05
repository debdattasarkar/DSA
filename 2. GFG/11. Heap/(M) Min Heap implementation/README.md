# Min Heap Implementation

## Problem Statement

Given a **priority queue (min heap)** and **Q** queries to be performed on it, the task is to perform operations based on the following types of queries:

* `p x`: Push element `x` into the priority queue and print the **size**.
* `pp`: Pop the top element from the priority queue and print the **size**.
* `t`: Return the **top element** of the priority queue. If empty, return `-1`.

---

## Example

**Input:**

```
Q = 5  
Queries:  
p 5  
p 3  
p 1  
t  
pp
```

**Output:**

```
1  
2  
3  
1  
2
```

**Explanation:**

* Pushing 5 → Queue: \[5], Size: 1
* Pushing 3 → Queue: \[3, 5], Size: 2
* Pushing 1 → Queue: \[1, 5, 3], Size: 3
* `t` → Top element is 1 (min heap property)
* `pp` → Pop 1, Queue becomes \[3, 5], Size: 2

---

## Constraints

* 1 ≤ Q ≤ 100

---

## Expected Time & Space Complexities

* **Time Complexity:** O(Q \* log(n))
* **Auxiliary Space:** O(1)

---

## Tags

`STL` `Data Structures` `Heap`

---

## C++ Function Signatures

```cpp
// Push element to priority_queue
void push(priority_queue<int, vector<int>, greater<int>> &pq, int x);

// Pop top element from priority_queue
void pop(priority_queue<int, vector<int>, greater<int>> &pq);

// Return top element of priority_queue or -1 if empty
int top(priority_queue<int, vector<int>, greater<int>> &pq);
```

---

## C++ Sample Implementation

```cpp
#include <queue>
using namespace std;

void push(priority_queue<int, vector<int>, greater<int>> &pq, int x) {
    pq.push(x);
}

void pop(priority_queue<int, vector<int>, greater<int>> &pq) {
    if (!pq.empty()) {
        pq.pop();
    }
}

int top(priority_queue<int, vector<int>, greater<int>> &pq) {
    return pq.empty() ? -1 : pq.top();
}
```

---

## Python Equivalent

```python
import heapq

pq = []

def push(pq, x):
    heapq.heappush(pq, x)
    return len(pq)

def pop(pq):
    if pq:
        heapq.heappop(pq)
    return len(pq)

def top(pq):
    return pq[0] if pq else -1
```

---

## JavaScript Equivalent

```javascript
class MinHeap {
    constructor() {
        this.heap = [];
    }

    push(x) {
        this.heap.push(x);
        this.bubbleUp();
        return this.heap.length;
    }

    pop() {
        if (this.heap.length === 0) return 0;
        const min = this.heap[0];
        const end = this.heap.pop();
        if (this.heap.length > 0) {
            this.heap[0] = end;
            this.sinkDown();
        }
        return this.heap.length;
    }

    top() {
        return this.heap.length > 0 ? this.heap[0] : -1;
    }

    bubbleUp() {
        let i = this.heap.length - 1, element = this.heap[i];
        while (i > 0) {
            let parentIdx = Math.floor((i - 1) / 2);
            if (this.heap[parentIdx] <= element) break;
            this.heap[i] = this.heap[parentIdx];
            i = parentIdx;
        }
        this.heap[i] = element;
    }

    sinkDown() {
        let i = 0, length = this.heap.length;
        const element = this.heap[0];

        while (true) {
            let leftIdx = 2 * i + 1, rightIdx = 2 * i + 2, swap = null;

            if (leftIdx < length && this.heap[leftIdx] < element) {
                swap = leftIdx;
            }

            if (rightIdx < length && this.heap[rightIdx] < (swap === null ? element : this.heap[leftIdx])) {
                swap = rightIdx;
            }

            if (swap === null) break;

            this.heap[i] = this.heap[swap];
            i = swap;
        }

        this.heap[i] = element;
    }
}
```

---

Would you like this in a downloadable format or extended to support interactive CLI testing?


Here’s a quick breakdown and confirmation that everything is in order:

---

### ✅ Final Correct Code

```cpp
/* Function to implement push operation in priority_queue
 * pq : priority_queue
 * x : element to be pushed
 */
void push(priority_queue<int, vector<int>, greater<int>> &pq, int x) {
    pq.push(x); // Insert x into the min-heap
}

/* Function to implement pop operation in priority_queue
 * pq : priority_queue
 */
void pop(priority_queue<int, vector<int>, greater<int>> &pq) {
    if (!pq.empty()) {
        pq.pop(); // Remove smallest element from heap
    }
    // No action needed if empty
}

/* Function to implement top operation in priority_queue
 * pq : priority_queue
 */
int top(priority_queue<int, vector<int>, greater<int>> &pq) {
    if (!pq.empty()) {
        return pq.top(); // Return smallest element
    } else {
        return -1; // If empty, return -1
    }
}
```

---

### 🧪 Behavior Summary

* **`push(x)`**: Adds `x` to the min-heap.
* **`pop()`**: Removes the top (smallest) if available.
* **`top()`**: Returns the top (smallest) value or `-1` if empty.

---

### 🧵 Integration in Full Driver Code (Example)

If you're running this in a competitive programming platform (like GeeksforGeeks):

```cpp
int main() {
    int Q;
    cin >> Q;

    priority_queue<int, vector<int>, greater<int>> pq;

    for (int i = 0; i < Q; ++i) {
        string op;
        cin >> op;

        if (op == "p") {
            int x;
            cin >> x;
            push(pq, x);
            cout << pq.size() << endl;
        } else if (op == "pp") {
            pop(pq);
            cout << pq.size() << endl;
        } else if (op == "t") {
            cout << top(pq) << endl;
        }
    }
    return 0;
}
```

Here are equivalent implementations of the **Min Heap operations (`push`, `pop`, `top`)** in **Python** and **JavaScript**, using appropriate data structures to simulate a **min-heap**:

---

## ✅ Python Version (Using `heapq` for Min Heap)

```python
import heapq

# Initialize an empty list as min heap
pq = []

def push(pq, x):
    """Push x to the heap and return its size"""
    heapq.heappush(pq, x)
    return len(pq)

def pop(pq):
    """Pop top from heap and return new size"""
    if pq:
        heapq.heappop(pq)
    return len(pq)

def top(pq):
    """Return the smallest element or -1 if empty"""
    return pq[0] if pq else -1

# Example simulation
queries = ["p 5", "p 3", "p 1", "t", "pp"]
pq = []

for q in queries:
    if q.startswith("p "):  # push operation
        _, val = q.split()
        print(push(pq, int(val)))
    elif q == "pp":
        print(pop(pq))
    elif q == "t":
        print(top(pq))
```

### ✅ Sample Output (same as C++):

```
1
2
3
1
2
```

---

## ✅ JavaScript Version (Min Heap Implementation)

JavaScript doesn’t have a native priority queue, so we use a custom class:

```javascript
class MinHeap {
    constructor() {
        this.heap = [];
    }

    push(val) {
        this.heap.push(val);
        this._bubbleUp(this.heap.length - 1);
        return this.heap.length;
    }

    pop() {
        if (this.heap.length === 0) return 0;
        const min = this.heap[0];
        const end = this.heap.pop();
        if (this.heap.length > 0) {
            this.heap[0] = end;
            this._sinkDown(0);
        }
        return this.heap.length;
    }

    top() {
        return this.heap.length > 0 ? this.heap[0] : -1;
    }

    _bubbleUp(index) {
        const val = this.heap[index];
        while (index > 0) {
            const parentIdx = Math.floor((index - 1) / 2);
            const parent = this.heap[parentIdx];
            if (val >= parent) break;
            this.heap[index] = parent;
            index = parentIdx;
        }
        this.heap[index] = val;
    }

    _sinkDown(index) {
        const length = this.heap.length;
        const val = this.heap[index];
        while (true) {
            let left = 2 * index + 1;
            let right = 2 * index + 2;
            let smallest = index;

            if (left < length && this.heap[left] < this.heap[smallest]) smallest = left;
            if (right < length && this.heap[right] < this.heap[smallest]) smallest = right;

            if (smallest === index) break;
            [this.heap[index], this.heap[smallest]] = [this.heap[smallest], this.heap[index]];
            index = smallest;
        }
    }
}

// Example usage
const heap = new MinHeap();
console.log(heap.push(5)); // 1
console.log(heap.push(3)); // 2
console.log(heap.push(1)); // 3
console.log(heap.top());   // 1
console.log(heap.pop());   // 2
```

---
