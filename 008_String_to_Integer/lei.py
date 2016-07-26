class Solution:
    # @param {string} str
    # @return {integer}
    def myAtoi(self, str):
    	sign = None
    	starting = False
    	res = 0
    	for i in str:
    		ascii = ord(i)
    		if starting == False:
    			if ascii == 32: # blank
    				continue
    			elif ascii == 43: # plus
    				sign = True
    				starting = True
    			elif ascii == 45: # minus
    				sign = False
    				starting = True
    			elif ascii >= 48 and ascii <= 57:
    				res = res*10 + ascii - 48
    				starting = True
    			else:
    				break
    		else:
    			if ascii >= 48 and ascii <= 57:
    				res = res * 10 + ascii - 48
    			else:
    				break
    	if sign == False:
    		res = -res
    	if res >= pow(2, 31):
    		return pow(2, 31)-1
    	elif res < -pow(2,31):
    		return -pow(2, 31)
    	else:
    		return res