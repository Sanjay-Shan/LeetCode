class Solution(object):
    def reverse(self, x):
        new=0
        value= x if x>0 else x*-1
        while value!=0:
            rem=value%10
            new=new*10+rem
            value=value/10
        if new > (2**31)-1 or new< -1 *(2**31):
            return 0
        else:
            if  x>0 :
                return new
            else:
                return -1*new
        
        