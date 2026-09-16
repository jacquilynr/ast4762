#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import numpy


# In[2]:


from hw3_jacquilyn_support_functions import square


# In[3]:


#Problem 2

#part h
print("Problem 2 Part h")

test_square_1= list(range(10))

print(square(test_square_1))


#part i
print("\nProblem 2 Part i")

test_square_2= numpy.arange(25).reshape(5,5)

print(square(test_square_2))


# In[4]:


#Problem 3
print("Problem 3")

from hw3_jacquilyn_support_functions import squareplot

squareplot(1, 7, 5, True)


# In[ ]:





# In[ ]:




