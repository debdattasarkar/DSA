class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        if len(arr) < 2:
            return -1
        buff=arr[:2]
        if(buff[0]<buff[1]):
            buff[0],buff[1] = buff[1],buff[0]
            
        for i in range(2,len(arr)):
            if(buff[0]==arr[i]):# or buff[1]==arr[i]):
                continue
            if(buff[1]<arr[i]):
                buff[1]=arr[i]
                if(buff[0]<buff[1]):
                    buff[0],buff[1] = buff[1],buff[0]
        
        if buff[1]==buff[0]:
            return -1
        else:
            return buff[1]