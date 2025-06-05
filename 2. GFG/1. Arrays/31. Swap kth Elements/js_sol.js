//{ Driver Code Starts


function main() {
    const readline = require('readline').createInterface({
        input : process.stdin,
        output : process.stdout
    });

    let inputLines = [];
    readline.on('line', (line) => { inputLines.push(line); });

    readline.on('close', () => {
        let t = parseInt(inputLines[0]);
        let index = 1;
        while (t-- > 0) {
            let k = parseInt(inputLines[index]);
            let arr = inputLines[index + 1].split(' ').map(Number);
            let ob = new Solution();
            ob.swapKth(arr, k);
            console.log(arr.join(' '));

            console.log("~");
            index += 2;
        }
    });
}

main();

// } Driver Code Ends



class Solution {
    swapKth(arr, k) {
        // code here
        const n = arr.length;
        // Swap k-th element from beginning and end (0-based indexing)
        let temp = arr[k - 1];
        arr[k - 1] = arr[n - k];
        arr[n - k] = temp;
    }
}