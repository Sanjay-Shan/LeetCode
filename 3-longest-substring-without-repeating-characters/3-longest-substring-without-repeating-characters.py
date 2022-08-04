class Solution(object):
    def lengthOfLongestSubstring(self, s):
        p1=0      #pointer 1
        p2=p1+1   #pointer 2
        temp=0    #temp variable
        ls=0      #length counter
        
        # keep running until the p2 pointer reaches the end of array 
        while p2<=len(s):
            if len(set(s[p1:p2]))==len(s[p1:p2]):
                   temp+=1
                   p2+=1
            else:
                   p1+=1
                   p2=p1+1
                   temp=0
            if temp>=ls:
               ls=temp
        return ls
            
                   
        