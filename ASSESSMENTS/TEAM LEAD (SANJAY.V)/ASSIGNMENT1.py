#!/usr/bin/env python
# coding: utf-8

# In[3]:


Basic Python

1. Split this string


# In[4]:


s = "Hi there Sam!"

s.split(" ")


# In[10]:


# 2. Use.format() to print the following string.

# Output should be: The diameter of Earth is 12742 kilometers.


# In[12]:


planet = "Earth"

diameter = 12742

print("The diameter of {} is {} kilometers.".format(planet, diameter))


# In[14]:


# 3. In this nest dictionary grab the word "hello"


# In[15]:


d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}

d['k1'][3]['tricky'][3]['target'][3]


# In[16]:


# Numpy


# In[17]:


import numpy as np


# In[18]:


# 4.1 Create an array of 10 zeros?

# 4.2 Create an array of 10 fives?


# In[19]:


array_zeros = np.zeros(10)

array_zeros


# In[20]:


array_fives = np.ones(10)*5

array_fives


# In[21]:


# 5. Create an array of all the even integers from 20 to 35


# In[22]:


array_even = np.arange(20,35,2)

array_even


# In[25]:


# 6. Create a 3x3 matrix with values ranging from 0 to 8


# In[26]:


array_three = np.arange(0, 9).reshape(3,3)

array_three


# In[27]:


# 7. Concatenate a and b

# a = np.array([1, 2, 3]), b = np.array([4, 5, 6])


# In[28]:


a = np.array([1, 2, 3])

b = np.array([4, 5, 6])

array_concat = np.concatenate((a, b), axis=0)


# In[29]:


array_concat


# In[30]:


# Pandas

# 8. Create a dataframe with 3 rows and 2 columns


# In[31]:


import pandas as pd


# In[4]:


list1 = [['Sanjay', 21], ['Doren', 25], ['Joshua', 21]]


# In[5]:


list1 = pd.DataFrame(list1)


# In[6]:


list1


# In[35]:


# 9. Generate the series of dates from 1st Jan, 2023 to 10th Feb, 2023


# In[36]:


dates = pd.date_range(start='2023-01-01', end='2023-02-10')

dates


# In[ ]:


# 10. Create 2D list to DataFrame

# lists = [[1, 'xxx', 22], [2, 'yyy', 25], [3, 'zzz', 24]]


# In[3]:


import pandas as pd

lists = [[1, 'xxx', 22], [2, 'yyy', 25], [3, 'zzz', 24]]

pd.DataFrame(lists)


# In[ ]:





# In[ ]:




