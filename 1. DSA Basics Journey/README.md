
---

# 📘 DSA Problem Solving Techniques Cheat Sheet

A quick reference to the most common techniques used to solve algorithmic and data structure problems.

---

## 🔍 Search Techniques

* **Binary Search**
  Find an element in a sorted array in `O(log n)` time.
  *Example*: Search a target in a rotated sorted array.

* **Ternary Search**
  Used to find the minimum or maximum of a unimodal function.
  *Example*: Optimize a convex cost function.

---

## 🪟 Window and Pointer Techniques

* **Two Pointer**
  Use left and right pointers to find pairs, subarrays, etc.
  *Example*: Two sum in sorted array.

* **Sliding Window**
  Maintain a window of elements for fixed/variable-length problems.
  *Example*: Longest substring without repeating characters.

* **Fast and Slow Pointers (Tortoise & Hare)**
  Detect cycles in linked lists or arrays.
  *Example*: Detect cycle in linked list.

---

## 🔁 Recursion & Backtracking

* **Basic Recursion**
  Solve subproblems recursively.
  *Example*: Tower of Hanoi.

* **Backtracking**
  Try all possibilities and backtrack if invalid.
  *Example*: N-Queens, Sudoku Solver.

* **Memoized Recursion**
  Cache previous calls to avoid recomputation.
  *Example*: Fibonacci with memoization.

---

## 📚 Dynamic Programming (DP)

* **Top-down (Memoization)**
  Recursive + cache for overlapping subproblems.

* **Bottom-up (Tabulation)**
  Iterative DP to build up the answer.
  *Example*: 0/1 Knapsack, LIS.

* **Bitmask DP**
  Used when the state depends on subsets.
  *Example*: Traveling Salesman Problem (TSP).

---

## 📈 Greedy Algorithms

* **Interval Scheduling**
  Select max number of non-overlapping intervals.

* **Coin Change (Greedy)**
  Works if coin denominations are canonical.

* **Huffman Coding**
  Optimal prefix code generation.

---

## ⛓ Divide and Conquer

* **Divide, Solve, Combine**
  *Example*: Merge Sort, Quick Sort.

* **2D Problems**
  *Example*: Closest pair of points.

---

## 🌐 Graph Algorithms

* **DFS / BFS**
  Traverse or search nodes.

* **Topological Sort**
  Ordering for DAGs.

* **Dijkstra’s Algorithm**
  Shortest path with non-negative weights.

* **Union-Find (DSU)**
  Track components for Kruskal’s MST.

---

## 🌲 Tree Techniques

* **DFS Traversals**
  Inorder / Preorder / Postorder.

* **Level-order (BFS)**
  Using a queue.

* **Lowest Common Ancestor**
  Binary lifting or Euler tour.

* **Segment Tree / BIT**
  Efficient range queries and updates.

---

## 📦 Heap / Priority Queue

* **Kth Largest Element**
  Min-heap of size k.

* **Merging Sorted Lists**
  Use a min-heap for efficiency.

---

## 🧮 Mathematical Techniques

* **Prefix Sum / Difference Array**
  O(1) range queries or updates.

* **Modular Arithmetic**
  Avoid overflow, handle divisibility.

* **Sieve of Eratosthenes**
  Prime generation up to n.

---

## 🧩 Hashing Techniques

* **Hash Maps / Sets**
  Fast lookup and frequency count.

* **Rolling Hash**
  Pattern matching (Rabin-Karp).

---

## 🔣 Bit Manipulation

* **XOR Tricks**
  Find unique elements.

* **Bitmasking**
  Represent subsets and flags.

---

## 🔃 Sorting-Based Techniques

* **Sort + Logic**
  Apply two-pointer or greedy logic post-sort.

* **Custom Comparators**
  Useful in greedy scheduling.

---

## 🧵 Trie / Prefix Tree

* **Prefix Matching**
  Efficient for dictionaries, autocomplete.

* **Word Filters**
  Check word prefixes/suffixes quickly.

---

## 📉 Monotonic Stack / Queue

* **Next Greater/Smaller Element**
  Use stack for O(n) solutions.

* **Largest Rectangle in Histogram**
  Classic stack problem.

---

## 🔄 Simulation & State Machines

* **Emulate Step-by-Step**
  *Example*: Game of Life, finite automata.

---

## 🧠 Constraint Propagation

* **Reduce Possibilities Early**
  *Example*: Sudoku with forward checking.

---

