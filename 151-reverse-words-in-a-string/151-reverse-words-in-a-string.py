class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=s.strip(" ").split(" ") #remove trailing and leading spaces 
    
        temp=""
        
        for i in range(len(s)-1,-1,-1): # traverse in a reverse order
            if len(s[i])==0: # to remove the empty spaces
                continue
            temp+=s[i]
            if i!=0: #for the last word in the string
                temp+=" "
        return temp
            
        