Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num<10:
            return num
        if num==10:
            return 1
        else:
            while num>10:
                digits=self.separatedigits(num)
                num=0
                for i in digits:
                    num=num+i
                if num==10:
                    return 1
                    
        return num        
        
    def separatedigits(self,n):
        dig=[]
        while n>0:
            dig.append(n%10)
            n=n//10
        return dig
    def comdigits(self,nums):
        number=0
        for i in nums:
            number=(number*10)+i
            
        return number
