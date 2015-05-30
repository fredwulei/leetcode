class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
    	if len(strs) <= 0:
    		return ''
    	res = strs[0]
    	for s in strs[1:]:
    		l = len(s)
    		for i in xrange(len(res)):
    			if i >= l or res[i] != s[i]:
    				res = res[:i]
    				break
    	return res