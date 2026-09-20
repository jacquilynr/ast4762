#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Jacquilyn Reilly
# Homework 4
# 9/20/2026


# In[2]:


#imports 

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


# In[3]:


#Problem 2
print("Problem 2:")


#Part A
#A function that draws a random sample of N draws from a Gaussian dist. with width sigma and mean mu
print("\n    Part A:")

def drawrandom(N, sigma, mu):
    sample= np.random.normal( loc= mu, scale= sigma, size= N)

    return(sample)


# In[4]:


#Part A continued...
#Use the function to make a sample of 10,000 draws from a pop. of sigma=13 and mu=55

twoB= drawrandom(10000, 13, 55)


# In[8]:


#Part B
print("\n    Part B:")
#Plot the histogram of your sample
#with bins x= 0 to 100 with 1 unit width

#define specified bins firts
spec_bins= np.arange(0, 101, 1)

#Now plot histogram using bins
plt.hist(twoB, bins= spec_bins, color= 'pink')

#Make the plot publication ready
plt.title("Random Sample")
plt.xlabel("Value")
plt.ylabel("Count")
plt.show()

#save it as a PNG with correct name
plt.savefig("hw4_jacquilyn_problem2_graph1.png")


# In[7]:


#Part C
print("\n    Part C:")

#Overplot a Gaussian distribution with the same mu and sigma as the histogram
#Approximate the integration between bin boundaries by evaluating the Gaussian at the center of each bin
#Multiply the function by total number of draes to get expected values

def gaussian(n, sigma, mu):
    return (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((n - mu) / sigma) ** 2)


#Begin with the same histogram
plt.hist(twoB, bins= spec_bins, color= 'pink')

#Add gaussian fucntion on top
x= (spec_bins[:-1] + spec_bins[1:])/2
y= (gaussian(x, 13, 55))*10000           #scaling gaussian to match histogram x and y axis

plt.plot(x, y, color= 'purple', linewidth= 2, label= 'Gaussian')

#Make plot publication ready
plt.title("Gaussian Overplot")
plt.xlabel("Value")
plt.ylabel("Density")

#Save as new png file
plt.savefig("hw4_jacquilyn_problem2_graph2.png")


# In[ ]:




