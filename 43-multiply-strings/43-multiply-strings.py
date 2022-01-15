class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        
        num={'1': 1, '0': 0, '3': 3, '2': 2, '5': 5, '4': 4, '7': 7, '6': 6, '9': 9, '8': 8}
        n1=0
        n2=0
        for i in range(len(num1)-1,-1,-1):
            x=num[num1[i]]
            n1=n1+x*(10**abs(len(num1)-1-i))
            print(n1)
            
        for i in range(len(num2)-1,-1,-1):
            x=num[num2[i]]
            n2=n2+x*(10**abs(len(num2)-1-i))
            
        print(n1,n2)
        return str(n1*n2)
            
            
            
            
        