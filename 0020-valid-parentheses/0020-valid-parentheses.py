class Solution:
    def isValid(self, s: str) -> bool:
        # to do the checks we'd have to iterate over string 
        # s[0] must be an open paranthesis

        stack = []
        mapping = {")":"(", "}":"{","]":"["}

        for c in s:
            if c in mapping.values():
                stack.append(c)
            elif c in mapping.keys():
                if not stack or mapping[c] != stack.pop():
                    return False

        return not stack

