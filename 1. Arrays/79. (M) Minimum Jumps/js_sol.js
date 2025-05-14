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
        let arr = readLine().split(" ").map((x) => parseInt(x));
        let obj = new Solution();
        let res = obj.minJumps(arr);
        console.log(res);

        console.log("~");
    }
}
// } Driver Code Ends


/**
 * @param {number[]} arr
 * @return {number}
 */

class Solution {
    minJumps(arr) {
        // code here
        const n = arr.length;
        if (n <= 1) return 0;
        if (arr[0] === 0) return -1;
    
        let jumps = 1;
        let maxReach = arr[0];
        let steps = arr[0];
    
        for (let i = 1; i < n; i++) {
            if (i === n - 1) return jumps;
    
            maxReach = Math.max(maxReach, i + arr[i]);
            steps--;
    
            if (steps === 0) {
                jumps++;
                if (i >= maxReach) return -1;
                steps = maxReach - i;
            }
        }
    
        return -1;
    }
}