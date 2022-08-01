class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # perform sort and set operation to get the elements in order
        nums=sorted(list(set(nums)))
        arr=[]
        
        # set length=0 if the len(arr)=0
        length=0
        if len(nums)>0:
            length=1
            arr.append(length)
            
        #loop through the elements to see if they are consecutive
        for i in range(len(nums)-1):
            if nums[i+1]==nums[i]+1:
                length+=1
            else:
                arr.append(length)
                length=1
        arr.append(length)
        return max(arr)