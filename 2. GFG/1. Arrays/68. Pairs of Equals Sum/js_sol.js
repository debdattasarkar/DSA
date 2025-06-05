//{ Driver Code Starts
// Driver code
const readline = require('readline');
const rl = readline.createInterface({input : process.stdin, output : process.stdout});

let inputLines = [];
let currentLine = 0;

rl.on('line', (line) => { inputLines.push(line.trim()); });

rl.on('close', () => { main(); });

function readLine() { return inputLines[currentLine++]; }

function main() {
    let tc = parseInt(readLine());
    while (tc > 0) {
        let arr = readLine().split(' ').map(Number);
        let ob = new Solution();
        let ans = ob.findPairs(arr);
        // console.log(ans);
        if (ans) {
            console.log("true");
        } else {
            console.log("false");
        }
        console.log("~");
        tc--;
    }
}
// } Driver Code Ends


// User function Template for javascript

class Solution {
    findPairs(arr) {
        // code here
        let sumMap = new Map();

        while (arr.length > 0) {
            // Remove the first element from array
            let val = arr.shift();

            // Check with all remaining elements
            for (let j = 0; j < arr.length; j++) {
                let sum = val + arr[j];

                // Count how many times the sum occurs
                sumMap.set(sum, (sumMap.get(sum) || 0) + 1);

                // If sum occurs second time, return true
                if (sumMap.get(sum) === 2) {
                    return true;
                }
            }
        }

        return false;
    }
}
