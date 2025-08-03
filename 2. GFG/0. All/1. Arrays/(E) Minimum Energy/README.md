To solve the **Minimum Energy** problem, the key idea is to ensure that at no point while traversing the checkpoints the energy drops to `0` or below. So we need to **track the cumulative energy** and make sure the **lowest point it ever drops to** is compensated by the initial energy.

---

### ✅ Problem Summary

* Given an array of positive and negative integers representing energy gain/loss at checkpoints.
* We need to find the **minimum initial energy** such that energy never falls to `0` or below.

---

### 🔍 Dry Run

#### Example:

`arr = [4, -10, 4, 4, 4]`

We simulate the energy level starting from some `x`, and ensure it stays > 0.

Track cumulative energy:

* After index 0: 4
* After index 1: -6
* After index 2: -2
* After index 3: 2
* After index 4: 6

**Minimum cumulative sum = -6**
→ We need at least `7` energy initially to stay above 0 (i.e. 1 more than 6).

---

### ✅ Logic

1. Traverse array and track `cumulative sum`.
2. Track the **minimum value** reached in cumulative sum.
3. Return `max(1, 1 - min_cumulative)`.

---

### ✅ Python Code (with inline comments)

```python
class Solution:
    def minEnergy(self, arr):
        energy = 0       # Cumulative energy level
        min_energy = 0   # Track the lowest point of energy

        for value in arr:
            energy += value
            min_energy = min(min_energy, energy)  # Update lowest energy seen

        # We need at least 1 more than the lowest point
        return abs(min_energy) + 1
```

---

### ✅ C++ Code

```cpp
class Solution {
  public:
    int minEnergy(vector<int>& a) {
        int energy = 0, min_energy = 0;

        for (int val : a) {
            energy += val;
            min_energy = min(min_energy, energy);
        }

        return abs(min_energy) + 1;
    }
};
```

---

### ✅ JavaScript Code

```javascript
class Solution {
    minEnergy(a) {
        let energy = 0, min_energy = 0;

        for (let i = 0; i < a.length; i++) {
            energy += a[i];
            min_energy = Math.min(min_energy, energy);
        }

        return Math.abs(min_energy) + 1;
    }
}
```

---

### ✅ Time and Space Complexity

* **Time:** O(n)
* **Space:** O(1)

Would you like a visual diagram of the energy changes over the checkpoints?
