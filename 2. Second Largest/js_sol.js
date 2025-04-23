//{ Driver Code Starts
// Initial Template for javascript

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => { inputString += inputStdin; });

process.stdin.on('end', _ => {
    inputString = inputString.trim().split("\n").map(string => string.trim());
    main();
});

function readLine() { return inputString[currentLine++]; }

function main() {
    let t = parseInt(readLine());
    for (let i = 0; i < t; i++) {
        const arr = readLine().split(' ').map(x => parseInt(x));
        let obj = new Solution();
        let ans = obj.getSecondLargest(arr);
        console.log(ans);
        console.log("~");
    }
}

// } Driver Code Ends

// } Driver Code Ends


class Solution {
    getSecondLargest(arr) {
        // code here
        if (arr.length < 2) return -1;
    
        let largest = -1;
        let second = -1;
    
        for (let num of arr) {
            if (num > largest) {
                second = largest;
                largest = num;
            } else if (num > second && num !== largest) {
                second = num;
            }
        }
    
        return second;
    }
}