#A sentence is a string of single-space separated words where each word consists only of lowercase letters.

#A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

#Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.

class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        uncommon=[]
        singleword1=self.singlewords(s1)
        singleword2=self.singlewords(s2)
        ws=s2.split()
        for i in singleword1:
            if i not in singleword2:
                
                if i not in ws:
                    uncommon.append(i)
        wss=s1.split()
        for j in singleword2:
            if j not in singleword1 and j not in wss:
                uncommon.append(j)
        return uncommon
    def singlewords(self,s1):
        words=[]
    
        w=s1.split()
        for i in range(len(w)):
            count=0
            for j in range(0,len(w)):
                if(i!=j and w[i]==w[j]):
                    count=count+1
            if(count==0):
                words.append(w[i])
        return words
