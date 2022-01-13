class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=s.strip(" ") #remove trailing and leading spaces 
        s=s.split(" ") #put every word into a list
    
        print(s)
        temp=""
        
        for i in range(len(s)-1,-1,-1): # traverse in a reverse order
            if len(s[i])==0:
                continue
            temp+=s[i]
            if i!=0:
                temp+=" "
        return temp
            
        