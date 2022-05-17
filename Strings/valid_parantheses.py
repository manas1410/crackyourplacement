'''
Problem url-https://leetcode.com/problems/valid-parentheses/submissions/
'''
'''
Approach:- using stack concept
'''
class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        ans = True
        for i in s:
            if i in ['(','[','{']:
                l.append(i)
            else:
                try:
                    if i == '}' and l[-1] == '{':
                        l.pop()
                    elif i == ']' and l[-1] == '[':
                        l.pop()
                    elif i == ')' and l[-1] == '(':
                        l.pop()
                    else:
                        ans = False
                        break
                except:
                    ans = False
                    break
        #print(l)
        if ans and len(l)==0:
            return True
        else:
            return False
