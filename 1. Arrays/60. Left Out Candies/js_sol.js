//{ Driver Code Starts
// Initial Template for javascript
// Position this line where user code will be pasted.
//  Driver code
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
        let ans = ob.leftCandies(arr[0], arr[1]);
        console.log(ans);
        console.log("~");
        tc--;
    }
}
// } Driver Code Ends


// User function Template for javascript
class Solution {
    leftCandies(n, m) {
        // code
        let low = 0, high = m;

        // Binary search for number of full rounds
        while (low <= high) {
            let mid = Math.floor((low + high) / 2);
            let total = (mid * n * (n + 1)) / 2;

            if (total <= m) low = mid + 1;
            else high = mid - 1;
        }

        // Used in complete `high` rounds
        let used = (high * n * (n + 1)) / 2;
        m -= used;

        // Final round simulation
        for (let i = 1; i <= n; i++) {
            if (m >= i) m -= i;
            else break;
        }

        return m;
    }
}

