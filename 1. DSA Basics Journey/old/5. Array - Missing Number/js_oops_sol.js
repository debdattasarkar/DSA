class ArrayManager {
    constructor() {
        this.arr = [];
    }

    insert(value) {
        if (this.arr.length < 10) {
            this.arr.push(value);
        } else {
            console.log("Array is full, cannot insert more elements!");
        }
    }

    display() {
        console.log("Array elements:", this.arr);
    }

    search(value) {
        return this.arr.includes(value);
    }

    remove(value) {
        const index = this.arr.indexOf(value);
        if (index !== -1) {
            this.arr.splice(index, 1);
            console.log(`Element ${value} deleted successfully.`);
        } else {
            console.log("Element not found, cannot delete!");
        }
    }

    findSmallest() {
        if (this.arr.length === 0) {
            console.log("Array is empty!");
            return null;
        }
        return Math.min(...this.arr);
    }

    findLargest() {
        if (this.arr.length === 0) {
            console.log("Array is empty!");
            return null;
        }
        return Math.max(...this.arr);
    }

    reverse() {
        this.arr.reverse();
        console.log("Array reversed successfully.");
    }

    findMissingNumber() {
        if (this.arr.length === 0) {
            console.log("Array is empty!");
            return null;
        }
        let n = this.arr.length;
        let maxNum = n + 1;
        let expectedSum = (maxNum * (maxNum + 1)) / 2;
        let actualSum = this.arr.reduce((a, b) => a + b, 0);
        return expectedSum - actualSum;
    }
}


function main() {
    let am = new ArrayManager();

    am.insert(1);
    am.insert(2);
    am.insert(4);
    am.insert(5);

    am.display();

    // console.log("Searching for 3:", am.search(3) ? "Found" : "Not Found");
    // console.log("Searching for 10:", am.search(10) ? "Found" : "Not Found");

    // am.remove(9);
    // console.log("After Reversing:");
    // am.reverse()
    // am.display();

    // console.log("Smallest number:", am.findSmallest());
    // console.log("Largest number:", am.findLargest());
    console.log("Missing number:", am.findMissingNumber());
}

main();