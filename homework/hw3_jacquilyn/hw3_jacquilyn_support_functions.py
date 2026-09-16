#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Imported libraries
'''Included here are any libraries needed for the functions to run correctly'''

import os
import numpy
import matplotlib
import matplotlib.pyplot


# In[4]:


#Imported functions from other files


# In[5]:


#Function 1
def square(x):
    import numpy
    return numpy.square(x)

    ''' 
    Computes the square of a scalar or an array-like input of any dimension or numerical type and returns its square


    Parameters
    ----------
    x: array_like, or numerical type


    Returns
    -------
    output: array_like or single value
      the square of user's input (x). output type depends on input type


    Example
    -------
    >>> final= square(3)
    >>> print(final)
    9


    >>> a= (2, 3, 6)
    >>> square(a)
    (4, 9, 36)

    '''




# In[9]:


#Tests

a= (5, 7, 8)
b= numpy.arange(6).reshape(3,2)

aprime= square(a)

bprime= square(b)

print(aprime)
print(bprime)


# In[ ]:




