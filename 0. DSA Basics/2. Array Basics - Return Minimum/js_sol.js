function main() {
    let arr = [7, 3, 9, 1, 5];
    // let arr = [];

    // arr.push(7);
    // arr.push(3);
    // arr.push(9);
    // arr.push(1);
    // arr.push(5);

    console.log("Array:", arr);
    let smallest = arr[0];
    arr.forEach(function(element){
        if (element < smallest) {
            smallest = element;
        }
    });
    console.log("Smallest number is:", smallest);
}
main();