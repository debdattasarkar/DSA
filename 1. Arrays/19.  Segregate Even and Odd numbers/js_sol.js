//{ Driver Code Starts
// Initial Template for javascript
// Position this line where user code will be pasted.
const readline = require("readline");

const rl = readline.createInterface({input : process.stdin, output : process.stdout});

let inputLines = [];
let t = 0;
let currentTest = 0;

rl.on("line", function(line) { inputLines.push(line.trim()); }).on("close", function() {
    t = parseInt(inputLines[0]);
    let lineIndex = 1;

    for (let i = 0; i < t; i++) {
        const arr = inputLines[lineIndex++].split(" ").map(Number);
        const obj = new Solution();
        obj.segregateEvenOdd(arr);
        console.log(arr.join(" "));
        console.log("~");
    }
});

// } Driver Code Ends


class Solution {
    segregateEvenOdd(arr) {
        // code here
        let evens = arr.filter(x => x % 2 === 0).sort((a, b) => a - b);
        let odds = arr.filter(x => x % 2 !== 0).sort((a, b) => a - b);
    
        // Overwrite original array
        for (let i = 0; i < arr.length; i++) {
            arr[i] = i < evens.length ? evens[i] : odds[i - evens.length];
        }
    }
}
