
---

# 📚 Implement Stack using Array

### 💡 Difficulty: Basic

**Accuracy:** 54.76%
**Submissions:** 281K+
**Points:** 1
**Average Time:** 25 mins

---

## 🔍 Problem Statement

Write a program to implement a Stack using Array. Your task is to use the class as shown in the comments and complete the functions `push()` and `pop()` to implement a stack.

* The `push(x)` method takes one argument `x` to be pushed into the stack.
* The `pop()` method returns the top element and removes it from the stack. If the stack is empty, return `-1`.

---

### 📥 Note:

The input is given in the form of queries:

* `1 x` → Push `x` into the stack
* `2` → Pop from the stack and print the popped element

---

## 📘 Examples

### Example 1:

```
Input: 1 2 1 3 2 1 4 2  
Output: 3, 4  
Explanation:
push(2) → Stack: [2]  
push(3) → Stack: [2, 3]  
pop()   → 3 → Stack: [2]  
push(4) → Stack: [2, 4]  
pop()   → 4 → Stack: [2]
```

---

### Example 2:

```
Input: 2 1 4 1 5 2  
Output: -1, 5  
Explanation:
pop()   → -1 (stack is empty)  
push(4) → Stack: [4]  
push(5) → Stack: [4, 5]  
pop()   → 5 → Stack: [4]
```

---

## 📊 Constraints

* `1 ≤ number of calls made to push, pop ≤ 100`
* `1 ≤ x ≤ 100`

---

## ⏱ Expected Complexities

* **Time Complexity:** `O(1)` for both `push()` and `pop()`
* **Auxiliary Space:** `O(1)`

---

## 🧠 Explanation with Dry Run

Suppose input is:

```
1 10 1 20 2 1 30 2
```

Operations step-by-step:

* `1 10` → push(10) → Stack: `[10]`
* `1 20` → push(20) → Stack: `[10, 20]`
* `2`    → pop() → returns 20 → Stack: `[10]`
* `1 30` → push(30) → Stack: `[10, 30]`
* `2`    → pop() → returns 30 → Stack: `[10]`

**Output:** `20, 30`

---

## ✅ Optimized Code Implementations

---

### 🐍 Python

```python
class MyStack:
    
    def __init__(self):
        self.arr = []  # Using Python list to simulate stack
    
    # Function to push an integer into the stack.
    def push(self, data):
        self.arr.append(data)  # Add element to end
    
    # Function to remove an item from top of the stack.
    def pop(self):
        if not self.arr:
            return -1  # Stack is empty
        return self.arr.pop()  # Removes and returns top element
```

---

### 💠 C++

```cpp
class MyStack {
private:
    int arr[1000];  // Fixed-size array for stack
    int top;        // Points to the top element

public:
    MyStack() { top = -1; }

    void push(int x) {
        if (top < 999)  // Prevent overflow
            arr[++top] = x;
    }

    int pop() {
        if (top == -1) return -1;  // Stack is empty
        return arr[top--];         // Return top and decrement
    }
};
```

---

### 🌐 JavaScript

```javascript
function MyStack() {
    this.arr = [];
}

// Function to push an integer into the stack.
MyStack.prototype.push = function(x) {
    this.arr.push(x);  // Push at end
};

// Function to remove an item from top of the stack.
MyStack.prototype.pop = function() {
    if (this.arr.length === 0) return -1;  // Stack is empty
    return this.arr.pop();  // Pop from end
};
```

---

## 💬 Expected Interview Questions & Answers

---

### ❓ Q1. What data structure is used in this stack implementation?

**A:** A simple array or list (in Python/JavaScript) or a fixed-size array in C++.

---

### ❓ Q2. Why is time complexity O(1) for both operations?

**A:** Because both `append` (push) and `pop` operations on the end of the array/list take constant time.

---

### ❓ Q3. What would happen if pop is called on an empty stack?

**A:** The function should return `-1` as specified.

---

### ❓ Q4. Can this be implemented using a linked list?

**A:** Yes, stacks can be implemented using linked lists where each new node is pushed to the head.

---

### ❓ Q5. What are real-world applications of stacks?

**A:** Function call stacks, undo features, expression parsing, browser history tracking.

---

## Company Tags

- `FactSet`, `Visa`, `Goldman Sachs`, `Qualcomm`, `Kritikal Solutions`

## Topic Tags

- `Arrays`, `Stack`, `Data Structures`

## Related Articles

- [Implement Stack Using Array](https://www.geeksforgeeks.org/dsa/implement-stack-using-array/),  [Introduction To Stack Data Structure And Algorithm Tutorials](https://www.geeksforgeeks.org/dsa/introduction-to-stack-data-structure-and-algorithm-tutorials/)
