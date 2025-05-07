//{ Driver Code Starts

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => { inputString += inputStdin; });

process.stdin.on('end', _ => {
    inputString =
        inputString.trim().split("\n").map(string => { return string.trim(); });

    main();
});

function readLine() { return inputString[currentLine++]; }

function main() {
    let t = parseInt(readLine());
    let i = 0;
    for (; i < t; i++) {

        let n = parseInt(readLine());

        let a = new Array(n);
        let input_a = readLine().split(' ').map(x => parseInt(x));
        for (let i = 0; i < n; i++) {
            a[i] = input_a[i];
        }

        let b = new Array(n);
        let input_b = readLine().split(' ').map(x => parseInt(x));
        for (let i = 0; i < n; i++) {
            b[i] = input_b[i];
        }

        let q = parseInt(readLine());

        let queries = new Array(q);

        for (let i = 0; i < q; i++) {
            let temp = parseInt(readLine());
            queries[i] = temp;
        }

        let obj = new Solution();
        let res = obj.countElements(n, a, b, q, queries);

        for (let i = 0; i < res.length; i++) {
            console.log(res[i]);
        }

        console.log("~");
    }
}

// } Driver Code Ends



class Solution {
    /**
    * @param number n
    * @param number[] a
    * @param number[] b
    * @param number q
    * @param number[] queries

    * @returns number[]
    */
    countElements(n, a, b, q, queries) {
        // code here
        // Step 1: Determine the maximum value in a and b
        let maxVal = Math.max(...a, ...b);

        // Step 2: Build frequency array for elements in b
        let freq = new Array(maxVal + 2).fill(0);
        for (let val of b) {
            freq[val]++;
        }

        // Step 3: Build prefix sum array so freq[i] = count of elements ≤ i
        for (let i = 1; i <= maxVal; i++) {
            freq[i] += freq[i - 1];
        }

        // Step 4: For each query, use prefix sum
        let result = [];
        for (let idx of queries) {
            let val = a[idx];
            result.push(freq[val]);
        }

        return result;
    }
}
