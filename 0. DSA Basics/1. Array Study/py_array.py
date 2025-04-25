def main():
    arr = []  # Create an empty list

    # Insert elements
    arr.append(10)
    arr.append(20)
    arr.append(30)

    # Display elements
    print("Array elements:", arr)

    # Search for an element
    search_key = 20
    if search_key in arr:
        print(f"Found {search_key} at index {arr.index(search_key)}")
    else:
        print(f"{search_key} not found!")

    # Delete an element (say delete 20)
    delete_key = 20
    if delete_key in arr:
        arr.remove(delete_key)
        print(f"After deleting {delete_key}, array elements:", arr)
    else:
        print("Element not found to delete!")

if __name__ == "__main__":
    main()
