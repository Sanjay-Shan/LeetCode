class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 2 -- [2] -- 1 way
        # 22 -- [2,2],[22] -- 2 ways
        # 222 -- [2,2,2],[2.22],[22,2] -- 3 ways = 2ways + 1way
        # 220 -- [2,20] 
        
        # if the element is not zero then it is atleast d[i-1] ,and then consider the last numbers in a string ie to check if it lies in the range of 09<x>27, then d[i]=d[i-2]
        
        if s[0] == "0":
            return 0
        
        dp = [0]*(len(s)+1)
        dp[0] = 1
        dp[1] = 1 if s[0] != "0" else 0
        
        for i in range(1, len(s)):
            if s[i] != "0":
                dp[i+1] = dp[i]
            if s[i-1] == "1" or (s[i-1] == "2" and s[i] in ["0", "1", "2", "3", "4", "5", "6"]):
                dp[i+1] += dp[i-1]

        return dp[-1]
        