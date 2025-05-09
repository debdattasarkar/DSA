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
        let a = readLine().split(" ").map((x) => parseInt(x));
        let b = readLine().split(" ").map((x) => parseInt(x));
        let obj = new Solution();
        let res = obj.findMissing(a, b);
        printArray(res, res.length);

        console.log("~");
    }
}
// } Driver Code Ends


// User function Template for javascript

/**
 * @param {Number[]} arr1
 * @param {Number[]} arr2
 * @returns {Number[]}
 */

class Solution {
    findMissing(a, b) {
        // code here
        const bSet = new Set(b);
        const result = [];
        for (let num of a) {
            if (!bSet.has(num)) {
                result.push(num);
            }
        }
        return result;
    }
}