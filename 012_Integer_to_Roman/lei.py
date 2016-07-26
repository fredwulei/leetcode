class Solution:
    # @param {integer} num
    # @return {string}
    def intToRoman(self, num):
    	res = ''
    	symbols = 'IVXLCDM'
    	st = str(num)
    	l = len(st)
    	k = (l-1)*2
    	for s in st:
    		d = int(s)
    		if d == 0:
    			pass
    		elif d >= 1 and d <= 3:
    			res += symbols[k]*d
    		elif d == 4:
    			res += symbols[k]+symbols[k+1]
    		elif d == 5:
    			res += symbols[k+1]
    		elif d >= 6 and d <= 8:
    			res += symbols[k+1] + symbols[k]*(d-5)
    		elif d == 9:
    			res += symbols[k] + symbols[k+2]
    		k -= 2
    	return res