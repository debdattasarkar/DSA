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
        let arr1 = readLine().split(' ').map(Number);
        let arr2 = readLine().split(' ').map(Number);
        let ob = new Solution();
        let ans = ob.findSum(arr1, arr2);
        console.log(ans.join(' '));
        console.log("~");
        tc--;
    }
}
// } Driver Code Ends


// User function Template for javascript

/**
 * @param {number[]} arr1
 * @param {number[]} arr2
 * @returns {number[]}
 */

class Solution {
    findSum(arr1, arr2) {
        // code here
        let i = arr1.length - 1;
        let j = arr2.length - 1;
        let carry = 0;
        let result = [];

        while (i >= 0 || j >= 0 || carry > 0) {
            let digit1 = i >= 0 ? arr1[i] : 0;
            let digit2 = j >= 0 ? arr2[j] : 0;
            let total = digit1 + digit2 + carry;

            result.push(total % 10); // push the last digit
            carry = Math.floor(total / 10); // update carry

            i--;
            j--;
        }

        result.reverse(); // since we added digits from least to most significant
        return result;
    }
}
