#!/usr/bin/env python
# coding: utf-8

# In[ ]:


for value in range(1,50):
    if(value % 3 == 0 and value % 5 == 0):
        print(" fizzbuzz")
    elif(value % 3 == 0):
        print("fizz")
    elif (value % 5 == 0):
        print("buzz")
    else:
        pass
        print(value)

