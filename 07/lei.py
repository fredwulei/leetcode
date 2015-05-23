class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
    	num = x if x >= 0 else -x
    	res = 0
    	while num > 0:
    		d = num % 10
    		num = num / 10
    		res = res * 10 + d
    	if res > pow(2, 31):
    		return 0
    	return res if x >=0 else -res