class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     sum=0
    #     i=0
    #     num=0
    #     for i in range(len(nums)-1):
    #         sum=0
    #         for j in range(i,len(nums)):
    #             if j!=i:
    #                 sum=nums[i]+nums[j]
    #                 if sum==target:
    #                     return [i,j]
    #                     break
    #                 else:
    #                     sum=0
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash={}
        for i in range(len(nums)):
            rem=target-nums[i]
            if rem in hash:
                return [i,hash[rem]]
            hash[nums[i]]=i

                
            
            

                
            
            
        
        