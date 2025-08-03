//{ Driver Code Starts
// Position this line where user code will be pasted.
const readline = require('readline');
const rl = readline.createInterface({input : process.stdin, output : process.stdout});

const inputLines = [];
rl.on('line', (line) => { inputLines.push(line.trim()); });

rl.on('close', () => {
    const t = parseInt(inputLines[0]);
    const solution = new Solution();
    let index = 1;

    for (let i = 0; i < t; i++) {
        const arr = inputLines[index].split(' ').map(Number);
        const ans = solution.printUnsorted(arr);
        console.log(ans[0], ans[1]);
        console.log('~');
        index++;
    }
});
// } Driver Code Ends


class Solution {
    printUnsorted(arr) {
        // Code here
        let n = arr.length;
        let start = -1, end = -1;

        // Step 1: From left, find where order breaks
        for (let i = 0; i < n - 1; i++) {
            if (arr[i] > arr[i + 1]) {
                start = i;
                break;
            }
        }

        if (start === -1) return [0, 0]; // Already sorted

        // Step 2: From right, find where order breaks
        for (let i = n - 1; i > 0; i--) {
            if (arr[i] < arr[i - 1]) {
                end = i;
                break;
            }
        }

        // Step 3: Find min and max in the subarray
        let sub_min = Math.min(...arr.slice(start, end + 1));
        let sub_max = Math.max(...arr.slice(start, end + 1));

        // Step 4: Expand to left if needed
        for (let i = 0; i < start; i++) {
            if (arr[i] > sub_min) {
                start = i;
                break;
            }
        }

        // Step 5: Expand to right if needed
        for (let i = n - 1; i > end; i--) {
            if (arr[i] < sub_max) {
                end = i;
                break;
            }
        }

        return [start, end];
    }
}