//{ Driver Code Starts
// Position this line where user code will be pasted.
const readline = require('readline')
                     .createInterface({input : process.stdin, output : process.stdout});

const input = [];
readline.on('line', (line) => { input.push(line); }).on('close', () => {
    const t = parseInt(input[0], 10);
    for (let i = 1; i <= t; i++) {
        const arr = input[i].split(' ').map(Number);
        const ob = new Solution();
        console.log(ob.firstIndex(arr));
        console.log("~");
    }
});
// } Driver Code Ends


// User function Template for javascript

/**
 * @param {number[]} arr

 * @returns {number}
*/

class Solution {
    firstIndex(arr) {
        // code here
        let low = 0, high = arr.length - 1;
        let answer = -1;
    
        while (low <= high) {
            let mid = Math.floor((low + high) / 2);
    
            if (arr[mid] === 1) {
                answer = mid;
                high = mid - 1; // Search on the left side
            } else {
                low = mid + 1;
            }
        }
    
        return answer;
    }
}
