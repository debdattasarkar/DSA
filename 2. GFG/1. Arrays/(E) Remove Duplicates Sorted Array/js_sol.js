//{ Driver Code Starts
// Initial Template for javascript

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => { inputString += inputStdin; });

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => string.trim());
    main();
});

function readLine() { return inputString[currentLine++]; }

function main() {
    let t = parseInt(readLine());
    for (let i = 0; i < t; i++) {
        const arr = readLine().split(' ').map(x => parseInt(x));
        let obj = new Solution();
        let ans = obj.removeDuplicates(arr);
        for (let i = 0; i < ans; i++) {
            process.stdout.write(arr[i] + " ");
        }
        console.log();
        console.log("~");
    }
}
// } Driver Code Ends


// User function Template for javascript

class Solution {
    // Function to remove duplicates from the given array.
    removeDuplicates(arr) {
        // Code Here
        // Handle empty array
        if (arr.length === 0) return 0;
    
        let i = 0; // Index of last unique element
    
        for (let j = 1; j < arr.length; j++) {
            // If current element is different from last unique
            if (arr[j] !== arr[i]) {
                i++;              // Move index for next unique
                arr[i] = arr[j];  // Overwrite duplicate
            }
        }
    
        // Return the number of unique elements
        return i + 1;
    }
}