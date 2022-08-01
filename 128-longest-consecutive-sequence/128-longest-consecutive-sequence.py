class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # perform sort to get the elements in order
        nums=sorted(list(set(nums)))
        print(nums)
        arr=[]
        # set length=0 if the len(arr)=0
        length=0
        if len(nums)>0:
            length=1
            arr.append(length)
            
        for i in range(len(nums)-1):
            if nums[i+1]==nums[i]+1:
                length+=1
            else:
                arr.append(length)
                length=1
        arr.append(length)
        print(arr)
        return max(arr)