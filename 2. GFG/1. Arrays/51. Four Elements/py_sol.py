#User function Template for python3

def find4Numbers( A, n, X):
    # return true or false
    A.sort()  # Sort the array to use two-pointer technique
    for i in range(n - 3):
        for j in range(i + 1, n - 2):
            left = j + 1
            right = n - 1
            target = X - A[i] - A[j]
            while left < right:
                current_sum = A[left] + A[right]
                if current_sum == target:
                    return True
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1
    return False




#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        A = [int(x) for x in input().strip().split()]
        X = int(input())
        
        if find4Numbers(A, n, X):
            print(1)
        else:
            print(0)

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends