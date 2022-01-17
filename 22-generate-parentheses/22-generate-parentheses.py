class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result=[]
        self.genPar(n,result,0,0,"")
        return result
        
    def genPar(self,n,result,right,left,string):
        if left==n and right==n:
            result.append(string)
            return result
        
        if left<n:
            self.genPar(n,result,right,left+1,string+"(")
            
        if left>right:
            self.genPar(n,result,right+1,left,string+")")
        
        