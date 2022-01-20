#Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
#The overall run time complexity should be O(log (m+n)).
#Python code

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged=self.merge(nums1,nums2)
        l=len(merged)
        
        if l%2!=0:
            return float(merged[l//2])
        else:
            
            return (merged[l//2]+merged[(l//2)-1]) /2
           
    def merge(self,l1,l2):
        i=0
        j=0
      
        merged=[]
        a=len(l1)
        b=len(l2)
        while i <a and j< b:
            if(l1[i]<=l2[j]):
                merged.append(l1[i])
                i=i+1
            else:
                merged.append(l2[j])
                j=j+1
            
        while(i<a):
            merged.append(l1[i])
            i=i+1
            
        while j<b:
            merged.append(l2[j])
            j=j+1
            
        return merged
