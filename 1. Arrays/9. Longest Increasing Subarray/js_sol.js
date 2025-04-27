//{ Driver Code Starts
// Initial Template for javascript

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => { inputString += inputStdin; });

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => string.trim());
    main();
});

function readLine() { return inputString[currentLine++]; }

// Position this line where user code will be pasted.

function main() {
    let t = parseInt(readLine());
    let solution = new Solution();

    for (let i = 0; i < t; i++) {
        let arr = readLine().split(' ').map(x => parseInt(x));
        let ans = solution.lenOfLongIncSubArr(arr);
        console.log(ans);
        console.log("~");
    }
}
// } Driver Code Ends


// User function Template for javascript

class Solution {
    // Function to find the length of longest increasing subarray
    lenOfLongIncSubArr(arr) {
        // Your Code goes here
        let n = arr.length;
        let maxLen = 1, currLen = 1;
    
        for (let i = 1; i < n; i++) {
            if (arr[i] > arr[i - 1]) {
                currLen++;
                maxLen = Math.max(maxLen, currLen);
            } else {
                currLen = 1;
            }
        }
    
        return maxLen;
    }
}