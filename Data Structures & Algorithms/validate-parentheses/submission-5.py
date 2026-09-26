class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closetoOpen = { ')': '(', '}': '{', ']':'['}

        # traverse on each char in input and check
        for c in s:
            # will traverse to input and check weither its closing 
            # bracket, to do so we can check in hash map
            if c in closetoOpen:
                # if its in closing bracket, will check our stack
                # should not be empty, its last element should be
                # matched other wise return false
                if stack and stack[-1] == closetoOpen[c]:
                    # if the stack last is matched with its open
                    # closed remove from stack and go ahead
                    stack.pop()
                else:
                    # if they don't match, or stack is empty init
                    # return False ")", "[)"
                    return False
            else:
                stack.append(c)
        return True if not stack else False
