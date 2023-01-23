l=input().split()
stack=[]
for i in range(len(l)):
    if l[i]=='+':
        b=stack.pop()
        a=stack.pop()
        stack.append(int(a)+int(b))
    elif l[i]=='-':
        b=stack.pop()
        a=stack.pop()
        stack.append(int(a)-int(b))
    elif l[i]=='*':
        b=stack.pop()
        a=stack.pop()
        stack.append(int(a)*int(b))
    else:
        stack.append(l[i])
print(stack[0])