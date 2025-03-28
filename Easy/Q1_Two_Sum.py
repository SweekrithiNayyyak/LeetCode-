class Solution(object):
    def twoSum(self, nums, target):
        d={}
        for i in range(len(nums)):
            required=target-nums[i]
            if required in d.keys():
                return [d[required],i]
            d[nums[i]]=i
        return l
        
