# Insert in Sorted Circular Linked List

## 📝 Problem Statement

Given a **sorted circular linked list**, the task is to **insert a new node** into this circular linked list such that it remains sorted.

---

## 📌 Examples

### Example 1:

* **Input:** `head = 1 -> 2 -> 4`, `data = 2`
* **Output:** `1 -> 2 -> 2 -> 4`
* **Explanation:** The new node `2` is inserted after the second node.

### Example 2:

* **Input:** `head = 1 -> 4 -> 7 -> 9`, `data = 5`
* **Output:** `1 -> 4 -> 5 -> 7 -> 9`
* **Explanation:** The new node `5` is inserted after the node with value `4`.

---

## ✅ Constraints

* $2 \leq \text{number of nodes} \leq 10^6$
* $0 \leq \text{node->data} \leq 10^6$
* $0 \leq \text{data} \leq 10^6$

---

## ⏱️ Expected Complexities

* **Time Complexity:** $O(n)$
* **Auxiliary Space:** $O(1)$

---

## 🔧 Function Signature

### Python

```python
class Solution:
    def sortedInsert(self, head, data):
        # Your code here
```

### C++

```cpp
class Solution {
  public:
    Node* sortedInsert(Node* head, int data) {
        // Your code here
    }
};
```

### JavaScript

```javascript
class Solution {
    sortedInsert(head, data) {
        // Your code here
    }
}
```

---

## 💡 Key Concepts

* Circular Linked List
* In-place Node Insertion
* Edge Cases: Insert at beginning, end, or between nodes

---

## 🧠 Explanation

To insert a node into a sorted circular linked list:

1. Create the new node.
2. If the list is empty, point the new node to itself and return it.
3. Traverse the list to find the appropriate position where the node fits between two nodes:

   * either between two sorted values: `curr <= data <= next`
   * or at the pivot (wrap-around): `curr > next && (data >= curr or data <= next)`
4. Insert the node and update the links.

---

## 🏢 Company Tags

`Zoho`, `Amazon`, `Microsoft`

## 🏷️ Topic Tags

`circular-linked-list`, `Linked List`, `Data Structures`

## 🔗 Related Articles

* [Sorted Insert For Circular Linked List](https://www.geeksforgeeks.org/sorted-insert-for-circular-linked-list/)

---
Here’s the **corrected version of the solution** for **inserting a node into a sorted circular linked list** for all three languages: **C++**, **Python**, and **JavaScript**.

---

## ✅ Step-by-Step Explanation

### The core logic:

* If the list is empty, insert the node and point it to itself.
* If the data is less than the head's data, insert before the head and return the new node as the new head.
* Otherwise, traverse the list to find the correct sorted position and insert the node there.

---

## ✅ Python Code

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def sortedInsert(self, head, data):
        new_node = Node(data)

        # Case 1: Empty list
        if head is None:
            new_node.next = new_node
            return new_node

        current = head

        # Case 2: Insert before head (new smallest)
        if data < head.data:
            while current.next != head:
                current = current.next
            current.next = new_node
            new_node.next = head
            return new_node  # New head

        # Case 3: Insert in sorted order
        while current.next != head and current.next.data < data:
            current = current.next

        new_node.next = current.next
        current.next = new_node
        return head
```

---

## ✅ C++ Code

```cpp
class Node {
 public:
  int data;
  Node *next;
  Node(int x) {
    data = x;
    next = NULL;
  }
};

class Solution {
  public:
    Node* sortedInsert(Node* head, int data) {
        Node* new_node = new Node(data);

        // Case 1: Empty list
        if (!head) {
            new_node->next = new_node;
            return new_node;
        }

        Node* current = head;

        // Case 2: Insert before head (new smallest)
        if (data < head->data) {
            while (current->next != head)
                current = current->next;
            current->next = new_node;
            new_node->next = head;
            return new_node;  // new head
        }

        // Case 3: Insert in sorted order
        while (current->next != head && current->next->data < data)
            current = current->next;

        new_node->next = current->next;
        current->next = new_node;
        return head;
    }
};
```

---

## ✅ JavaScript Code

```javascript
class Node {
    constructor(data) {
        this.data = data;
        this.next = null;
    }
}

class Solution {
    sortedInsert(head, data) {
        let newNode = new Node(data);

        // Case 1: Empty list
        if (head === null) {
            newNode.next = newNode;
            return newNode;
        }

        let current = head;

        // Case 2: Insert before head (new smallest)
        if (data < head.data) {
            while (current.next !== head) {
                current = current.next;
            }
            current.next = newNode;
            newNode.next = head;
            return newNode;  // New head
        }

        // Case 3: Insert in sorted order
        while (current.next !== head && current.next.data < data) {
            current = current.next;
        }

        newNode.next = current.next;
        current.next = newNode;
        return head;
    }
}
```

---

Great! Let's walk through a **visual dry run** of inserting a new node into a **sorted circular linked list** using the Python logic.
We'll use the **input** from the GeeksforGeeks example:

---

## 🔄 Input

* **Initial list**: `1 -> 4 -> 7 -> 9 -> (back to 1)`
* **Insert data**: `5`

---

### 🧠 Step-by-Step Execution

#### Step 1: Create the new node

```python
new_node = Node(5)
```

We now have a new node with `data = 5`.

---

#### Step 2: Traverse the list to find the insert position

We begin traversal from `head = 1`.

| Current Node | Next Node | Next Node's Data | Comparison (5 > next.data) |
| ------------ | --------- | ---------------- | -------------------------- |
| 1            | 4         | 4                | ✅ Keep moving              |
| 4            | 7         | 7                | ❌ STOP                     |

We stop before 7 because 5 should be inserted between 4 and 7.

---

#### Step 3: Insert the new node between 4 and 7

Update pointers:

```python
new_node.next = current.next  # 5.next = 7
current.next = new_node       # 4.next = 5
```

#### Resulting Linked List:

```
1 → 4 → 5 → 7 → 9
↑               ↓
└──────(circular)──────┘
```

---

## ✅ Final Circular Linked List (Clockwise):

```text
1 -> 4 -> 5 -> 7 -> 9 -> (back to 1)
```

---

Absolutely! Let’s walk through a **visual dry run** of the **Sorted Insert in a Circular Linked List** problem using the input you provided:

---

### 🔢 Input:

* **Head**: `48 → 49 → 53 → 54 → 61 → (back to 48)`
* **Data to Insert**: `11`

---

### 🎯 Objective:

Insert `11` such that the **circular linked list remains sorted**.

---

## 🧠 Step-by-Step Dry Run:

### Step 1: Create `new_node = Node(11)`

We now try to find the **correct position** for inserting `11`.

---

### Step 2: Traverse the Circular List

Let's look at each transition:

| `Current Node` | `Next Node` | Comparison: `current.data < data < current.next.data` |
| -------------- | ----------- | ----------------------------------------------------- |
| 48             | 49          | 48 < 11 < 49 ❌                                        |
| 49             | 53          | 49 < 11 < 53 ❌                                        |
| 53             | 54          | 53 < 11 < 54 ❌                                        |
| 54             | 61          | 54 < 11 < 61 ❌                                        |
| 61             | 48          | ⚠ **Rotation Completed** (back to head)               |

No proper place **in between** was found, **BUT** we hit the **wrap-around condition**.

---

### 🔁 Wrap-Around Condition (Inserting Before Head)

When no suitable position is found and `data < head.data`, we need to:

* Insert the node **before the head**.
* The node becomes the **new head**.

So, insert `11` **after the last node (61)** and before `48`.

```text
Before:
61 → 48

After Insertion:
61 → 11 → 48
```

---

### ✅ Final Circular Linked List:

```text
11 → 48 → 49 → 53 → 54 → 61 → (back to 11)
```

---

### 🔄 Circular Flow:

```
         +-----+
         |     v
11 → 48 → 49 → 53 → 54 → 61
^                          |
|--------------------------+
```

---

### ✅ Output:

**`11 48 49 53 54 61`**

This matches the **expected output** from your earlier test result!
