Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if(x<0):
            return False
        if(x<10):
            return True
        
        digitsinx=self.separatedigits(x)
        number=0
        for digit in digitsinx:
            number=(number*10)+digit
        if number==x:
            return True
        return False
    def separatedigits(self,x):
        digits=[]
        while (x>0):
            digits.append(x%10)
            x=x//10
        return digits
