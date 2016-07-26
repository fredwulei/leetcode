class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
    	cands = {}
    	for indi, i in enumerate(nums):
    		c = target - i
    		if c in cands:
    			return [cands[c]+1, indi+1]
    		cands[i] = indi
    	return None