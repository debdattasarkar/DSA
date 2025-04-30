#User function Template for python3

class Solution:
    def totalFine(self, date, car, fine):
        #Code here
        total = 0
        for i in range(len(car)):
            if (date % 2 == 0 and car[i] % 2 != 0) or (date % 2 != 0 and car[i] % 2 == 0):
                total += fine[i]
        return total
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while (T > 0):
        date = int(input())
        car = [int(x) for x in input().strip().split()]
        fine = [int(x) for x in input().strip().split()]

        print(Solution().totalFine(date, car, fine))
        print("~")

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends