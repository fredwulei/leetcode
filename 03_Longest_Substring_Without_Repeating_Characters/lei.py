class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
    	current = ''
    	longest = 0
    	for ind, c in enumerate(s):
    		pos = current.find(c)
    		current+=c
    		if pos >= 0:
    			if len(current)-1>longest:
    				longest = len(current)-1
    			current = current[pos+1:]
    	if len(current)>longest:
    		longest = len(current)
    	return longest