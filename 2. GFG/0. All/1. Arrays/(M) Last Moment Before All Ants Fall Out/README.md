
---

# 🐜 Last Moment Before All Ants Fall Out

**Difficulty:** Medium
**Accuracy:** 71.54%
**Submissions:** 8K+
**Points:** 4

---

## 🧠 Problem Description

We have a **wooden plank** of length **n** units. Some ants are walking on the plank, each ant moves with a speed of **1 unit per second**, with some moving **left** and others **right**.

> 🌀 When two ants moving in two different directions meet at some point, they **change their directions** and continue moving again.
>
> * **Note:** Changing direction **does not take any extra time**.

When an ant reaches one end of the plank at a time `t`, it falls **off the plank immediately**.

---

## 🔧 Task

Given:

* an integer `n`
* two integer arrays `left[]` and `right[]`
  representing the positions of the ants moving **to the left** and **to the right**, respectively,
  your task is to **return the time when the last ant(s) fall off the plank**.

---

## 📌 Examples

### ➤ Example 1:

**Input:**

```
n = 4
left[] = [2]
right[] = [0, 1, 3]
```

**Output:**

```
4
```

**Explanation:**

```
T=0: Ants at [0,1,2,3]
T=1: Ant at 0 falls; rest move
T=4: Last ant falls off
```

As seen in the image, the **last ant falls off the plank at time = 4**.

---

### ➤ Example 2:

**Input:**

```
n = 4
left[] = []
right[] = [0, 1, 2, 3, 4]
```

**Output:**

```
4
```

**Explanation:**

All ants are moving **right**, so the ant that starts at index 0 takes **4 seconds** to reach the right edge.

---

### ➤ Example 3:

**Input:**

```
n = 3
left[] = [0]
right[] = [3]
```

**Output:**

```
0
```

**Explanation:**

The ants are already at the edges (0 and 3), so they fall off **immediately at time = 0**.

---

## 📏 Constraints

* $1 \leq n \leq 10^5$
* $0 \leq \text{left.length}, \text{right.length} \leq n + 1$
* $0 \leq \text{left}[i], \text{right}[i] \leq n$
* $1 \leq \text{left.length} + \text{right.length} \leq n + 1$
* All values in `left` and `right` are unique, and no value appears in both.

---

## 🧠 Expected Complexity

* **Time Complexity:** O(n + m)
* **Auxiliary Space:** O(1)

---

## 🏷️ Tags

* Greedy
* Arrays

---

## 🏢 Company Tags

* Google

---

## 🔗 Related Articles

* [Last Moment Before All Ants Fall Out Of A Plank (GeeksforGeeks)](https://www.geeksforgeeks.org)

---

---

Here’s the **complete breakdown** for the problem **“Last Moment Before All Ants Fall Out”**:

---

## ✅ 2. Explanation + Step-by-Step Dry Run

### 🧠 Key Insight:

When ants **meet**, they **just swap directions** and continue walking — i.e., **the final result is the same as if they passed through each other**. So, we can **ignore collisions entirely**.

> For ants moving left:
> They fall at time = their starting position (distance to 0).
> For ants moving right:
> They fall at time = (n - their position) (distance to n).

---

### 💡 Final Answer:

The **maximum** time taken by any ant to fall off the plank =
`max(max(left), n - min(right))`

---

### 🧪 Dry Run Example:

#### Input:

```
n = 4
left = [2]
right = [0, 1, 3]
```

#### Simulation:

* Ant at 2 going left takes `2` seconds to fall.
* Ant at 0 → time = 4 (to reach end).
* Ant at 1 → time = 3
* Ant at 3 → time = 1

Final time = `max(2, 4, 3, 1) = 4`

✅ **Output = 4**

---

## ✅ 3. Optimized Python Code (Most Interview-Expected Way)

```python
import time

class Solution:
    def getLastMoment(self, n, left, right):
        """
        Time Complexity: O(n)  — where n = max(len(left), len(right))
        Space Complexity: O(1) — No extra space used apart from constants
        """
        # Max time for ants going left is their distance from 0
        left_max = max(left) if left else 0
        
        # Max time for ants going right is their distance from n
        right_max = n - min(right) if right else 0
        
        # The ant that takes longest to fall off
        return max(left_max, right_max)

# -------- Main Execution with timeit --------
if __name__ == "__main__":
    arr_n = 4
    left = [2]
    right = [0, 1, 3]

    start_time = time.time()

    sol = Solution()
    result = sol.getLastMoment(arr_n, left, right)

    end_time = time.time()
    
    print("Input:")
    print(f"n = {arr_n}, left = {left}, right = {right}")
    print("Output:", result)
    print("Execution Time: {:.6f} sec".format(end_time - start_time))
```

---

## ✅ 4. Interviewer-Expected Q\&A

### Q1: Why can we ignore direction changes when ants meet?

**A:** Because direction change is instantaneous and symmetric — ants essentially swap identities. So the outcome is the same as if they passed through each other.

---

### Q2: What’s the time complexity?

**A:**

* `O(len(left) + len(right))` to compute max/min — but this is usually bounded by `O(n)`
* So effectively **linear time**.

---

### Q3: What are the edge cases?

* No ants on one side (`left = []` or `right = []`)
* Ants already at edge (`0` or `n`)
* Large `n` values with sparse ant distribution

---

### Q4: What if ants had varying speeds?

**A:** Then simulation would be needed. This greedy shortcut wouldn’t work.

---

### Q5: Real-world analog?

* **Robots on a conveyor belt** switching roles
* **Traffic simulation** where vehicles swap paths

---

---

Here are a **few important real-world use cases** inspired by the **“Last Moment Before All Ants Fall Out”** problem:

---

## 🔧 Real-World Use Cases

### 1. **Robot Movement on Conveyor Belts / Assembly Lines**

* **Scenario**: Multiple autonomous robots move along a narrow track.
* If two robots cross paths, they can **swap identifiers or payloads** and continue.
* **Application**: Optimizing delivery time for items on manufacturing belts or warehouse tracks (e.g., Amazon robotics).
* The problem helps calculate **maximum clearance time**.

---

### 2. **Evacuation Modeling / Emergency Exits**

* **Scenario**: People or agents moving in opposite directions along a narrow corridor.
* **Insight**: Models the time required for all agents to exit, assuming **direction switches don't affect time**.
* Helps in **evacuation drills**, **crowd simulation**, and **disaster management**.

---

### 3. **Packet Routing in Network Switches**

* **Scenario**: Packets moving left/right in a switching fabric.
* Packets may reverse direction due to collision or rerouting but ultimately reach an exit.
* This model helps in **estimating buffer flush times**, worst-case delays.

---

### 4. **Autonomous Vehicle Pathing**

* In narrow lanes or tunnels, **AVs moving in opposite directions** may have to switch or "yield" in logic — this mirrors ants swapping directions.
* Useful in **coordinating AV swarms** in bidirectional narrow corridors.

---

### 5. **Genetics or Molecular Simulation**

* Particles or agents moving on a chain (like DNA) and colliding or switching paths.
* Used in **biophysical simulations** where molecule direction or protein interactions are modeled.

---
