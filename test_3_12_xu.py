#!/usr/bin/env python
# coding: utf-8

# ## 通过索引访问一维数组

# #### 代码 2-18 使用索引访问一维数组

# In[3]:


import numpy as np
arry = np.arange(10)
print('索引结果为：\n',arry[5])


# In[4]:


print('索引结果为：\n',arry[3:5])


# In[5]:


print('索引结果为：\n',arry[:5])


# In[6]:


print('索引结果为：\n',arry[5:])


# In[7]:


arry[2:5] = 97,98,99


# In[8]:


print('替换后的数组为：\n',arry)


# In[9]:


print('索引结果为：\n',arry[1:-1:3])


# #### 代码 2-19 使用索引访问多维数组

# In[12]:


arry = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
print('创建的二维数组为：\n',arry)


# In[13]:


print('索引结果为：\n',arry[0,3:5])


# In[14]:


print('索引结果为：\n',arry[-1,3:5])


# In[19]:


print('索引结果为：\n',arry[0,2:])


# In[20]:


print('索引结果为：\n',arry[0:1,3:5])


# In[21]:


print('索引结果为：\n',arry[2:4,3:5])


# In[22]:


print('索引结果为：\n',arry[2:])


# In[23]:


print('索引结果为：\n',arry[:,2])


# #### 代码 2-20 使用整数函数和布尔值索引访问多维数组

# In[24]:


print('索引结果为：\n',arry[[(0,1,2),(1,2,3)]])


# In[27]:


arry = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
print('创建的二维数组为：\n',arry)


# In[29]:


print('索引结果为：\n',arry[1:,(0,2,3)])


# In[30]:


mask = np.array([1,0,1],dtype = np.bool)
print('索引结果为：\n',arry[mask,2])


# In[ ]:




