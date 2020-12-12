#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_excel(r'C:\Users\user\Downloads\aspiring_minds_employability_outcomes_2015.xlsx')


# In[3]:


import seaborn as sns


# In[4]:


df


# In[13]:


df.describe()


# In[15]:


df.corr()


# In[ ]:





# In[ ]:





# # plot 1 == lmplot

# In[5]:


sns.lmplot(x='Salary', y='10percentage', data=df)


# # plot 2 = voilinplot

# In[ ]:





# In[9]:


sns.set_style('whitegrid')
 
plt.figure(figsize=(15,10))
sns.violinplot(x='Salary', y='Gender', data=df)


# # plot 3 = heatmap

# In[11]:


sns.heatmap(df.corr())


# In[ ]:





# # plot 4 =catplot 

# In[17]:


sns.catplot(x='GraduationYear', y='collegeGPA', kind='swarm', data=df)


# # plot 5 = jointplot

# In[18]:


sns.jointplot(data=df, x="GraduationYear", y="Salary")


# # plot6 = pie chart 

# In[20]:


sizes = df.Gender.value_counts().values


# In[25]:


labels = df.Gender.value_counts().index
labels


# In[ ]:





# In[26]:


plt.pie(sizes,labels=labels,autopct="%1.1f%%")


# # plot 7= fill plot

# In[ ]:





# In[31]:


plt.fill("time", "signal",
        data={"time": [0, 1, 2], "signal": [0, 1, 0]})


# In[ ]:





# In[37]:


plt.bar(df['Gender'],df['Salary'])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




