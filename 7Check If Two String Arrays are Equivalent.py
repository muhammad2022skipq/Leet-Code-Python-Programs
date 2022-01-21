#Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

#A string is represented by an array if the array elements concatenated in order forms the string.

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        w1=""
        w2=""
        for i in range(len(word1)):
            w1=w1+word1[i]
        for j in range(len(word2)):
            w2=w2+word2[j]
        if w1==w2:
            return True
        return False
