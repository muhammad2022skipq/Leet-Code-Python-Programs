#Given an input string s, reverse the order of the words.

#A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

#Return a string of the words in reverse order concatenated by a single space.

#Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        reverse=""
        words=s.split()
        a=(len(words)-1)
        for i in range(a,-1,-1):
            if (words[i]!=" "):
                for j in words[i]:
                    reverse=reverse+str(j)
                if i>0:
                    reverse=reverse+" "
        return reverse
        
