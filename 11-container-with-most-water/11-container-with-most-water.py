class Solution:
    # def maxArea(self, height: List[int]) -> int:
    #     res=0
    #     area=0
    #     for l in range(0,len(height)):
    #         for r in range(l+1,len(height)):
    #             area=abs(l-r)*min(height[l],height[r])
    #             res = max(res,area)
    #     return res
    
    def maxArea(self, height: List[int]) -> int:
        res=0
        area=0
        l,r=0,len(height)-1
        while l<r:
            area=abs(l-r)*min(height[l],height[r])
            res = max(res,area)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return res