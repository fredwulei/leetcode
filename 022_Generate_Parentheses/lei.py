class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        l = []
        self.add(l,'', n, n)
        return l
        
    def add(self, res, s, left, right):
        if left == 0 and right == 0:
            res.append(s)
            return
        if left > 0:
            self.add(res, s+'(', left-1, right)
        if right > left:
            self.add(res, s+')', left, right-1)