from collections import OrderedDict
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq=OrderedDict()
        for i in range(len(s)):
            if s[i] in freq.keys():
                freq[s[i]]+=1
            else:
                freq[s[i]]=1
        for k,j in freq.items():
            if j==1:
                return s.index(k)
        return -1
        