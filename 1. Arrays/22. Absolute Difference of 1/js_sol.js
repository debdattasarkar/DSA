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
        let k = parseInt(readLine());
        let arr = readLine().split(' ').map(Number);
        let ob = new Solution();
        let ans = ob.getDigitDiff1AndLessK(arr, k);
        console.log(ans.join(' '));
        console.log("~");
        tc--;
    }
}
// } Driver Code Ends


// User function Template for javascript
class Solution {
    
    // ✅ Correct way to define class method
    isAdjacentDiffOne(num) {
        let digits = num.toString();
        for (let i = 0; i < digits.length - 1; i++) {
            if (Math.abs(parseInt(digits[i]) - parseInt(digits[i + 1])) !== 1) {
                return false;
            }
        }
        return true;
    }

    // ✅ Method to get all qualifying numbers
    getDigitDiff1AndLessK(arr, k) {
        let result = [];

        for (let num of arr) {
            // Call class method with this.<methodName>
            if (num < k && num >= 10 && this.isAdjacentDiffOne(num)) {
                result.push(num);
            }
        }

        return result;
    }
}