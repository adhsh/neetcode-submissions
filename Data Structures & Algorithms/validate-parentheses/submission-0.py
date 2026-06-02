class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {")":"(", "}":"{", "]":"["}

        for item in s:
            if item in pairs:
                if not stack or stack[-1] != pairs[item]:
                    return False
                stack.pop()
            else:
                stack.append(item)

        return not stack