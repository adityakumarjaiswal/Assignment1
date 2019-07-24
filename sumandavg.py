#!/usr/bin/env python
# coding: utf-8

# In[ ]:


input =int(input("Enter the size of the list\n"))
sum=0

for i in range(1,input+1):
    sum=sum+i
print("sum of given Numbers are",sum)
avg=sum/input
print("average of given number",avg)

