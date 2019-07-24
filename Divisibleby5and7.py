#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Assignment no 1:-
# Divisible by 5 and 7
for value in range(1500,2701):
	#print(value)
	if(value%5==0 and value%7==0):
		print(value ,"is Divisible by 5 and 7")
	else:
		continue

