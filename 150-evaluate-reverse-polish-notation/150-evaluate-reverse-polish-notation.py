class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in range(len(tokens)):
            try:
                x=int(tokens[i])
                stack.append(x)
            except:
                if tokens[i]=="+":
                    a=stack.pop()
                    b=stack.pop()
                    stack.append(b+a)
                if tokens[i]=="-":
                    a=stack.pop()
                    b=stack.pop()
                    stack.append(b-a)
                if tokens[i]=="*":
                    a=stack.pop()
                    b=stack.pop()
                    stack.append(a*b)
                if tokens[i]=="/":
                    a=stack.pop()
                    b=stack.pop()
                    c=int(b/a)
                    stack.append(c)
        return stack[-1]
        