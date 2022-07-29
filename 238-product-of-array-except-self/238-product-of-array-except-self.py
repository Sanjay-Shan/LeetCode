class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # create a forward pass and backward pass product arrays
        prefix=[]
        postfix=[]
        answer=[]
        
        #loop for prefix
        res=0
        for i in range(len(nums)):
            if i==0:
                res=nums[i]
            else:
                res*=nums[i]
            prefix.append(res)
        print(prefix)
        
        #loop for postfix
        res=0
        for i in range(len(nums)-1,-1,-1):
            if i==len(nums)-1:
                res=nums[i]
            else:
                res*=nums[i]
            postfix.append(res)
        postfix.reverse()
        print(postfix)
        
        ans=[]
        for i in range(len(nums)):
            pre=prefix[i-1] if i-1>=0 else 1
            post=postfix[i+1] if i+1<len(nums) else 1
            print(pre,post)
            answer.append(pre*post)
        return answer
        
        
        
        