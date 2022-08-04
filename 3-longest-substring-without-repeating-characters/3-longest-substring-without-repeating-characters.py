class Solution(object):
    def lengthOfLongestSubstring(self, s):
        i=0 #pointer 1
        j=i+1 #pointer 2
        l=0 #temp variable
        f=0 #length counter 
        while j<=len(s):
            # print(i,j,l,f)
            # print(len(set(s[i:j]))==len(s[i:j]))
            if len(set(s[i:j]))==len(s[i:j]):
                   l+=1
                   j+=1
            else:
                   i+=1
                   j=i+1
                   l=0
            if l>=f:
               f=l
        return f
            
                   
        