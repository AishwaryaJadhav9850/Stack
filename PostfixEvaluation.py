# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 09:02:12 2020

@author: SUPERNOVA2813
"""

from collections import deque
class StackDeque:
    def __init__(self):
        self.stack=deque()
        self.top=-1
    
    def push(self,i):
        self.stack.append(i)
        self.top=self.top+1
        
    def display(self):
        if(self.top<0):
            print("Stack is empty!")
            return 
        print("\n")
        for i in self.stack:
            print(i ,end="-->")
    
    def peek(self):
        if(self.top<0):
            print("Stack is empty!")
            return
        print("Top of the stack is :",self.stack[self.top])   
    
    def empty(self):
        if(self.top<0):
            print("Stack is empty!")
            return
        print("Stack has ",self.top+1," elements")
    
    def pop(self):
       if(self.top<0):
            print("Stack is empty!")
            return
       self.top=self.top-1 
       return self.stack.pop()

s=StackDeque()
ops = '+-*/'
string=[x for x in input("Enter the Postfix expression for Evaluation:").split(" ")]
for ch in string:
    if ch.isdigit()==True:
        s.push(int(ch))
        s.display()
    elif ch in ops:
        if(s.top<1):
            print("Expression is wrong!")
            break
        a=s.pop()
        b=s.pop()
        if ch=='+':
            s.push(a+b)
            s.display()
        elif ch=='-':
            if a>b:
                s.push(a-b)
            else:
                s.push(b-a)
            s.display()
        elif ch=='*':
            s.push(a*b)
            s.display()
        elif ch=='/':
            if a>b:
                s.push(a/b)
                s.display()
            else:
                s.push(b/a)
                s.display()
        else:
            print("Operator in Expression is wrong!")
            break
if(s.top<0):
    print("Expression is wrong!")  
else:         
    print("\n\nThe result is ",s.pop())        
