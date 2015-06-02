class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSum(self, nums):
    	nums = sorted(nums)
    	res = []
    	for i in xrange(len(nums)):
    		for j in xrange(i):
    			if j+1<i and nums[j+1] == nums[j]:
    				continue
    			c = -(nums[i] + nums[j])
    			if c in nums[i+1:]:
    				a = [nums[j], nums[i], c]
    				if not a in res:
    					res.append([nums[j], nums[i], c])
    	return res
