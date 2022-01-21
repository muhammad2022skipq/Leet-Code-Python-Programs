#Given a binary array nums, return the maximum number of consecutive 1's in the array.
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        onescount=0
        previouscount=0
        l=len(nums)
        for i in range(l):
            if(nums[i]==1):
                
                onescount=onescount+1
            else:
                onescount=0
            if onescount>previouscount:
                    previouscount=onescount
        return previouscount
