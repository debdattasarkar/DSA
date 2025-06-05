//{ Driver Code Starts
// Initial Template for javascript
// Position this line where user code will be pasted.
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

function main() {
    let t = parseInt(readLine());
    for (let i = 0; i < t; i++) {
        let arr1 = readLine().split(' ').map(x => parseInt(x));
        let arr2 = readLine().split(' ').map(x => parseInt(x));
        let res = new Array(arr1.length + arr2.length);

        let solution = new Solution();
        solution.sortedMerge(arr1, arr2, res);

        console.log(res.join(' '));
        console.log("~");
    }
}
// } Driver Code Ends


// User function Template for javascript
class Solution {
    sortedMerge(arr1, arr2, res) {
        // Your code goes here
        arr1.sort((a, b) => a - b);
        arr2.sort((a, b) => a - b);
        
        let i = 0, j = 0;
        let merged = [];
        
        while (i < arr1.length && j < arr2.length) {
            if (arr1[i] <= arr2[j]) {
                merged.push(arr1[i++]);
            } else {
                merged.push(arr2[j++]);
            }
        }
        
        while (i < arr1.length) merged.push(arr1[i++]);
        while (j < arr2.length) merged.push(arr2[j++]);


        // Copy back into res
        for (let k = 0; k < merged.length; k++) {
            res[k] = merged[k];
        }
    }
}