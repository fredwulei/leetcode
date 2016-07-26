class Solution:
    # @param {string} s
    # @return {string}
    def longestPalindrome(self, s):
    	longest = 0
    	longest_str = None
    	l = len(s)
    	m = l/2
    	if l == 1:
    	    return s
    	# case 1: 'abc|cba'
    	for i in xrange(l-1):
    		offset = -((i+1)/2) if i % 2 ==0 else (i+1)/2
    		pos = m+offset
    		front =  s[:pos]
    		back = s[pos:]
    		ismatch = True
    		match_length = min(len(front),len(back))
    		if match_length*2 <= longest:
    			continue
    		for j in xrange(match_length):
    			if front[-j-1] != back[j]:
    				ismatch = False
    				if j*2 > longest:
    					longest = j*2
    					longest_str = front[-j:]+back[:j]
    				break
    		if ismatch == True:
    			longest = match_length*2
    			longest_str = front[-match_length:]+back[:match_length]
    	
    	# case 2: 'abcba'
    	m = (l+1)/2
    	for i in xrange(l-2):
    		offset = -((i+1)/2) if i % 2 == 0 else (i+1)/2
    		pos = m+offset
    		front = s[:pos-1]
    		back = s[pos:]
    		ismatch = True
    		match_length = min(len(front),len(back))
    		if match_length*2+1 <= longest:
    			continue
    		for j in xrange(match_length):
    			if front[-j-1] != back[j]:
    				ismatch = False
    				if j*2+1 > longest:
    					longest = j*2+1
    					longest_str = front[-j:]+s[pos-1]+back[:j]
    				break
    		if ismatch == True:
    			longest = match_length*2+1
    			longest_str = front[-match_length:]+s[pos-1]+back[:match_length]
    	return longest_str