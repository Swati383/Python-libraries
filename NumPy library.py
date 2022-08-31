#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


#NumPy stands for numerical python and secientific computing library we can use it without do coding.
#NumPy has multidemension dementional array.
#1. How to create NumPy array as Single demensinal and multi demensions array.


# In[4]:


import numpy as np


# In[6]:


#single demensions
n1= np.array ([10,20])
n1


# In[8]:


#Multi demensional array
n1= np.array ([[10,20,30] , [60,70, 80]])
n1


# In[ ]:


#initailization of NumPy with different methods
#1.zero method #2. full method #3. arange method #4.random.randint method


# In[14]:


#1. zero method : In which we put element as zero so that we can manupulate later on.
import numpy as np
n2= np.zeros ((0,0))
n2


# In[16]:


#2. full method it use to fill the element as numerical values.
n3=np.full([12,13],10)
n3 # it is showing 12 rows and 13 columns with the value of 10.


# In[21]:


#3. arange method intializing the NumPy array with range.
n4=np.arange(10,200)
n4


# In[24]:


n5=np.arange(10,100,5)
n5 #five is showing the diffrenece with the range 10-100 it never shows the last value.


# In[ ]:


#how to check or change the shape of NumPy array.


# In[27]:


#check shape
n5.shape


# In[32]:


n6=np.array([[12,10] ,[13,14]]) 
n6


# In[38]:


#change the shape of elements in rows into columns and columns into rows.
n6.shape=(2,2)
n6.shape


# In[42]:


#how to join to NumPy array, here is three ways to join two or more than two arrays
#1.vstack use for add arrays vertically.
#2.hstack use for add arrays horizentally.
#3.column_stack use for add array in columns
#1. 
n7=np.array ([[12,13, 14], [15,16,170],[20,23,22]])
n8=np.array ([[10,20,20] , [12,12,12,] , [13,12,14]])


# In[43]:


n7


# In[45]:


n8


# In[51]:


np.vstack((n7,n8))


# In[49]:


np.hstack((n7,n8))


# In[53]:


np.column_stack ((n7,n8))


# In[ ]:


#Opreation in NumPy array are two type intersection opreation and diffretiate operation.


# In[56]:


#Intersection opreation : its is useful to find the common elements from different arraies.
n9=np.array([10,20,30,40,50])
n10=np.array ([10,19,20,30,29])
np.intersect1d (n9,n10)


# In[57]:


# diiferentiat method use to find the values are uniques from different arraies.
np.setdiff1d (n9,n10)


# In[58]:


np.setdiff1d (n10,n9)


# In[ ]:


# NumPy mathemetical arraies "SUM" (LIKE SOLVE MATRIX ADDITION) 


# In[60]:


n11= np.array ([12,13,14])
n11


# In[61]:


n12=np.array([13,13,24])
n12


# In[63]:


np.sum([n11,n12])


# In[65]:


np.sum (([n11,n12]), axis=0) #axis=0 parameter used to addition of row elements.


# In[66]:


np.sum (([n11,n12]), axis=1) #axis=1 parameter used to additon of columns elements.


# In[ ]:


#basic numpy array mathemetics opreations 


# In[68]:


#!. basic addition
n13=np.array([10,20,30])
n13


# In[71]:


n13=n13+1
n13


# In[73]:


#2. basic substraction
n14=np.array([12,13,141])
n14


# In[74]:


n14=n14-1


# In[75]:


n14


# In[ ]:


#3. basic multipication


# In[76]:


n14=n14*2


# In[78]:


n14


# In[79]:


sonn14=n14/2 #4. basic divi


# In[80]:


n14


# In[ ]:


#statistics function in numpy library 1. mean 2. median 3. standard deviation


# In[82]:


n15= ([[12,45,78], [41,78,45]])


# ##### 

# In[83]:


n15


# In[84]:


np.mean (n15) # mean


# In[86]:


np.median (n15) # median


# In[87]:


np.std (n15) #standaed deviation


# In[ ]:


# how to save and load your NumPy arraies


# In[89]:


#save
n16=([[19,29,39], [12,39,49]])
n16


# In[90]:


np.save ('my_Numpy', n16)


# In[93]:


#laod 
n17=np.load('my_Numpy.npy')


# In[ ]:


n17


# In[ ]:




