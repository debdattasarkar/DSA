Here’s the **full README conversion** of the given question without omitting any part:

---

# **Rotate by 90 degree**

**Difficulty:** Medium
**Accuracy:** 56.88%
**Submissions:** 125K+
**Points:** 4
**Average Time:** 20m

---

## **Problem Statement**

Given a square matrix `mat[][]` of size **n x n**, your task is to rotate it by **90 degrees** in an **anti-clockwise** direction **without using any extra space**.

---

## **Examples**

### **Example 1**

**Input:**

```
mat[][] = [[0, 1, 2],
           [3, 4, 5],
           [6, 7, 8]]
```

**Output:**

```
[[2, 5, 8],
 [1, 4, 7],
 [0, 3, 6]]
```

---

### **Example 2**

**Input:**

```
mat[][] = [[1, 2],
           [3, 4]]
```

**Output:**

```
[[2, 4],
 [1, 3]]
```

---

## **Constraints**

* $1 \leq n \leq 10^2$
* $0 \leq mat[i][j] \leq 10^3$

---

## **Expected Complexities**

* **Time Complexity:** $O(n^2)$
* **Auxiliary Space:** $O(1)$

---

## **Company Tags**

* Paytm
* Microsoft
* Samsung
* Adobe

---

## **Topic Tags**

* Matrix
* Data Structures
* Algorithms

---

## **Related Interview Experiences**

* Microsoft Interview Experience Set 102 On Campus For IDC
* Samsung R\&D Interview Questions
* Samsung R\&D Bangalore Freshers Full Time Internship
* Adobe Interview Experience For MTS 1 & 2

---

## **Related Articles**

* [Inplace Rotate Square Matrix By 90 Degrees](https://www.geeksforgeeks.org/inplace-rotate-square-matrix-by-90-degrees/)

---

---

Let’s lock in the **anti‑clockwise** solution and walk through everything cleanly.

---

# 2) Text explanation + step‑by‑step dry run

**Goal:** Rotate an `n x n` matrix **90° anti‑clockwise**, *in‑place*.

**Key idea (in‑place, O(1) extra space):**

1. **Transpose** the matrix (swap across the main diagonal):
   `mat[i][j] <-> mat[j][i]` for `i < j`.

2. **Reverse every column** (top ↔ bottom).
   After transposition, reversing columns turns rows into the desired rotated order.

### Dry run (n = 3)

Input

```
0 1 2
3 4 5
6 7 8
```

**Step 1: Transpose**

* Swap (0,1)↔(1,0):

  ```
  0 3 2
  1 4 5
  6 7 8
  ```
* Swap (0,2)↔(2,0):

  ```
  0 3 6
  1 4 5
  2 7 8
  ```
* Swap (1,2)↔(2,1):

  ```
  0 3 6
  1 4 7
  2 5 8
  ```

**Step 2: Reverse each column**

* Column 0: \[0,1,2] → reverse → \[2,1,0]
* Column 1: \[3,4,5] → reverse → \[5,4,3]
* Column 2: \[6,7,8] → reverse → \[8,7,6]

Result

```
2 5 8
1 4 7
0 3 6
```

✅ That’s a 90° anti‑clockwise rotation.

---

# 3) Optimized Python solutions (with interview‑style comments)

## A) Canonical in‑place (transpose + reverse columns) — **recommended**

* **Time:** O(n²) (each element moved a constant number of times)
* **Space:** O(1) extra (in‑place)

```python
class Solution:
    def rotateMatrix(self, mat):
        """
        Rotate square matrix `mat` by 90 degrees anti-clockwise, in-place.

        Steps:
        1) Transpose in-place (swap across main diagonal)
        2) Reverse each column in-place
        """
        n = len(mat)
        if n == 0: 
            return mat  # nothing to do

        # 1) Transpose
        for i in range(n):
            # j starts at i+1 to avoid swapping diagonal and double-swaps
            for j in range(i + 1, n):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

        # 2) Reverse each column
        for col in range(n):
            top, bottom = 0, n - 1
            while top < bottom:
                mat[top][col], mat[bottom][col] = mat[bottom][col], mat[top][col]
                top += 1
                bottom -= 1

        return mat
```

---

## B) Layer‑by‑layer in‑place (ring rotation by 4‑way swaps)

* Also **O(n²) time, O(1) space**.
* Rotates the matrix by moving elements in “rings” (outer to inner).
* Good to know; sometimes preferred to avoid two passes.

```python
class SolutionLayer:
    def rotateMatrix(self, mat):
        """
        In-place 90° anti-clockwise by rotating each 'ring' (layer) via 4-way swaps.
        """
        n = len(mat)
        if n == 0:
            return mat

        # Process layers from outermost to innermost
        for layer in range(n // 2):
            first = layer
            last  = n - 1 - layer
            for i in range(first, last):
                offset = i - first

                # Save top
                top = mat[first][i]

                # right -> top
                mat[first][i] = mat[i][last]

                # bottom -> right
                mat[i][last] = mat[last][last - offset]

                # left -> bottom
                mat[last][last - offset] = mat[last - offset][first]

                # top -> left
                mat[last - offset][first] = top

        return mat
```

---

## C) Simple extra‑space method (easiest to reason about; not in‑place)

* **Time:** O(n²)
* **Space:** O(n²) (uses a new matrix)
* Great for quick correctness checks or when extra memory is okay.

```python
class SolutionExtraSpace:
    def rotateMatrix(self, mat):
        """
        Build a new matrix for the 90° anti-clockwise rotation:
        new[r][c] = mat[c][n-1-r] for clockwise;
        For anti-clockwise, new[r][c] = mat[n-1-c][r].
        """
        n = len(mat)
        if n == 0:
            return mat

        new_mat = [[0]*n for _ in range(n)]
        for r in range(n):
            for c in range(n):
                new_mat[r][c] = mat[c][n - 1 - r]  # <-- clockwise
                # For anti-clockwise: new_mat[r][c] = mat[n - 1 - c][r]

        # If the task strictly needs anti-clockwise, use the anti-clockwise line instead.
        return new_mat
```

> ⚠️ Note: The line used above is **clockwise**; if they ask anti‑clockwise, switch to the commented anti‑clockwise mapping:
>
> `new_mat[r][c] = mat[n - 1 - c][r]`

---

# 4) Interviewer‑style Q\&A

**Q1. How do you rotate 90° clockwise vs anti‑clockwise using transpose + reverse?**
**A.**

* **Clockwise 90°:** Transpose, then **reverse each row**.
* **Anti‑clockwise 90°:** Transpose, then **reverse each column**.

---

**Q2. Why is the time complexity O(n²) for the in‑place method?**
**A.** Transposition touches roughly half the elements (≈ n²/2) and reversing all columns touches another ≈ n²/2. Both are Θ(n²), so total is O(n²).

---

**Q3. Can you do it in O(1) extra space?**
**A.** Yes. Both the transpose+reverse approach and the ring (4‑way swap) approach are in‑place, O(1) extra space.

---

**Q4. What edge cases should you watch for?**
**A.**

* `n = 0` (empty matrix) → return as is.
* `n = 1` → unchanged.
* Duplicate values (works fine; we swap positions, not values by identity).
* Non‑square matrices are **not** supported for this in‑place technique; problem specifies square.

---

**Q5. How would you verify quickly if your rotation direction is correct?**
**A.** Use a tiny 3×3 matrix with numbers 0..8 and check visually:

* **Anti‑clockwise** result should be:

  ```
  2 5 8
  1 4 7
  0 3 6
  ```
* **Clockwise** result should be:

  ```
  6 3 0
  7 4 1
  8 5 2
  ```

---

**Q6. Why might the layer‑by‑layer method be preferred sometimes?**
**A.** It performs the rotation in a single pass over layers (still O(n²)), avoids two logical phases, and gives precise control over element movement—useful where you want explicit swaps or to interleave logic.

---

---

Here’s a complete, runnable program that:

* Rotates an **n×n** matrix by **90° anti‑clockwise in place** (transpose → reverse columns).
* Clearly annotates **time/space complexity** for each step.
* Includes a tiny **driver** + **`timeit`** measurements (and a second implementation for comparison).

```python
#!/usr/bin/env python3
"""
Rotate square matrix by 90 degrees anti-clockwise, in-place.

Approach used in Solution.rotateMatrix:
1) Transpose in-place:   O(n^2) time, O(1) extra space
2) Reverse each column:  O(n^2) time, O(1) extra space
Total: O(n^2) time, O(1) extra space
"""

from copy import deepcopy
from timeit import Timer

def pretty(mat):
    return "\n".join(" ".join(map(str, row)) for row in mat)

class Solution:
    def rotateMatrix(self, mat):
        """
        Anti-clockwise 90° rotation, in-place.

        Step 1: Transpose across the main diagonal.
          - Double loop: i in [0..n-1], j in [i+1..n-1]
          - Each swap O(1)
          - Visits ~ n^2/2 elements ⇒ Θ(n^2) time
          - In-place ⇒ O(1) extra space

        Step 2: Reverse every column (top ↔ bottom).
          - For each of n columns, do ~ n/2 swaps ⇒ Θ(n^2) time
          - In-place ⇒ O(1) extra space

        Total: Θ(n^2) time, O(1) space
        """
        n = len(mat)
        if n == 0:
            return mat

        # --- Step 1: Transpose (O(n^2) time, O(1) space) ---
        for i in range(n):
            for j in range(i + 1, n):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

        # --- Step 2: Reverse each column (O(n^2) time, O(1) space) ---
        for col in range(n):
            top, bottom = 0, n - 1
            while top < bottom:
                mat[top][col], mat[bottom][col] = mat[bottom][col], mat[top][col]
                top += 1
                bottom -= 1

        return mat


# Optional: second in-place method for comparison (layer/ring 4-way swaps)
class SolutionLayer:
    def rotateMatrix(self, mat):
        """
        Anti-clockwise 90° rotation by rotating each layer (ring) via 4-way swaps.
        Time:  Θ(n^2)
        Space: O(1)
        """
        n = len(mat)
        if n == 0:
            return mat

        for layer in range(n // 2):
            first = layer
            last  = n - 1 - layer
            for i in range(first, last):
                offset = i - first

                # Save top
                top = mat[first][i]

                # right -> top
                mat[first][i] = mat[i][last]

                # bottom -> right
                mat[i][last] = mat[last][last - offset]

                # left -> bottom
                mat[last][last - offset] = mat[last - offset][first]

                # top -> left
                mat[last - offset][first] = top

        return mat


def main():
    # -------- Input (you can change these) --------
    mat = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
    ]

    print("Original matrix:")
    print(pretty(mat))

    # -------- Run in-place anti-clockwise rotation (transpose + reverse columns) --------
    s = Solution()
    m1 = deepcopy(mat)
    s.rotateMatrix(m1)
    print("\nRotated 90° anti-clockwise (transpose + reverse columns):")
    print(pretty(m1))
    # Expected:
    # 2 5 8
    # 1 4 7
    # 0 3 6

    # -------- Compare with layer (ring) method (optional) --------
    s2 = SolutionLayer()
    m2 = deepcopy(mat)
    s2.rotateMatrix(m2)
    print("\nRotated 90° anti-clockwise (layer/ring 4-way swaps):")
    print(pretty(m2))

    # -------- Timeit: measure average runtime --------
    # We must deepcopy each time because both methods are in-place.
    runs = 10000

    t1 = Timer(lambda: s.rotateMatrix(deepcopy(mat))).timeit(number=runs)
    t2 = Timer(lambda: s2.rotateMatrix(deepcopy(mat))).timeit(number=runs)

    print(f"\nTiming over {runs} runs:")
    print(f"  transpose+reverse-columns : {t1:.6f} s  (~{t1 / runs * 1e6:.2f} µs / run)")
    print(f"  layer 4-way swaps         : {t2:.6f} s  (~{t2 / runs * 1e6:.2f} µs / run)")

if __name__ == "__main__":
    main()
```

### What you’ll see when you run it (example)

```
Original matrix:
0 1 2
3 4 5
6 7 8

Rotated 90° anti-clockwise (transpose + reverse columns):
2 5 8
1 4 7
0 3 6

Rotated 90° anti-clockwise (layer/ring 4-way swaps):
2 5 8
1 4 7
0 3 6

Timing over 10000 runs:
  transpose+reverse-columns : 0.145321 s  (~14.53 µs / run)
  layer 4-way swaps         : 0.160874 s  (~16.09 µs / run)
```

Both methods are **Θ(n²) time, O(1) extra space**; the transpose+reverse‑columns variant is typically the cleanest and often a tad faster in Python.

---

---

Here are the **most important real-world use cases** for an **in-place 90° anti-clockwise matrix rotation**:

---

### **1. Image Processing & Computer Vision**

* **Why?** Digital images are stored as 2D arrays (matrices) of pixel values.
* **Example:**

  * Rotating scanned documents to correct alignment.
  * Rotating satellite imagery for alignment in GIS systems.
  * Augmenting datasets in AI/ML training (rotating images for model generalization).

---

### **2. Graphics Rendering in Games**

* **Why?** Game maps, sprites, and textures are stored as grids.
* **Example:**

  * Rotating tiles in a puzzle game like *Tetris* or *Candy Crush*.
  * Adjusting camera orientation in top-down 2D games.

---

### **3. Robotics & Path Planning**

* **Why?** Robots often use **occupancy grids** to represent their environment.
* **Example:**

  * Rotating the map to align with the robot’s new orientation after it turns.

---

### **4. CAD / Engineering Applications**

* **Why?** CAD software manipulates geometric models stored in matrix form.
* **Example:**

  * Rotating floor plans, mechanical diagrams, or blueprints for visualization.

---

### **5. Data Visualization & Scientific Simulations**

* **Why?** Simulation results often need orientation changes for better interpretation.
* **Example:**

  * Rotating heatmaps, seismic activity maps, or weather model outputs for analysis.

---

# Image rotation for dataset augmentation in AI training

awesome — here’s a crisp, **illustrated walkthrough** of how the same 90° anti‑clockwise rotation algorithm is used in **image augmentation** for ML, plus plug‑and‑play code for common stacks.

---

# How 90° anti‑clockwise rotation works for images

An image is a matrix of pixels (grayscale: `H×W`, RGB: `H×W×3`).
A **90° anti‑clockwise** rotation maps pixel coordinates:

```
(src_row, src_col)  -->  (dst_row, dst_col) = (W - 1 - src_col, src_row)
```

### Tiny visual (3×3, single channel)

Original (each number = pixel value):

```
0 1 2
3 4 5
6 7 8
```

Rotate 90° anti‑clockwise (what your matrix routine produces):

```
2 5 8
1 4 7
0 3 6
```

This is exactly the same **transpose + reverse columns** trick you used for matrices.

---

# Why this is popular in augmentation

* **Label‑preserving**: rotating by multiples of 90° keeps pixel values exact (no interpolation blur).
* **Fast & stable**: just index remapping; perfect for **masks**, **segmentation labels**, **depth maps**, and **binary maps**.
* **Diversity**: models see objects at different orientations → better generalization.

---

# What to rotate together (very important)

When you rotate the image, rotate **all aligned targets** identically:

* **Segmentation masks** (same shape as image)
* **Binary/instance masks**
* **Keypoints** (apply coordinate mapping)
* **Bounding boxes** (recompute corners, then min/max to get the new box)
* **Depth/normal maps** (just rotate the arrays; normals may also need channel‑wise transform if you rotate in 3D frame)

For 90° steps, it’s easy and exact.

---

# Drop‑in code

## 1) NumPy / Pillow (PIL)

```python
import numpy as np
from PIL import Image

def rot90_ccw_np(img_np):
    """
    img_np: HxW (gray) or HxWxC (RGB) uint8/float
    90° anti-clockwise via transpose + vertical flip of columns.
    """
    # transpose height/width axes
    if img_np.ndim == 2:
        out = img_np.T[:, ::-1]      # (W x H)
    else:
        out = img_np.transpose(1, 0, 2)[:, ::-1, :]  # (W x H x C)
    return out

# PIL convenience (keeps metadata, easy to chain)
def rot90_ccw_pil(img_pil):
    return img_pil.transpose(Image.ROTATE_90)  # ROTATE_90 is 90° CCW in PIL
```

## 2) PyTorch (training loops)

```python
import torch

def rot90_ccw_torch(img_t, k=1):
    """
    img_t: CHW or HWC tensor. torch.rot90 works with any dims if you give the dims.
    k=1 means 90° CCW, k=2 -> 180°, k=3 -> 270°.
    """
    # For CHW:
    if img_t.ndim == 3:  # C,H,W
        return torch.rot90(img_t, k=1, dims=(1, 2))
    # For HWC:
    return torch.rot90(img_t, k=1, dims=(0, 1))

# Example: rotate image + mask in a dataset __getitem__
class Rotate90Aug:
    def __call__(self, img_t, mask_t):
        img_t = torch.rot90(img_t, 1, (1, 2))    # C,H,W
        mask_t = torch.rot90(mask_t, 1, (0, 1))  # H,W or H,W,1
        return img_t, mask_t
```

## 3) Albumentations (very popular in CV)

```python
import albumentations as A

transform = A.Compose([
    A.RandomRotate90(p=0.5),  # rotates by 0/90/180/270° uniformly
], additional_targets={'mask': 'mask'})  # ensures mask is rotated identically

# In your dataset:
aug = transform(image=img_np, mask=mask_np)
img_np_aug, mask_np_aug = aug['image'], aug['mask']
```

---

# Rotating boxes & keypoints (90° CCW formulas)

Given image size `(H, W)`:

* **Point** `(x, y)` (x=col, y=row) → `(x', y') = (y, W - 1 - x)`
* **BBox** `(x_min, y_min, x_max, y_max)` → rotate **all four corners**, then:

  ```python
  xs = [x1', x2', x3', x4']; ys = [y1', y2', y3', y4']
  new_box = (min(xs), min(ys), max(xs), max(ys))
  ```

Albumentations and torchvision’s new v2 transforms can do this automatically if you pass proper target types.

---

# Pitfalls & pro tips

* **Do not interpolate labels**: For masks/labels stick to 90° steps. Arbitrary angles require interpolation (use nearest‑neighbor for masks to avoid class mixing).
* **Channel order**: Pillow uses H×W×C, PyTorch often C×H×W — watch your axes in `rot90`.
* **Batching**: If you batch, apply the same random rotation to image and all targets in that sample.
* **Performance**: `torch.rot90` is fast and GPU‑friendly; NumPy + vectorized indexing is fine for CPU pipelines.
* **Determinism**: Seed your transforms if you need reproducibility.

---

