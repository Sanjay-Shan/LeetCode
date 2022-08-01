# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         # range of alphabets in ASCII (65-90) & (97-122)
#         r=""
#         for i in range(len(s)):
#             if (ord(s[i])>=65 and ord(s[i])<=90) or (ord(s[i])>=97 and ord(s[i])<=122) or ((ord(s[i])>=48 and ord(s[i])<=57)):
#             # if s[i].isalnum():
#                 if (ord(s[i])>=65 and ord(s[i])<=90):
#                     r+=s[i].lower()
#                 else:
#                     r+=s[i]
#         return r[::-1]==r
    
#     # functions used
#     # 1. ord() chr()
#     # 2. str.lower()
#     # 3. ASCII (A-Z,65-90) (a-z,97-122) (0-9,48-57)
#     # 4. isalnum() could also be used instead of a combination of ord conditions
class Solution:
    def isPalindrome(self, s: str) -> bool:
        #consider 2 pointers
        l,r=0,len(s)-1
        while l<r:
            while l<r and not self.isalpha(s[l]):
                l+=1
            while l<r and not self.isalpha(s[r]):
                r-=1
            if s[l].lower()!=s[r].lower():
                return False
            l+=1
            r-=1
        return True
        
    def isalpha(self,c):
        return ord('a')<= ord(c) <=ord('z') or ord('A')<= ord(c) <=ord('Z') or ord('0')<= ord(c) <=ord('9')
            
        