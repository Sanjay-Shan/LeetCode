class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num=0
        dum=[]
        for i in range(len(digits)):
            if i==0:
                print(digits[len(digits)-1-i])
                num+=digits[len(digits)-1-i]*10**i
                num+=1
            else:
                num+=digits[len(digits)-1-i]*10**i
                
                
        return [int(i) for i in str(num)]
                

                
            
            
            
        