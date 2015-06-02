class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def threeSumClosest(self, nums, target):
    	nums = sorted(nums)
    	closest = None
    	l = len(nums)
    	for i in xrange(l-2):
    		j = i + 1
    		k = l - 1
    		while(j < k):
    			threesum = nums[i]+nums[j]+nums[k]
    			if nums[i]+nums[j]+nums[k] == target:
    				return target
    			elif nums[i]+nums[j]+nums[k] < target:
    				j += 1
    			else:
    				k -= 1
    			if closest == None or abs(threesum-target) < abs(closest-target):
    				closest = threesum
    	return closest