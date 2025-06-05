function reverseInDblsGroups(arr) {
    const n = arr.length;
    let k = 1;
    let i = 0;

    while (i < n) {
        let left = i;
        let right = Math.min(i + k - 1, n - 1);

        while (left < right) {
            [arr[left], arr[right]] = [arr[right], arr[left]];
            left++;
            right--;
        }

        i += k;
        k = k * 2;
    }

    return arr;
}

// Test
console.log(reverseInDblsGroups([1, 2, 3, 4, 5, 6, 7, 8, 9]));
// Output: [1, 3, 2, 7, 6, 5, 4, 9, 8]
