class Solution(object):
    def isValid(self, s):
        stack = []
        for ch in s:
            if ch in '({[':
                stack.append(ch)
            elif not stack:
                return False
            else:
                if ((ch == ']' and stack.pop() != '[') or
                    (ch == '}' and stack.pop() != '{') or
                    (ch == ')' and stack.pop() != '(')):
                    return False
        return len(stack) == 0

# second try
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = [] #stack for storing brackets
        
        for bracket in s:
            if bracket in "({[":
                stack.append(bracket)
                
            else:
                if stack:
                    bracketInStack = stack.pop()
                    
                    if ((bracket == ')' and bracketInStack != '(') or
                        (bracket == '}' and bracketInStack != '{') or
                        (bracket == ']' and bracketInStack != '[')):
                        return False
                        
                else:
                    return False
                
        return bool(len(stack) == 0)