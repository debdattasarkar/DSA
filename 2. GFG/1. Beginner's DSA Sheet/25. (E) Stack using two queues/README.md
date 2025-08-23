
Here’s the full **README-style conversion** of the problem statement in your screenshot (“Stack using two queues”), with **no part omitted**:

---

# Stack using Two Queues

**Difficulty:** Easy
**Accuracy:** 51.4%
**Submissions:** 152K+
**Points:** 2
**Average Time:** 20m

---

## Problem Statement

Implement a **Stack** using two queues `q1` and `q2`.

---

## Examples

### Example 1

**Input:**

```
push(2)
push(3)
pop()
push(4)
pop()
```

**Output:**

```
3 4
```

**Explanation:**

* `push(2)` → stack will be `[2]`
* `push(3)` → stack will be `[2, 3]`
* `pop()` → popped element will be `3`, stack will be `[2]`
* `push(4)` → stack will be `[2, 4]`
* `pop()` → popped element will be `4`

---

### Example 2

**Input:**

```
push(2)
pop()
pop()
push(3)
```

**Output:**

```
2 -1
```

**Explanation:**

* `push(2)` → stack will be `[2]`
* `pop()` → popped element will be `2`
* `pop()` → stack is empty, so popped element will be `-1`
* `push(3)` → stack will be `[3]`

---

## Constraints

* `1 <= Number of queries <= 100`
* `1 <= size of stack <= 100`

---

## Expected Complexities

* **Time Complexity:**

  * `O(n)` for `push()` and `O(1)` for `pop()` (or vice-versa).
* **Auxiliary Space:**

  * `O(1)` for both `push()` and `pop()`.

---

## Company Tags

* Accolite
* Amazon
* Microsoft
* OYO Rooms
* Snapdeal
* D-E-Shaw
* Oracle
* Adobe
* Cisco
* Grofers
* CouponDunia
* Kritikal Solutions

---

## Topic Tags

* Stack
* Queue
* Design-Pattern
* Data Structures

---

## Related Articles

* [Implement Stack Using Queue](https://www.geeksforgeeks.org/implement-stack-using-queue/)

---

---

Got it — if **this exact free‑function + `queue.Queue`** version is what GFG’s runner accepts for your problem, you’re good. Your implementation is the standard **costly‑push / cheap‑pop** approach and it’s correct.

A couple of small, practical tweaks that make it more robust on GFG (especially when there are **multiple test cases in one run**, which can leak globals):

* Add a tiny `init()` to **reset** the two queues at the start of each test.
* Keep `global` declarations **at the top** of each function (you already do this).
* Keep the interface exactly as GFG expects: `push(x)` / `pop()`.

Here’s your code with only the safe reset helper added and tiny cleanup (no logic changes):

```python
from queue import Queue

# Global queues (GFG free-function style)
queue_1 = Queue()  # first queue
queue_2 = Queue()  # second queue

def init():
    """
    Optional: call this once per test case (if your driver allows)
    to avoid leaking state across tests.
    """
    global queue_1, queue_2
    # Re-create queues because queue.Queue has no .clear()
    queue_1 = Queue()
    queue_2 = Queue()

'''
    :param x: value to be inserted
    :return: None
'''
def push(x):
    global queue_1, queue_2

    # Step 1: Push new element into queue_2
    # Time: O(1), Space: O(1)
    queue_2.put(x)

    # Step 2: Move all elements from queue_1 to queue_2
    # Time: O(n), Space: O(1)
    while not queue_1.empty():
        queue_2.put(queue_1.get())

    # Step 3: Swap the queues
    # Time: O(1), Space: O(1)
    queue_1, queue_2 = queue_2, queue_1


def pop():
    global queue_1, queue_2

    # If queue_1 is empty, the stack is empty
    if queue_1.empty():
        return -1

    # The front of queue_1 is the top of the stack
    # Time: O(1), Space: O(1)
    return queue_1.get()
```

### Why this passes on GFG

* Matches the **free‑function** API exactly.
* Uses `queue.Queue` (which GFG often wires in its own driver).
  (For pure DSA code we usually prefer `collections.deque`, but if GFG’s judge is happy with `queue.Queue`, stick with it.)
* `init()` prevents the “mystery extra value” issue when multiple test cases share the same Python process.

### Tiny FAQ

* **Why not `deque`?** It’s usually faster and simpler (`append`/`popleft` O(1)), but some GFG stubs internally use `queue.Queue`; since this works for you, keep it.
* **What if I can’t call `init()`?** If the judge doesn’t expose a place to call it per test, your current code still works for a **single** test case. If you see stray outputs again, the driver likely ran multiple tests in one process—then a **class‑based** solution is safer (fresh object per test case).

