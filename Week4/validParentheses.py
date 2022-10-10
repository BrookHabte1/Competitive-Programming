class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        flag = True
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "{" or s[i] == "[":
                stk.append(s[i])                
            elif s[i] == ")" or s[i] == "}" or s[i] == "]":
                if len(stk) == 0:
                    return False
                    
                else:
                    if s[i] == ")" and stk[-1] == "(":
                        stk.pop()
                    elif s[i] == "}" and stk[-1] == "{":
                        stk.pop()
                    elif s[i] == "]" and stk[-1] == "[":
                        stk.pop()
                    else:
                        return False
                        
        return flag if len(stk) == 0 else False
        