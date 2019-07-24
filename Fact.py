#!/usr/bin/env python
# coding: utf-8

# In[1]:


input =int(input("Enter the size in number\n"))
#input=3
fact=1
i=1
if(input==0):
    print("factorial of given no is 1")
elif(input==1):
    print("factorial of given no is 1")
else:
    print("given no is: ",input)
    while i<=input:
        fact=fact*i
        i=i+1
    print("Factorial of the given number is ",fact)

