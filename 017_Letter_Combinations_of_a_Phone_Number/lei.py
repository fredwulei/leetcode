class Solution:
    # @param {string} digits
    # @return {string[]}
    def letterCombinations(self, digits):
    	mapping = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    	res = []
    	s = str(digits)
    	current = ''
    	for i in s:
    		d = int(i)
    		l = mapping[d]
    		if len(l) == 0:
    			continue
    		if len(res) == 0:
    			res = ['']
    		res = [ k+_ for k in res for _ in l]
    	return res