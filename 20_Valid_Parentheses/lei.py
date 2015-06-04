class Solution:
    # @param {string} s
    # @return {boolean}
    def isValid(self, s):
        stack = []
        for c in s:
            if c in '([{':
                stack.append(c)
            else:
                if len(stack) <= 0:
                    return False
                a = stack.pop()
                print 'a', a
                if a == '(' and c == ')':
                    pass
                elif a == '[' and c == ']':
                    pass
                elif a == '{' and c == '}':
                    pass
                else:
                    return False
        if len(stack) > 0:
            return False
        return True