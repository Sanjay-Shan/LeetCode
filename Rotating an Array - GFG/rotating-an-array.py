#User function Template for python3

class Solution:
    def leftRotate(self, arr, n, d):
        self.reverse(arr,0,d-1)
        self.reverse(arr,d,n-1)
        self.reverse(arr,0,n-1)
    
    def reverse(self,arr,low,high):
        while low<high:
            arr[low],arr[high]=arr[high],arr[low]
            low+=1
            high-=1
        return arr

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        d = int(input())
        ob = Solution()
        ob.leftRotate(arr, n, d)
        for xx in arr:
            print(xx, end=" ")
        print()
        tc -= 1

# } Driver Code Ends