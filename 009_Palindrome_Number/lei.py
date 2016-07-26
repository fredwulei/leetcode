class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        # return str(x) == str(x)[::-1]
    	rev = 0
    	num = x
    	while num >0:
    		d = num % 10
    		num = num /10
    		rev = rev*10 + d
    	if x == rev:
    		return True
    	else:
    		return False