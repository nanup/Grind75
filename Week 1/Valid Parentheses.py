class Solution(object):
    def isValid(self, s):
        stack = []
        for ch in s:
            if ch in '({[':
                stack.append(ch)
                print(stack)
            elif not stack:
                return False
            else:
                if ((ch == ']' and stack.pop() != '[') or
                    (ch == '}' and stack.pop() != '{') or
                    (ch == ')' and stack.pop() != '(')):
                    return False
        return len(stack) == 0