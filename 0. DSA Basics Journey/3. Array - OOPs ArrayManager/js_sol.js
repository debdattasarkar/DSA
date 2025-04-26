class ArrayManager {
    constructor() {
        this.arr = []; // Dynamic array (list)
    }

    // Insert an element
    insert(value) {
        if (this.arr.length < 10) {
            this.arr.push(value);
        } else {
            console.log("Array is full, cannot insert more elements!");
        }
    }

    // Display all elements
    display() {
        console.log("Array elements:", this.arr);
    }

    // Search for an element
    search(value) {
        return this.arr.includes(value);
    }

    // Remove an element
    remove(value) {
        const index = this.arr.indexOf(value);
        if (index !== -1) {
            this.arr.splice(index, 1); // Remove 1 element at index
            console.log(`Element ${value} deleted successfully.`);
        } else {
            console.log("Element not found, cannot delete!");
        }
    }

    // Find the smallest element
    findSmallest() {
        if (this.arr.length === 0) {
            console.log("Array is empty!");
            return null;
        }
        let smallest = this.arr[0];
        this.arr.forEach((num) => {
            if (num < smallest) {
                smallest = num;
            }
        });
        return smallest;
    }

    // Find the largest element
    findLargest() {
        if (this.arr.length === 0) {
            console.log("Array is empty!");
            return null;
        }
        let largest = this.arr[0];
        this.arr.forEach((num) => {
            if (num > largest) {
                largest = num;
            }
        });
        return largest;
    }
}

function main() {
    let am = new ArrayManager();

    am.insert(7);
    am.insert(3);
    am.insert(9);
    am.insert(1);
    am.insert(5);

    am.display();

    console.log("Searching for 3:", am.search(3) ? "Found" : "Not Found");
    console.log("Searching for 10:", am.search(10) ? "Found" : "Not Found");

    am.remove(9);
    am.display();

    console.log("Smallest number:", am.findSmallest());
    console.log("Largest number:", am.findLargest());
}

main();