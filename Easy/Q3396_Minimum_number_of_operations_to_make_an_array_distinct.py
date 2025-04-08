class Solution(object):
    def is_distinct(self,nums):
        for i in nums:
            if nums.count(i)>1:
                return False
        return True

    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        
        while len(nums)>0:
            is_distinct=self.is_distinct(nums)
            if not is_distinct:
                nums=nums[3:]
                count+=1
            else:
                break
        return count
