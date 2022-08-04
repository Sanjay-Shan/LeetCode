class Solution:
    # def maxProfit(self, prices: List[int]) -> int:
    #     res=[]
    #     for i in range(len(prices)):
    #         m=prices[i]
    #         n=prices[i+1:]
    #         if len(n)==0:
    #             res.append(0)
    #         else:
    #             res.append(max(n)-m)
    #     return max(res)
    
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1
        m=0
        while r<=len(prices)-1:
            diff=prices[r]-prices[l]
            if m<diff:
                m=diff
            if prices[l]>prices[r]:
                l=r
                r+=1
            else:
                r+=1
                
        return m