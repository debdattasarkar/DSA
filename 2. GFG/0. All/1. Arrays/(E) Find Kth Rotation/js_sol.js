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
        let res = obj.findKRotation(arr);
        console.log(res);
        console.log("~");
    }
}

// } Driver Code Ends


// User function Template for javascript

class Solution {
    findKRotation(arr) {
        // Code Here
        let low = 0, high = arr.length - 1;

        while (low <= high) {
            // Already sorted subarray
            if (arr[low] <= arr[high]) return low;

            let mid = Math.floor((low + high) / 2);
            let next = (mid + 1) % arr.length;
            let prev = (mid - 1 + arr.length) % arr.length;

            if (arr[mid] <= arr[next] && arr[mid] <= arr[prev])
                return mid;
            else if (arr[mid] <= arr[high])
                high = mid - 1;
            else
                low = mid + 1;
        }
        return 0;
    }
}
