#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df = pd.read_csv('/Users/ks/Downloads/Paper1/MonthWiseMarketArrivals_Clean.csv')


# In[3]:


df.head()


# In[4]:


df.tail()


# In[5]:


df.dtypes


# In[6]:


df.tail(1)


# In[7]:


df.drop(df.tail(1).index, inplace = True)


# In[8]:


df.head()


# In[9]:


df.tail()


# In[10]:


df.dtypes


# In[11]:


df.iloc[:,4:7].head()


# In[12]:


df.iloc[:,2:7] = df.iloc[:,2:7].astype(int)


# In[13]:


df.dtypes


# In[14]:


df.head()


# In[15]:


df.describe()


# In[16]:


df.market.value_counts().head()


# In[17]:


df['state'] = df.market.str.split('(').str[-1]


# In[18]:


df.head()


# In[19]:


df['city'] = df.market.str.split('(').str[0]


# In[20]:


df.head()


# In[21]:


df.state.unique()


# In[22]:


df['state'] = df.state.str.split(')').str[0]


# In[23]:


df.state.unique()


# In[24]:


dfState = df.groupby(['state', 'market'], as_index=False).count()


# In[25]:


dfState.market.unique()


# In[26]:


state_now = ['PB', 'UP', 'GUJ', 'MS', 'RAJ', 'BANGALORE', 'KNT', 'BHOPAL', 'OR',
       'BHR', 'WB', 'CHANDIGARH', 'CHENNAI', 'bellary', 'podisu', 'UTT',
       'DELHI', 'MP', 'TN', 'Podis', 'GUWAHATI', 'HYDERABAD', 'JAIPUR',
       'WHITE', 'JAMMU', 'HR', 'KOLKATA', 'AP', 'LUCKNOW', 'MUMBAI',
       'NAGPUR', 'KER', 'PATNA', 'CHGARH', 'JH', 'SHIMLA', 'SRINAGAR',
       'TRIVENDRUM']


# In[27]:


state_new =['PB', 'UP', 'GUJ', 'MS', 'RAJ', 'KNT', 'KNT', 'MP', 'OR',
       'BHR', 'WB', 'CH', 'TN', 'KNT', 'TN', 'UP',
       'DEL', 'MP', 'TN', 'TN', 'ASM', 'AP', 'RAJ',
       'MS', 'JK', 'HR', 'WB', 'AP', 'UP', 'MS',
       'MS', 'KER', 'BHR', 'HR', 'JH', 'HP', 'JK',
       'KEL']


# In[28]:


df.state = df.state.replace(state_now, state_new)


# In[29]:


df.state.unique()


# In[30]:


df.head()


# In[31]:


df.index


# In[32]:


pd.to_datetime('January 2012')


# In[33]:


df['date'] = df['month'] + '-' + df['year'].map(str)


# In[34]:


get_ipython().run_line_magic('pinfo2', 'map')


# In[35]:


df.head()


# In[36]:


index = pd.to_datetime(df.date)


# In[37]:


df.index = pd.PeriodIndex(df.date, freq='M')


# In[38]:


df.columns


# In[39]:


df.index


# In[40]:


df.head()


# In[41]:


df.to_csv('MonthWiseMarketArrivals_Clean.csv', index = False)


# In[ ]:




