class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num={}
        for i in range(len(nums)):
            if nums[i] in num.keys():
                num[nums[i]]+=1
            else:
                num[nums[i]]=1
        for i,j in num.items():
            if j==1:
                return i
                    
        
        