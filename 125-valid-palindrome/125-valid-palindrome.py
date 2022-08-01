class Solution:
    def isPalindrome(self, s: str) -> bool:
        # range of alphabets in ASCII (65-90) & (97-122)
        r=""
        for i in range(len(s)):
            if (ord(s[i])>=65 and ord(s[i])<=90) or (ord(s[i])>=97 and ord(s[i])<=122) or ((ord(s[i])>=48 and ord(s[i])<=57)):
            # if s[i].isalnum():
                if (ord(s[i])>=65 and ord(s[i])<=90):
                    r+=s[i].lower()
                else:
                    r+=s[i]
        return r[::-1]==r
    
    # functions used
    # 1. ord() chr()
    # 2. str.lower()
    # 3. ASCII (A-Z,65-90) (a-z,97-122) (0-9,48-57)
    # 4. isalnum() could also be used instead of a combination of ord conditions
            
        