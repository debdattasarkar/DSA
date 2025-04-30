function reverseInAltGroups(arr, k) {
    const n = arr.length;
    let flag = 1; // Flag to check if we are in the reverse group or not
    for (let i = 0; i < n; i += k) {
        let left = i;
        let right = Math.min(i + k - 1, n - 1);
        if (flag % 2 !== 0) {
            while (left < right) {
                [arr[left], arr[right]] = [arr[right], arr[left]];
                left++;
                right--;
            }
        }
        flag++; // Increment the flag after processing each group
    }
    return arr;
}
console.log(reverseInAltGroups([1, 2, 3, 4, 5, 6, 7, 8, 9], 3));
