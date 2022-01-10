class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        length=len(min(strs,key=len))
        strlist=[]
        for i in range(len(strs)):
            strlist.append("")
        i=0
        pre=''
        for i in range(length):
            for s in range(len(strs)):
                strlist[s]+=strs[s][i]
            if len(set(strlist))==1:
                pre=set(strlist)
            else:
                break
                
        return ''.join(pre)
            
        