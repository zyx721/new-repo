from collections import deque
class stack:
    def __init__(self):
        self.containt = deque()
    def push(self,val):
        self.containt.append(val)
    def pop(self):
        return self.containt.pop()
    def peek(self):
        return self.containt[-1]
    def is_empty(self):
        return len(self.containt)==0
    def size(self):
        return len(self.containt)
    def reverse_string(self,str):
        for i in str:
            self.push(i)
        reversed =''
        for i in range(self.size()):
            reversed += self.pop()
        return reversed
    def is_balanced(self,str):
        for i in str:
            if i == '(' or i == '{'or i == '[':
                self.push(i)
            if  (i == ')' or i == '}'or i == ']'):
                if not self.containt or (i == ')' and self.containt and self.peek() != '('):
                    return False
                if not self.containt or (i == ']' and self.containt and self.peek() != '['):
                    return False
                if not self.containt or(i == '}' and self.containt and self.peek() != '{'):
                    return False
                self.pop()
        return True

stack =stack()
# print(stack.reverse_string("We will conquere COVID-19"))
print(stack.is_balanced("({a+b})"))
print(stack.is_balanced("))((a+b}{"))
print(stack.is_balanced("((a+b))"))
print(stack.is_balanced("))"))
print(stack.is_balanced("[a+b]*(x+2y)*{gg+kk}"))

