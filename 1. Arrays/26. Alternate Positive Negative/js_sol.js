//{ Driver Code Starts
// Initial Template for javascript

"use strict";

process.stdin.resume();
process.stdin.setEncoding("utf-8");

let inputString = "";
let currentLine = 0;

process.stdin.on("data", (inputStdin) => { inputString += inputStdin; });

process.stdin.on("end", (_) => {
    inputString =
        inputString.trim().split("\n").map((string) => { return string.trim(); });

    main();
});

function readLine() { return inputString[currentLine++]; }

/* Function to print an array */
function printArray(arr, size) {
    let i;
    let s = "";
    for (i = 0; i < size; i++) {
        s += arr[i] + " ";
    }
    console.log(s);
}

function main() {
    let t = parseInt(readLine());
    let i = 0;
    for (; i < t; i++) {
        let arr = readLine().trim().split(" ").map((x) => parseInt(x));
        let obj = new Solution();
        obj.rearrange(arr);
        printArray(arr, arr.length);

        console.log("~");
    }
}
// } Driver Code Ends


// User function Template for javascript

/**
 * @param {Number[]} arr
 * @returns {Number[]}
 */

class Solution {
    rearrange(arr) {
        // code here
        // Separate positives and negatives
        let pos = arr.filter(x => x >= 0);
        let neg = arr.filter(x => x < 0);

        let result = [];
        let i = 0, j = 0;

        // Alternate placement of positives and negatives
        while (i < pos.length && j < neg.length) {
            result.push(pos[i++]);
            result.push(neg[j++]);
        }

        // Add remaining elements if any
        while (i < pos.length) result.push(pos[i++]);
        while (j < neg.length) result.push(neg[j++]);

        // Modify original array in-place
        for (let k = 0; k < arr.length; k++) {
            arr[k] = result[k];
        }
    }
}