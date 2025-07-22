class Solution:
    def isValid(self, s: str) -> bool:
        # to do the checks we'd have to iterate over string 
        # s[0] must be an open paranthesis

        stack = []
        mapping = {")":"(", "}":"{","]":"["}

        for c in s:
            if c in mapping:
                # for closing bracket, check stack
                if stack and stack[-1] == mapping[c]:
                    stack.pop() #remove matching opening bracket
                else:
                    return False #if latest bracket isn't matching
            else:
                #push opening bracket on stack
                stack.append(c)

        return not stack #true if stack empty

