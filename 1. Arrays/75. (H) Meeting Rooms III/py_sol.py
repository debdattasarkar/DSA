#{ 
 # Driver Code Starts
#Initial Template for Python 3
import heapq


# } Driver Code Ends

#User function Template for python3
class Solution:
    def mostBooked(self, n, meetings):
        #code here
        meetings.sort()  # Sort by start time

        # Available rooms by room number
        available = list(range(n))
        heapq.heapify(available)

        # Busy rooms as (end_time, room_id)
        busy = []

        # Count of meetings per room
        count = [0] * n

        for start, end in meetings:
            # Free up rooms that are now available
            while busy and busy[0][0] <= start:
                end_time, room_id = heapq.heappop(busy)
                heapq.heappush(available, room_id)

            if available:
                # Assign to earliest available room
                room = heapq.heappop(available)
                heapq.heappush(busy, (end, room))
                count[room] += 1
            else:
                # Delay: take earliest finishing room
                end_time, room = heapq.heappop(busy)
                duration = end - start
                new_end = end_time + duration
                heapq.heappush(busy, (new_end, room))
                count[room] += 1

        # Find room with max count, prefer lower room number
        max_meetings = max(count)
        for i in range(n):
            if count[i] == max_meetings:
                return i


#{ 
 # Driver Code Starts.

if __name__ == "__main__":
    import sys
    input = sys.stdin.read().split()
    it = iter(input)
    t = int(next(it))
    while t > 0:
        t -= 1
        n = int(next(it))
        m = int(next(it))
        meetings = []
        for _ in range(m):
            s = int(next(it))
            e = int(next(it))
            meetings.append([s, e])
        sol = Solution()
        res = sol.mostBooked(n, meetings)
        print(res)
        print("~")
# } Driver Code Ends