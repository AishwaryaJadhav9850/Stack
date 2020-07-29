# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 23:52:36 2020

@author: SUPERNOVA2813
"""
from collections import deque
class StackDeque:
    def __init__(self):
        self.stack=deque()
        self.top=-1
    
    def push(self):
        i=int(input("Enter the element to push onto Stack:-"))
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
       print(self.stack.pop())

s=StackDeque()
print("\nWelcome to Stack program using Deque Collections")
while(1):    
    print("\n1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Top")
    print("5. isEmpty")
    print("6. EXIT")
    ch=int(input("Enter your choice:-"))
    if ch==1:
        s.push()
        s.display()
    elif ch==2:
        s.pop()
        s.display()
    elif ch==3:
        s.display()
    elif ch==4:
        s.peek()
    elif ch==5:
        s.empty()
    elif ch==6:
        break
    else:
        print("Please enter correct choice!")
    
        
