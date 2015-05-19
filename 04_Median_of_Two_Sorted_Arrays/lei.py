class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def getMedian(self, nums):
    	l = len(nums)
    	if l % 2 ==0:
    		return (nums[l/2-1]+nums[l/2])/2.0
    	else:
    		return nums[(l-1)/2]
    def findMedianSortedArrays(self, nums1, nums2):
    	if len(nums1) < len(nums2):
    		a1 = nums1
    		a2 = nums2
    	else:
    		a1 = nums2
    		a2 = nums1
    	len1 = len(a1)
    	len2 = len(a2)
    	while len1>2 and len2>2:
    		m1 = self.getMedian(a1)
    		m2 = self.getMedian(a2)
    		cut = len1 - (len1+2)/2
    		if m1 == m2:
    			return m1
    		elif m1>m2:
    			a1 = a1[:len1-cut]
    			a2 = a2[-(len2-cut):]
    		else:
    			a1 = a1[-(len1-cut):]
    			a2 = a2[:len2-cut]
    		len1 = len(a1)
    		len2 = len(a2)
    	if len1 == 0:
    	    return self.getMedian(a2)
    	m1 = self.getMedian(a1)
    	m2 = self.getMedian(a2)
    	if len1 == 1:
            if len2 == 1:
    	        return (m1+m2)/2.0
            elif len2 % 2 == 1:
    			if m1 < a2[len2/2-1]:
    				return (a2[len2/2-1] + a2[len2/2])/2.0
    			elif m1 >= a2[len2/2-1] and m1 <= a2[len2/2+1]:
    				return (m1+m2)/2.0
    			elif m1 > a2[len2/2+1]:
    				return (a2[len2/2] + a2[len2/2+1])/2.0
            else:
    			if m1 < a2[len2/2-1]:
    				return a2[len2/2-1]
    			elif m1 >= a2[len2/2-1] and m1 <= a2[len2/2]:
    				return m1
    			elif m1 > a2[len2/2]:
    				return a2[len2/2]
    	else:
    
    		if len2 == 2:
    			l = sorted([a1[0], a1[1], a2[0], a2[1]])
    			return self.getMedian(l)
    		elif len2 % 2 == 1:
    			l = sorted([m2, max(a1[0], a2[len2/2-1]), min(a1[1], a2[len2/2+1])])
    			return self.getMedian(l)
    		else:
    			l = sorted([a2[len2/2-1], a2[len2/2], max(a1[0], a2[len2/2-2]), min(a1[1], a2[len2/2+1])])
    			return self.getMedian(l)
    	return None       