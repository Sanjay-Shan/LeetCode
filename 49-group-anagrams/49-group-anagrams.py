from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # we will make use of the defaultdict which is same as that of the dict but doesn't
        # give out key errors
        hash=defaultdict(list)
        
        for s in strs:
            count=[0]*26
            for c in s:
                count[ord(c)-ord('a')]+=1
            hash[tuple(count)].append(s)
        return hash.values()
        
        #built-in functions used in this code
        #1. defaultdict --> dict without key error ie with default values https://docs.python.org/3/library/collections.html#collections.defaultdict
        #2. ord --> gets the ascii value
        
            
        