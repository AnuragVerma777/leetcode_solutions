class Solution(object):
    def isValid(self, s):
        stack = []

        for char in s:
            if char in "([{":
                stack.append(char)

            elif char in ")]}":
                if not stack:
                    return False

                top = stack.pop()

                if char == ')' and top != '(':
                    return False
                if char == ']' and top != '[':
                    return False
                if char == '}' and top != '{':
                    return False

        return len(stack) == 0