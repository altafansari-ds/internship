#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_excel(r'C:\Users\user\Downloads\aspiring_minds_employability_outcomes_2015.xlsx')


# In[3]:


df


# In[4]:


df.columns


# In[5]:


df.head()


# In[24]:


df.groupby('ComputerScience').mean()
# 


# In[27]:


per=df.groupby('collegeGPA').mean()["Salary"]


# # collegegpa does not effect salary

# In[28]:


per.sort_values()


# In[33]:


df.collegeGPA.plot(kind = 'hist')


# In[32]:


df.groupby('collegeGPA').mean()['Salary'].plot()


# In[ ]:





# In[27]:


df[['12percentage','collegeGPA','Salary']].min()


# In[26]:


df[['12percentage','collegeGPA','Salary']].max()


# In[25]:


df[['12percentage','collegeGPA','Salary']].mean()


# In[24]:


df[['12percentage','collegeGPA','Salary']].median()


# # most earning designation

# In[12]:


dr=df.groupby('Designation').median()['Salary']   


# In[13]:


dr.sort_values()


# In[9]:


ar = df.Designation.head(10)
ar


# In[11]:


plt.figure(figsize=(20,20))
plt.bar(df['Designation'], df['Salary']) 
plt.ylabel("Salary")
plt.xlabel("Designation")


# # earning compared to cities
# 

# In[14]:


maxi = df.groupby("JobCity")['Salary'].mean()


# In[15]:


maxi.sort_values(inplace=True)
maxi


# # number of males recruited is more compared to females

# In[6]:


df.Gender.value_counts()


# # cs students introversion

# In[36]:


plt.bar(df['extraversion'],df['ComputerScience'], color ='maroon',  
        width = 0.4)
# cs students introversion


# In[16]:


plt.bar(df['extraversion'],df['MechanicalEngg'], color ='Black',  
        width = 0.4)


# In[22]:


df.groupby('Domain').mean()


# In[5]:


df.groupby('English').mean()['Salary'].sort_values()


# In[12]:


df[['Logical','Quant']]


# In[19]:


plt.scatter(df['Logical'],df['Quant'])
plt.xlabel("logical")
plt.ylabel("quant")
plt.title("comparision btw logical and quant")


# # salary does not depend on logical ability

# In[27]:


df[['Logical','Salary']].sort_values(by=['Salary','Logical'])
# salary does not depend on logical ability


# In[ ]:





# In[27]:


df[['10percentage','CivilEngg','TelecomEngg','ElectricalEngg','MechanicalEngg','ComputerScience','openess_to_experience']].mean()


# In[ ]:





# In[ ]:





# In[ ]:




