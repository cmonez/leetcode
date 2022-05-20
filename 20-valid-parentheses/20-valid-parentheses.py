class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
    
        stack = []
        closeToOpen = {")": "(", "]":"[", "}": "{"}
        for char in s:
            if char == "(" or char == "[" or char == "{":
                stack.append(char)
            elif  char == ")" or char == "]" or char == "}":
                if len(stack) == 0:
                    return False
                last_in = stack.pop()
                if last_in != closeToOpen[char]:
                    return False
            else:
                return False
            
        if len(stack) == 0:
            return True
        return False
            
        
        