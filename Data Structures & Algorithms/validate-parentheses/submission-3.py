class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for bracket in s:
            if bracket in ('(', '[', '{'):
                stack.append(bracket)
            else:
                # No opening bracket to match this closing bracket
                if not stack:
                    return False

                top = stack.pop()

                # Check whether the types match
                if top != matching[bracket]:
                    return False

        # Valid only if every opening bracket was closed
        return not stack