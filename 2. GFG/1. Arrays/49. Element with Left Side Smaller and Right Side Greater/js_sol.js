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
        let ans = obj.findElement(arr);
        console.log(ans);
        console.log("~");
    }
}

// } Driver Code Ends


class Solution {
    findElement(arr) {
        // code here
        const n = arr.length;
        if (n < 3) return -1;

        const maxLeft = Array(n).fill(0);
        const minRight = Array(n).fill(0);

        // Step 1: Fill maxLeft
        maxLeft[0] = -Infinity;
        for (let i = 1; i < n; i++) {
            maxLeft[i] = Math.max(maxLeft[i - 1], arr[i - 1]);
        }

        // Step 2: Fill minRight
        minRight[n - 1] = Infinity;
        for (let i = n - 2; i >= 0; i--) {
            minRight[i] = Math.min(minRight[i + 1], arr[i + 1]);
        }

        // Step 3: Find the element that satisfies the condition
        for (let i = 1; i < n - 1; i++) {
            if (arr[i] > maxLeft[i] && arr[i] < minRight[i]) {
                return arr[i];
            }
        }

        return -1;
    }
}
