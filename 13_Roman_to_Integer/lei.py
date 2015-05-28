class Solution:
    # @param {string} s
    # @return {integer}
    def romanToInt(self, s):
    	res = 0
    	symbols = 'IVXLCDM'
    	numbers = [1, 5, 10, 50, 100, 500, 1000]
    	last = 6
    	for i in s:
    		d = symbols.index(i)
    		if d > last:
    			res -= 2*numbers[last]
    		res += numbers[d]
    		last = d
    	return res
        