import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stacks = []
        for i in range(len(tokens)):
                        if tokens[i] != '+' and tokens[i] != '-' and tokens[i] != '*' and tokens[i] != '/':
                                stacks.append(int(tokens[i]))
                        else:
                                a=stacks.pop()
                                b=stacks.pop()
                                if tokens[i] == '+':
                                        stacks.append(b+a)
                                elif tokens[i] == '-':
                                        stacks.append(b-a)
                                elif tokens[i] == '*':
                                        stacks.append(b*a)
                                elif tokens[i] == '/':
                                        if a<0 and b>0:
                                                stacks.append(math.ceil(b/a))
                                        elif a>0 and b<0:
                                                stacks.append(math.ceil(b/a))
                                        else:
                                                stacks.append(math.floor(b/a))
        return stacks[0]
        