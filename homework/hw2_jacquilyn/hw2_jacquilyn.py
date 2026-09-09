#!/usr/bin/env python
# coding: utf-8

# In[2]:


#imports

import numpy as np
import matplotlib.pyplot as plt


# In[3]:


#Problem 2 
print("Homework 2 Problem 2")

#A
print("\nA")

#a1: create an array
x= np.arange(0,1001)    #1001 includes 1000 in array

#a2: print array's datatype, minimum, and maximum
print (x.dtype)
print (x.min())
print (x.max())



#B
print ("\nB")

#b1: re-scale 
x = x*((2 * np.pi)/ 1001)

#b2: print minimum and maximum
print (x.min())
print (x.max())



#C and D
print ("\nC and D")

#c: new array y is the sine of array x
y= np.sin(x)

#d: printing element 234 from y (the 235th element)
print (y[235])





# In[7]:


#Problem 3
print("Problem 3")



#A: make a publication ready plot of array y vs array x
print ("\nA")

plt.ion()    #turning on interactive mode
threea= plt.plot (y, x, color= 'pink')    #making baseline plot (in pink!!)

#making the plot publication ready:
plt.xlabel ('Y', fontsize= 14)
plt.ylabel ('X', fontsize= 14)
plt.title ('Array Y vs. array X');    #semicolon to remove the text line that was printing



#B: saving the plot as a PNG
plt.savefig('hw2_problem3_plot1.png')


# In[24]:


#Problem 4
print("Problem 4")


#A
print("\nA")

#a1: make a "ramp" array with 101 evenly spaced elements from -1 to 1
r= np.linspace(-1, 1, num=101)




# In[29]:


#a2: clip the array to remain between -.5 and .5
rclipped= np.clip(r, -.5, .5)




#B:
print("\nB")

#b1: in the same plot, plot both the original and clipped arrays
plt.plot (r, color= 'pink')
plt.plot (rclipped, color= 'purple')

#Adding plot labels
plt.xlabel ('X', fontsize= 14)
plt.ylabel ('Y', fontsize= 14)
plt.title ('Clipped Ramp');

#b2: saving the plot as a pdf:
plt.savefig ('hw2_jacquilyn_problem4_plot1.pdf')


# In[2]:


#Problem 5
print('Problem 5')

first_url= '''My first URL is https://sunpy.org/ which will bring you to the page to install sunpy. 
            Sunpy is a python extention that is free and open source, originally developed by a group
            from NASA's Goddard Flight Center. The package is targeted for those in solar physics with
            a goal to help them complete their research and other works more easily. This program allows
            users to download solar data from online through python, allows for data mapping, can help
            visualize solar phenomena, along with other functions useful in the field.'''

second_url= '''My second URL is https://pypi.org/project/ephem/ which will take you to the page from which 
            you can install PyEphem. This python package allows for the computation of the position of many
            different celestial objects in our solar system. This package is based on the language C, applied
            into python. This program is useful for Earth-centered calculations and beyond.'''

print('\n', first_url)
print('\n', second_url)







