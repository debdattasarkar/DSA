
class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        if len(arr) < 2:
            return -1

        buff=arr[:2]
        buff.sort(reverse=True)
            
        for i in range(2,len(arr)):
            if(buff[0]==arr[i]):# or buff[1]==arr[i]):
                continue
            if(buff[1]<arr[i]):
                buff[1]=arr[i]
                buff.sort(reverse=True)
        
        return -1 if buff[1]==buff[0] else buff[1]