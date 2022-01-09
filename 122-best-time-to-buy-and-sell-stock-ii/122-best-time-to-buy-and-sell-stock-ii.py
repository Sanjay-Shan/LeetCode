class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        cur_min=prices[0]
        profit=0
        for i in range(1,len(prices)):
            if prices[i]< cur_min:
                cur_min=prices[i]
            else:
                profit+=cur_min-prices[i]
                cur_min=prices[i]
        return abs(profit)
                
        





# if prices==sorted(prices):
#             return max(prices)-min(prices)
#         elif prices==list(reversed(sorted(prices))):
#             return 0
#         else:
#             stocks={}
#             sell=[]
#             buy=[]
#             avg=sum(prices)/len(prices)
#             print(avg)
#             for i in range(len(prices)):
#                 if prices[i]>avg:
#                     stocks[prices[i]]="Peak"
#                 else:
#                     stocks[prices[i]]="Valley"
                    
#             print(stocks)
#             indicator=0 # initially set to bu mode
#             for i in range(len(prices)):
#                 if indicator %2==0: #then it's a buy mode
#                     if stocks[prices[i]]=="Valley":
#                         buy.append(prices[i])
#                         indicator+=1
#                         continue
#                     else:
#                         continue
#                 else: #it is a sell mode
#                     if stocks[prices[i]]=="Peak":
#                         sell.append(prices[i])
#                         indicator+=1
#                         continue
#                     else:
#                         continue
#             l=[a-b for a,b in zip(buy,sell)]
#             return abs(sum(l))
                    
    
        