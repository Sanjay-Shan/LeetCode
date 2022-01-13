class Solution(object):
    def longestPalindrome(self, s):
        maxlen=1
        low=0
        high=0
        start=0
        
        for i in range(1,len(s)):
            
            #considering palindrome is a string of even length with centre i and i-1
            high=i
            low=i-1
            
            while low>=0 and high<len(s) and s[low]==s[high]:
                low-=1
                high+=1
            
            # correcting the indices
            low+=1
            high-=1
            
            if s[low]==s[high] and high-low+1>maxlen:
                start=low
                maxlen=high-low+1
                
            #considering the palindrome as string of odd length with centre i
            
            low=i-1
            high=i+1
            
            while low>=0 and high<len(s) and s[low]==s[high]:
                low-=1
                high+=1
            
            # correcting the indices
            low+=1
            high-=1
            
            if s[low]==s[high] and high-low+1>maxlen:
                start=low
                maxlen=high-low+1
        
        return s[start:start+maxlen]    
            
        
            
                
            
            
        
        