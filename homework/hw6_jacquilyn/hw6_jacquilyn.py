#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Jacquilyn Reilly
# October 2
# Homework 6 (and Practicum 4)


# In[2]:


# Imports
import numpy as np
from astropy.io import fits
import os


# In[3]:


# Problem 2
#----------
print ("___Problem 2___")


# Part a
#-------

# Begin with minimal hardcodings:
datadir = "hw6_data/"
fext = ".fits"



# Part B
#--------

# Initialize lists for target images and dark images
objfile = []
darkfile = []


# Populate the lists
files = os.listdir(datadir)

for filename in files:

    if filename.startswith("rdpharocor_stars_13s_") and filename.endswith(fext):
        objfile.append(filename[:-len(fext)])

    elif filename.startswith("rdpharocor_dark_13s_") and filename.endswith(fext):
        darkfile.append(filename[:-len(fext)])


# Part C
#--------
print("\nPart C")

# Printing datadir, fext and the last elements of objfile and darkfile
print("Data directory: ", datadir)
print ("FITS extention: ", fext)
print ("Last object measurement: ", objfile[-1])
print ("Last dark measurement: ", darkfile[-1])



# Part D
#--------

# Reading object file and determining array size
objdata = fits.getdata(datadir + objfile[0] + fext)

# Determining size and assigning variables
ny, nx = objdata.shape




# Part E
#--------
print("\nPart E:")

# Defining variables containing the number of each measurement type
nobj= len(objfile)
ndark= len(darkfile)

'''
You should not hardcode these so the measurement can change automatically
as the size of the data changes.
'''

# printing ny, nx, nobj, and ndark
print("The image dimensions are: ", nx, " by ", ny)
print ("The number of object images is: ", nobj)
print("The number of dark images is: ", ndark)


# In[4]:


# Problem 3
#-----------
print("Problem 3")


# Part A
#--------
print("\nPart A")


# Create 3D arrays for the objects and for the darks
objdata3D = np.zeros((nobj, ny, nx), dtype=np.float64)
darkdata3D = np.zeros((ndark, ny, nx), dtype=np.float64)

# Print the arrays
print("Object data cube shape:", objdata3D.shape)
print("Dark data cube shape:", darkdata3D.shape)


# Part B
#--------
print("\nPart B")

# Populate both data arrays

# Object array
for i in range(nobj):

    objdata, objhead = fits.getdata(
        datadir + objfile[i] + fext,
        header=True
    )

    objdata3D[i] = objdata


# Dark array
for i in range(ndark):

    darkdata, darkhead = fits.getdata(
        datadir + darkfile[i] + fext,
        header=True
    )

    darkdata3D[i] = darkdata



# Print observation of each array:
print("Object DATE-OBS:", objhead["DATE-OBS"])
print("Dark DATE-OBS:", darkhead["DATE-OBS"])


# Why not Time Observation?
'''
We are specifically looking for the observation DATE of the images,
it is not important the chronological order for this observation.
''';


# In[5]:


# START OF HOMEWORK 6 INSTRUCTIONS
#----------------------------------
print("\nHomework 6 Instructions:")




# Problem 2
#-----------
print("\n\nProblem 2")


# Part A
#-------
def medcom(data):

    '''
    Median-combines a stack of images along the first axis.

    Uses axis 0 to create a 2D image by collapsing "image number" direction
    '''

    return np.median(data, axis=0)


# Part B
#--------
print("\nPart B:")

# callng function for dark data
darkmed = medcom(darkdata3D)

# printing pixel [217, 184]
print("Median dark shape:", darkmed.shape)
print("Median dark pixel [217, 184]:", darkmed[217, 184])



# Part C
#-------

#adding a HISTORY entry to dark header
darkhead["HISTORY"] = "Median-combined dark frame."


# Part D
#-------

#writing median dark into a file
fits.writeto(
    datadir + "dark_13s_med.fits",
    darkmed,
    header=darkhead,
    overwrite=True
)



# Part E
#-------
print("\nPart E:")

# printing before subtraction
print("Object pixel [217, 184] before subtraction:",
      objdata3D[0, 217, 184])

# subtracting median-combined dark frame from each object
objdata3D -= darkmed

# printing after subtraction
print("Object pixel [217, 184] after subtraction:",
      objdata3D[0, 217, 184])


# In[ ]:




