class Solution: 
    # @param {integer[]} height
    # @return {integer}
    def maxArea(self, height):
    	maxArea = 0
    	lower = height[0]
    	higher = lower
    	num = len(height)
    	for i in xrange(1,num):
    		hi = height[i]
    		if i+1< num and height[i+1] > lower and height[i+1]> hi:
    			continue
    		for j in xrange(i):
    			hj = height[j]
    			area = (i-j)*min(hi, hj)
    			if area > maxArea:
    				maxArea = area
    				lower = min(hi,hj)
    				higher = max(hi,hj)
    			if hj >= hi:
    				break
    	return maxArea