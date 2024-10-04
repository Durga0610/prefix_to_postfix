class stack:
    def __init__(self,size):
        self.stack=[]
        self.size=size
    def push(self,a):
        if len(self.stack)==self.size:
            print("Stack overflow")
        else:
            self.stack.append(a)
    def pop(self):
        if not self.stack:
            return -1
        else:
            return self.stack.pop()
    def priority(self,a):
        if a=='+' or a=='-':
            return 1
        if a=='*' or a=='/':
            return 2
        if a=='^':
            return 3
        if a=='(':
            return 0
        return 0
    def infix_to_postfix(expression):
        postfix=[]
        for char in expression:
            if char.isalnum():
                postfix.append(char)
            elif char=='(':
                obj.push(char)
            elif char==')':
                x=obj.pop()
                while (x!='('):
                    postfix.append(x)
                    x=obj.pop()
            else:
                while obj.stack and obj.priority(obj.stack[-1])>=obj.priority(char):
                    postfix.append(obj.pop())
                obj.push(char)
        while obj.stack:
             postfix.append(obj.pop())
        return ''.join(postfix)
obj=stack(20)
expression=input("Enter the expression:")
result=infix_to_postfix(expression)
print(f"The postfix expression is :{result}")
