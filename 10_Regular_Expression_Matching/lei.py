import copy
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        if len(p) == 0:
            if len(s) == 0:
                return True
            else:
                return False
        
        states = [[]]
        for i,c in enumerate(p):
            if c == '*':
                pass
            else:
                if i+1 < len(p) and p[i+1] == '*':
                    states[-1].append((c, len(states)-1))
                    states[-1].append(('eps', len(states)))
                    states.append([])
                else:
                    states[-1].append((c, len(states)))
                    states.append([])

        curStates = set()
        curStates.add(0)
        temp = set()
        temp.add(0)
        while len(curStates):
            st = curStates.pop()
            for ch, successor in states[st]:
                if ch == 'eps':
                    curStates.add(successor)
                    temp.add(successor)

        curStates = temp
        for i,c in enumerate(s):
            temp = set()
            tt = copy.copy(curStates)
            t2 = set()
            arr = []
            while len(tt):
                st = tt.pop()
                for ch, successor in states[st]:
                    if successor in arr:
                        continue
                    else:
                        if ch == c or ch == '.':
                            arr.append(successor)
            t2 = copy.copy(arr)
            while len(t2):
                st = t2.pop()
                for ch, successor in states[st]:
                    if ch == 'eps' and successor not in arr:
                        arr.append(successor)
                        t2.append(successor)

            temp.update(arr)
            curStates = temp
            curStates.add(-1)
            
        return max(curStates) == len(states) -1