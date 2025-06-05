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
        if (arr[i] == -0) arr[i] = 0;
        s += arr[i] + " ";
    }
    console.log(s);
    console.log("~");
}

function main() {
    let t = parseInt(readLine());
    let i = 0;
    for (; i < t; i++) {
        let s = readLine().split(" ").filter((x) => x !== "").map((x) => parseInt(x));
        let n = s.length;
        let arr = new Array(n);
        for (let j = 0; j < n; j++) arr[j] = s[j];
        let x = parseInt(readLine());
        let obj = new Solution();
        let res = obj.subarraySum(arr, x);
        printArray(res, res.length);
    }
}
// } Driver Code Ends


// User function Template for javascript
/**
 * @param {number[]} arr
 * @param {number} target
 * @returns {number[]}
 */

class Solution {
    subarraySum(arr, target) {
        // code here
        let start = 0;
        let currentSum = 0;
    
        for (let end = 0; end < arr.length; end++) {
            currentSum += arr[end];
    
            while (currentSum > target && start <= end) {
                currentSum -= arr[start];
                start++;
            }
    
            if (currentSum === target) {
                // Return 1-based indices
                return [start + 1, end + 1];
            }
        }
        return [-1];
    }
}