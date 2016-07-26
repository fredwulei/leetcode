class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
    	if numRows == 1:
    		return s
    	res = ['' for _ in xrange(numRows)]
    	col_index = 0
    	row_index = 0
    	step = 1
    	for i in s:
    		res[row_index]+= i
    		row_index+=step
    		if row_index > numRows-1 or row_index < 0:
    			step = - step
    			row_index += 2*step
    	r = ''
    	for s in res:
    		r += s
    	return r
        