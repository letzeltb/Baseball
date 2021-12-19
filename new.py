#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt


# In[5]:


a = pd.read_csv(r'C:/Users/Brian/Desktop/baseball_logistic/batting.csv')


# In[7]:


m = pd.read_csv(r'C:/Users/Brian/Desktop/baseball_logistic/Master.csv')


# In[6]:


a.head()


# In[13]:


a.describe()


# In[8]:


m.head()


# In[9]:


m.columns


# In[15]:


name = m[['playerID','debut', 'finalGame','birthCountry',
       'birthState', 'birthCity', 'nameFirst', 'nameLast',
       'nameGiven']]


# Tesrt
# asdgasdg;lkjdasfj
# 
# asdlkjfasd
#     

# In[16]:


final = a.merge(name, how='left', on='playerID')


# teetewstaewetweta

# In[17]:


final.head()


# In[18]:


final.columns


# In[19]:


new = final[['playerID','nameFirst', 'nameLast','yearID', 'stint', 'teamID', 'lgID', 'G', 'AB', 'R', 'H',
       '2B', '3B', 'HR', 'RBI', 'SB', 'CS', 'BB', 'SO', 'IBB', 'HBP', 'debut', 'finalGame', 'birthCountry', 'birthState',
       'birthCity']]


# In[35]:


new[(new['nameFirst']=='Rick') & (new['nameLast']=='Lancellotti')]


# In[29]:


new.sort_values(by='HBP',ascending=False)


# In[27]:


a[a['3B']>30].sort_values(by='AB',ascending=False)


# In[33]:


a[['playerID','yearID','G','H']].sort_values(by='H', ascending=False)


# In[61]:


# Create data
x = a['2B']
y = a['RBI']
colors = (0,0,0)
area = np.pi*3

# Plot
plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.title('Scatter plot pythonspot.com')
plt.xlabel('2B')
plt.ylabel('RBI')
plt.show()


# In[ ]:




