function main() {
    let arr = []; // Create an empty array

    // Insert elements
    arr.push(10);
    arr.push(20);
    arr.push(30);

    // Display elements
    console.log("Array elements:", arr);

    // Search for an element
    let searchKey = 20;
    let index = arr.indexOf(searchKey);
    if (index !== -1) {
        console.log(`Found ${searchKey} at index ${index}`);
    } else {
        console.log(`${searchKey} not found!`);
    }

    // Delete an element (say delete 20)
    let deleteKey = 20;
    index = arr.indexOf(deleteKey);
    if (index !== -1) {
        arr.splice(index, 1); // Removes 1 element at position 'index'
        console.log(`After deleting ${deleteKey}, array elements:`, arr);
    } else {
        console.log("Element not found to delete!");
    }
}

// Run the program
main();
