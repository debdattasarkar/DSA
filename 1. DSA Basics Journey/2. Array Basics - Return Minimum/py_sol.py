def main():
    arr = [7, 3, 9, 1, 5]

    print("Array:", arr)

    smallest = arr[0]
    for num in arr:
        if num < smallest:
            smallest = num

    print("Smallest number is:", smallest)

if __name__ == "__main__":
    main()